# Curriculum guide

## Goal

Move from the mechanics of robot learning to the ability to design, implement, and evaluate a small modern system. The sequence is cumulative: later sessions reuse the same task contract, dataset format, and evaluation habits established in weeks 1–3.

## What is on each lecture page

- An original concept diagram designed for this study group
- A compact method/component comparison
- Key equations with implementation interpretation
- Common failure modes and diagnostics
- A measurable build milestone
- Primary lecture, paper, recording, and homework links where available

These pages are independent study companions. They do not reproduce or replace the access-controlled ETH lecture decks.

## Tracks

- **Core:** read the guide, join the discussion, and complete the minimal build milestone.
- **Builder:** reproduce a result and submit code plus a short experiment report.
- **Presenter:** lead one paper discussion using claim → evidence → limitation → next experiment.

## Recommended common task

Use one lightweight task for several weeks so algorithm differences remain interpretable. Good choices are a simulated reaching task, planar pushing, or a small grid-world for the earliest sessions. Define:

- observation and action spaces;
- success and safety metrics;
- reset and termination rules;
- demonstration and evaluation distributions;
- compute budget and random seeds.

## Reading list by week

| Week | Suggested discussion papers |
| ---: | --- |
| 1 | No required paper; agree on task and evaluation conventions. |
| 2 | [Simple random search provides a competitive approach to RL](https://arxiv.org/abs/1803.07055); [Deep RL Doesn't Work Yet](https://www.alexirpan.com/2018/02/14/rl-hard.html); [Curiosity-driven Exploration](https://arxiv.org/abs/1705.05363) |
| 3 | [Causal Confusion in Imitation Learning](https://arxiv.org/abs/1905.11979); [Representation Learning for Visual Imitation](https://arxiv.org/abs/2112.01511); [Transporter Networks](https://arxiv.org/abs/2010.14406) |
| 4 | [Evolution Strategies as a Scalable Alternative to RL](https://arxiv.org/abs/1703.03864); [Learning Synergies Between Pushing and Grasping](https://arxiv.org/abs/1803.09956); [Human-in-the-loop RL for Dexterous Manipulation](https://arxiv.org/abs/2410.21845) |
| 5 | [End-to-End Training of Deep Visuomotor Policies](https://arxiv.org/abs/1504.00702); [Eureka](https://arxiv.org/abs/2310.12931); [Latent Plans for Task-Agnostic Offline RL](https://arxiv.org/abs/2209.08959) |
| 6 | [Diffuser](https://arxiv.org/abs/2205.09991); [Implicit Behavioral Cloning](https://arxiv.org/abs/2109.00137); [Steering Your Diffusion Policy with Latent Space RL](https://arxiv.org/abs/2506.15799) |
| 7 | [Decision Transformer](https://arxiv.org/abs/2106.01345); [ALOHA](https://arxiv.org/abs/2304.13705); [Humanoid Locomotion as Next Token Prediction](https://arxiv.org/abs/2402.19469) |
| 8 | [Universal Policies via Text-Guided Video Generation](https://arxiv.org/abs/2302.00111); [Training Agents Inside Scalable World Models](https://arxiv.org/abs/2509.24527); [World Action Models are Zero-shot Policies](https://dreamzero0.github.io/DreamZero.pdf) |
| 9 | [Language Conditioned Imitation Learning](https://arxiv.org/abs/2005.07648); [Gato](https://arxiv.org/abs/2205.06175); [π*0.6](https://arxiv.org/abs/2511.14759) |
| 10 | [In-Context Imitation Learning](https://arxiv.org/abs/2408.15980); [Voyager](https://arxiv.org/abs/2305.16291); [Training Strategies for Efficient Embodied Reasoning](https://arxiv.org/abs/2505.08243) |
| 11 | [A Path Towards Autonomous Machine Intelligence](https://openreview.net/forum?id=BZ5a1r-kVsf); [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html); [Intelligence without Representation](https://people.csail.mit.edu/brooks/papers/representation.pdf) |

The [official course page](https://cvg.ethz.ch/lectures/Robot-Learning/) is the source of truth for its schedule and links.

## Capstone checkpoint

By week 11, each team should have a one-page proposal containing a falsifiable question, baseline, intervention, dataset/task, primary metric, compute estimate, ablations, and a stop condition. Prefer a small clean result over an unbounded platform build.
