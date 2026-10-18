# Week 07 — Sequence Modeling and Transformers

[← Generative Models](week-06-generative-models.md) · **Week 7 of 11** · [Next: World Models →](week-08-world-models.md)

**Know these first:** reactive policies, RNNs, MDP, POMDP
**Topics:** RNNs, transformers, ViTs, LLMs, VLMs, VLAs (basic)
**Before the session:** *Attention Is All You Need*; ACT paper (Zhao et al.); pen and paper for the attention example.

## Outcomes

- Explain why a one-frame policy struggles and what sequence modeling changes.
- Write the attention equation and say what each part does.
- Describe tokens, positional encodings, causal masking, teacher forcing.
- Say what the KV cache stores, how big it gets, and how it differs from an RNN hidden state.
- Explain how text, images and robot actions go into one transformer, and why action chunking smooths motion.

## Core notes

### 0. Glossary

| Term | Meaning |
|---|---|
| Token | One unit the model reads: a subword, an image patch, or an action value |
| Embedding | Vector of numbers representing a token |
| Autoregressive | Generates one token at a time, each conditioned on all earlier ones |
| Policy | Maps what the robot sees to what it does |
| Trajectory | One full run: observation, action, observation, action, ... |
| Hidden state | Fixed-size summary of the past that an RNN carries forward |
| KV cache | Stored keys and values of past tokens, so they are not recomputed each step |
| Prefill / decode | Reading the prompt all at once / generating tokens one by one |

### 1. Why one frame is not enough

Reactive policies map the current observation $o_t$ to an action $a_t$. Two problems:

- **Memory.** One image cannot show speed, or that the road was icy earlier. Real robots are in a POMDP: the frame is a partial view of the state.
- **Jerky motion.** Independent per-step actions oscillate.

![Reactive policy: one observation in, one action out](../assets/diagrams/reactive-policy.png)

Fix: model the whole **sequence** of observations and actions.

### 2. The trajectory equation

$$
p_\pi(\tau) = \rho(s_0) \prod_{t=0}^{T-1} \pi(a_t \mid o_t)\, P(o_{t+1} \mid o_t, a_t)
$$

| Piece | Meaning |
|---|---|
| $\rho(s_0)$ | How the world starts (e.g. random object positions) |
| $\pi(a_t \mid o_t)$ | Policy: how likely is this action given what the robot sees |
| $P(o_{t+1} \mid o_t, a_t)$ | The world's reply to the action |

The product runs to $T-1$ because there are $T$ transitions but $T+1$ observations.

**Only $\pi$ depends on the policy parameters.** When you differentiate $\log p_\pi(\tau)$, $\rho$ and $P$ drop out, so you can train a policy without knowing the physics.

**Where it breaks.** Truthfully, a hidden state sits in the middle: physics moves it, $P(s_{t+1} \mid s_t, a_t)$, then a sensor reads it, $O(o_{t+1} \mid s_{t+1})$. The simple form is exact only if $o_t$ is a **sufficient statistic** of the state. Example: a gripper closes on a cube. The images and commands are identical, but the cube is heavy in one run and light in the other. The next frames differ and the camera cannot see mass, so no single $P(o_{t+1} \mid o_t, a_t)$ fits both. The fix is to condition on the full history $h_t$: $\pi(a_t \mid h_t)$. Papers still write the simple form as shorthand, usually with frame stacking or a wrist camera to make $o_t$ nearly sufficient.

### 3. Chain rule and RNNs

Any sequence splits into conditionals (this is autoregressive modeling):

$$
p(x_1, \dots, x_T) = \prod_{t=1}^{T} p(x_t \mid x_1, \dots, x_{t-1})
$$

An **RNN** models each conditional with a hidden state updated each step, $h_t = f(h_{t-1}, x_t)$. Problems:

1. **Long-range memory:** gradients pass back through every step and vanish or explode (LSTMs only slow this).
2. **Slow training:** step $t$ needs step $t-1$, so no parallelism.
3. **Bottleneck:** all history squeezed into one fixed-size vector.

![RNN unrolled over time](../assets/diagrams/rnn-unrolled.svg)

### 4. Attention

**Idea.** Every token looks at every other token in one hop and decides which matter. This fixes all three RNN problems: direct long-range links, parallel training, no single bottleneck vector.

![RNN chain vs attention direct access](../assets/diagrams/rnn-vs-attention.svg)

**Query / key / value.** Each token makes three vectors: a **query** $q$ (what I am looking for), a **key** $k$ (what I advertise), a **value** $v$ (what I hand over if chosen).

**The math.** Stack the $n$ token embeddings into $X \in \mathbb{R}^{n \times d_{\text{model}}}$ and project:

$$
Q = XW_Q,\qquad K = XW_K,\qquad V = XW_V
$$

$$
\boxed{\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}} + M\right)V}
$$

