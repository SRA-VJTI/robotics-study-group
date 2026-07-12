# Week 07 — Sequence Modeling and Transformers

## Outcomes

- Represent trajectories as sequences for causal prediction.
- Explain attention, positional information, and causal masking in a robot policy.
- Choose a tokenization and action-chunking scheme.

## Core notes

Sequence models replace a hand-designed fixed state with a learned function of history. A transformer embeds tokens, mixes information through self-attention, and predicts under a causal mask so future tokens cannot leak into the current decision. Robot tokens may represent images, proprioception, language, rewards, returns, or discretized/continuous actions.

Decision Transformer casts offline RL as conditional sequence modeling: predict actions from past context and a desired return. This avoids an explicit Bellman objective, but performance depends on dataset coverage and whether the conditioning signal identifies achievable behavior. It does not automatically solve out-of-distribution action selection.

Action chunking predicts several future controls per query. It can model temporally coherent motions and shorten the effective horizon, which is valuable for high-frequency manipulation. The tradeoff is responsiveness. Temporal ensembling or receding-horizon execution can combine overlapping chunks.

Architecture choices must preserve causality and modality identity. Record token order, attention mask, context length, image encoder, action representation, normalization, and inference rate. A silent mask error can produce excellent offline metrics and an unusable deployed policy.

## Paper discussion

Contrast return-conditioned control in [Decision Transformer](https://arxiv.org/abs/2106.01345) with action chunking in [ALOHA](https://arxiv.org/abs/2304.13705).

## Build milestone

Train a small causal transformer to predict action sequences from state history. Compare single-step actions with short chunks at equal parameter count. Measure success, latency, and recovery after a mid-episode perturbation.

## Primary material

- [Official slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture7_sequence_modeling.pdf)
- [Lecture recording](https://youtu.be/imSTfMJjp7M)
