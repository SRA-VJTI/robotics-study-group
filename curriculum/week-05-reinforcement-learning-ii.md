# Week 05 — Reinforcement Learning II

## Outcomes

- Explain the policy-gradient estimator and the purpose of a baseline.
- Contrast on-policy PPO with off-policy SAC.
- Identify when offline RL or human-in-the-loop correction is appropriate.

## Core notes

Policy-gradient methods optimize a parameterized policy directly. The score-function estimator weights the gradient of an action's log probability by its return. Subtracting a baseline leaves the estimator unbiased while reducing variance; actor-critic methods learn a value function for this role.

PPO is an on-policy method that limits how far the policy moves on a batch of recent experience, usually through a clipped probability-ratio objective. It is comparatively straightforward but discards data quickly. SAC is off-policy: it reuses replay data, learns critics, and adds entropy to encourage diverse behavior. It is often attractive for continuous control but is sensitive to critic errors and data quality.

Offline RL learns from a fixed dataset. The main danger is evaluating actions not supported by that dataset: an inaccurate critic may assign them unrealistically high value. Conservative objectives, behavior constraints, uncertainty, and careful dataset coverage help. Human intervention can supply corrective data near failures, but the intervention policy and safety boundary become part of the system.

## Concept checks

1. Why does reusing an old batch violate the simplest on-policy gradient derivation?
2. When can entropy improve robustness, and when can it harm a precision task?

## Build milestone

Train PPO or SAC on the same task contract used earlier. Compare it with the non-learning controller and behavior-cloning policy using equal evaluation episodes. Report environment steps and wall-clock time.

## Primary material

- [Official slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture5_rl_II.pdf)
- [Lecture recording](https://youtu.be/AdTGz8YnnlE)
- [SRA VPG tutorial](../Tutorials/VPG_tutorial.md)