| Piece | Shape | What it does |
|---|---|---|
| $W_Q, W_K, W_V$ | $d_{\text{model}} \times d_k$ | Learned projections that create $q$, $k$, $v$ |
| $QK^\top$ | $n \times n$ | Entry $(i,j)$ = dot product of query $i$ with key $j$. How relevant token $j$ is to token $i$ |
| $\sqrt{d_k}$ | scalar | Dot products of $d_k$-dim vectors have variance $\propto d_k$. Without scaling, large scores saturate softmax and gradients vanish |
| $M$ | $n \times n$ | Mask. $0$ where allowed, $-\infty$ for future tokens in causal attention, so their weight becomes 0 |
| softmax | row-wise | Turns each row into positive weights summing to 1 |
| $\cdot V$ | $n \times d_v$ | Each output is the weighted average of all value vectors |

So it is a **soft dictionary**: a normal dictionary returns one entry, attention returns a blend of all entries weighted by key-query match. Everything is differentiable, so the model learns what to store in $q, k, v$ and where to look.

**Multi-head.** Run $h$ attentions in parallel, each with its own $W_Q, W_K, W_V$ and a smaller $d_k = d_{\text{model}}/h$, then concatenate and apply $W_O$. Different heads learn different relations.

**Worked example** (scores already scaled). Token "it" scores $[2, 1, 0]$ against ["robot", "picked", "spoon"]:

- $e^2, e^1, e^0 = 7.39, 2.72, 1$; total $11.11$ → weights $[0.67, 0.24, 0.09]$.
- Output $= 0.67\,v_{\text{robot}} + 0.24\,v_{\text{picked}} + 0.09\,v_{\text{spoon}}$. It mostly pulls in "robot".

![Attention worked example](../assets/diagrams/attention-example.svg)

**Positional encodings.** The dot product ignores order, so position must be injected.

| Type | Idea | Note |
|---|---|---|
| Absolute | Add a fixed vector per position | Fails beyond training length |
| Relative | Bias scores by token distance | Generalizes to longer sequences |
| RoPE | Rotate $q, k$ by position-proportional angle, so the dot product depends only on distance | Used in most modern LLMs |

### 5. The original transformer

- **Encoder:** *bidirectional* self-attention (full input is available).
- **Decoder:** *causal* self-attention (the mask $M$ above), so each token sees only itself and earlier tokens.
- **Cross-attention:** queries from the decoder, keys and values from the encoder: "which part of the source matters now?"

![Transformer encoder-decoder architecture](../assets/diagrams/transformer-architecture.svg)

**Teacher forcing.** In training, feed the true previous tokens and predict the next true token (cross-entropy). With the causal mask, one forward pass gives the loss at every position at once. An RNN needs one step per token.

### 6. The KV cache

During generation each new token attends to all earlier ones. Earlier keys and values never change, so compute them once and store them. Queries are used only at their own step, so they are not cached.

![KV cache growing during generation](../assets/diagrams/kv-cache-decode.svg)

$$
\text{cache size} = 2 \times n_{\text{layers}} \times n_{\text{kv heads}} \times d_{\text{head}} \times L \times B \times \text{bytes}
$$

($L$ = sequence length, $B$ = batch size, 2 = key + value.) Llama-3-8B, 16-bit (32 layers, 8 KV heads, $d_{\text{head}}=128$): **128 KB per token**, about 1 GB at 8k context, about 16 GB at 128k. The weights are about 16 GB, so batch 8 at 128k will not fit on an H100 from the cache alone.

Two different memory problems:

| | Attention matrix | KV cache |
|---|---|---|
| Hurts during | Training, prefill | Decode |
| Grows as | $L^2$ | $L$ |
| At $L$ = 8k | ~4 GB per layer per sequence | ~1 GB whole model |
| Needed later? | No, temporary by-product | Yes |

**FlashAttention** computes attention in small tiles in fast on-chip memory and never stores the full $n \times n$ matrix (memory $O(n)$, same answer). It fixes the matrix, not the cache, because the cache holds information later tokens need.

### 7. KV cache vs RNN hidden state

The real difference is **when the model decides what to keep**.

| | RNN hidden state | KV cache |
|---|---|---|
| Size | Fixed, $O(d)$ | Grows, $O(L \cdot d)$ |
| Past tokens | Blended into one summary | Stored separately, never overwritten |
| What to keep is decided | At write time, blind to future questions | At read time, by the current query |
| Access to old tokens | Through the bottleneck | Direct, one hop |
| Training | Sequential in $L$ | Parallel over $L$ |
| Cost per generated token | $O(d^2)$, constant | $O(L \cdot d)$, grows |

![RNN hidden state vs KV cache](../assets/diagrams/kv-cache-vs-rnn.svg)

**What the cache drops.** It stores two learned projections of each token ($W_K$, $W_V$), not the token itself, so what is dropped is fixed at training time. An RNN compresses *across time* (tokens compete for one slot); the cache compresses *within each token* and every token keeps its own slot. Many heads and layers give many views of each token, and deep-layer entries are contextualized by earlier tokens.

**For robots:** for short episodes it is a wash (frame stacking works). For long tasks that need a memory from minutes ago, keeping raw history and re-reading it wins, at linear memory cost.

### 8. Tokens, LLMs

- **Subword tokens** balance vocabulary size and sequence length (attention cost is quadratic in length). **BPE:** start from characters, repeatedly merge the most frequent adjacent pair until you hit the target vocabulary. Byte-level BPE can encode any input. Expect ~3-4x compression at a ~100k vocabulary.
- **LLMs** are decoder-only transformers trained on next-token prediction. Scale brought new abilities: zero-shot (GPT-2), in-context learning (GPT-3, 175B).
- **Bitter lesson (Sutton):** general methods that scale with compute beat handcrafted ones. Open question: what emerges when we scale robot data?

### 9. Vision transformers (ViT)

To feed images to a transformer, change only the tokenizer: cut the image into patches and treat each patch as a token.

![Vision Transformer pipeline](../assets/diagrams/vision-transformer.svg)

1. **Patchify.** Split the image into $P \times P$ patches (224×224 with $P=16$ gives 196 patches).
2. **Embed.** Flatten each patch ($16 \cdot 16 \cdot 3 = 768$ numbers) and apply one shared linear layer.
3. **Add position.** Prepend a learnable **[CLS]** token and add a learned position embedding to every token.
4. **Encode.** Standard transformer encoder with *bidirectional* attention (no mask).
5. **Use the output.** [CLS] feeds a classifier, or the patch tokens go on as image tokens for a VLM or VLA.

Cost grows with (number of patches)$^2$, so smaller patches mean more tokens and much more attention cost. CLIP's vision tower is a ViT.

### 10. Vision + language (VLMs)

Simply concatenating image and text tokens does not tell the model which words go with which region. Four ways to connect them:

| Approach | How | Trade-off |
|---|---|---|
| **CLIP** (two towers) | Separate image and text encoders trained contrastively so matching pairs land close together | Shared embedding space, but no LLM to reason with |
| **Early fusion** (LLaVA, PaliGemma) | Frozen ViT + small trainable connector; image tokens prepended to text; ordinary self-attention | Richest interaction; risks hurting the LLM. Most common in open source |
| **Late fusion** (Flamingo) | New cross-attention layers in the LLM: text queries look at visual keys and values. A gate starts at 0, so the model initially behaves exactly like the original LLM | Keeps LLM intact; less interaction |
| **Native multimodal** | One transformer trained from scratch on interleaved text, images, audio, video | No modality bias, most expensive |

### 11. Robot actions as tokens (VLAs)

Same recipe: tokenize the new modality, feed one transformer, scale. Inputs are language and image tokens; outputs are **action tokens**. Attention over history also helps the memory problem.

To discretize continuous actions (RT-2, OpenVLA):

1. Per action dimension, clip to the 1st-99th percentile and map to $[-1, 1]$ (min-max would let one outlier squash everything).
2. Split into 256 bins.
3. Reuse the 256 least-used LLM tokens as action tokens.
4. Train with next-token cross-entropy.

**Limit:** at high control frequency consecutive action tokens look nearly identical, so the model can score well by copying the previous one without learning the skill.

### 12. Action chunking

Predict the next $k$ actions as a chunk, run them, then query again. Actions are planned together, so motion is smoother.

![One-step policy vs action chunking vs temporal ensembling](../assets/diagrams/action-chunking.svg)

- Long chunks (e.g. 100) leave the robot blind while the chunk runs.
- **Temporal ensembling:** query every step, so each timestep gets several overlapping predictions, blended with exponentially decaying weights. Keeps smoothness and stays responsive.
- **ACT:** bimanual ALOHA at 50 Hz, chunks of 100 actions × 14 joints = 1,400 values per forward pass. A specialist policy with no LLM; handles precise tasks like battery insertion.

### Takeaway

Find the right representation, use a general scalable architecture, and let data and compute do the work: text, then images, audio, and now robot actions.

## Concept checks

1. A robot sees one camera frame. Name two things it cannot know from that frame alone.
2. Scores $[2, 1, 0]$ gave weights $[0.67, 0.24, 0.09]$. What are the weights if all three scores are equal?
3. Why divide by $\sqrt{d_k}$ in the attention equation?
4. What does the mask $M$ do, and why can a transformer compute every loss in one pass under teacher forcing while an RNN cannot?
5. Why do relative positional encodings handle longer sequences better than absolute ones?
6. How does a ViT turn an image into tokens, and why does halving the patch size hurt cost so much?
7. Compare early fusion, late fusion and native multimodal training. Why does Flamingo start its gate at zero?
8. Why does predicting a chunk give smoother motion, and what does temporal ensembling add?
9. In the trajectory equation, which terms vanish when you differentiate with respect to the policy parameters, and why does that matter?
10. Give an example where identical images and actions lead to different next images. What does it say about conditioning only on $o_t$?
11. Why are keys and values cached but queries not?
12. Name the two memory problems in attention. Which does FlashAttention fix, and why not the other?
13. An RNN and a KV cache both remember the past. When does each decide what to keep?

---

[← Generative Models](week-06-generative-models.md) · [Next: World Models →](week-08-world-models.md)