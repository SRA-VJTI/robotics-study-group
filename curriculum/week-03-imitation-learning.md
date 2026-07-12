# Week 03 — Imitation Learning

## Outcomes

- Explain why supervised accuracy is insufficient for closed-loop imitation.
- Compare behavior cloning, DAgger, and sequence/action-chunking policies.
- Diagnose covariate shift and causal confusion.

## Core notes

Behavior cloning fits a policy to expert observation-action pairs. It is simple and stable, but the learned policy changes which states it visits. Small errors move the robot away from the demonstration distribution; unfamiliar states cause more errors, and mistakes compound over the horizon.

DAgger addresses this by rolling out the learner, querying the expert on states the learner actually visits, aggregating those labels, and retraining. It trades expert effort for better coverage of recovery states. When online relabeling is impossible, dataset diversity, perturbation/recovery demonstrations, conservative deployment, and uncertainty-aware fallback become important.

Robotic behavior is often multimodal: several actions can be correct in the same observation. A mean-squared-error policy may average them into an invalid action. Discrete bins, mixture models, energy-based models, diffusion policies, or action chunks can represent alternatives. Chunking also reduces the effective decision horizon, but long chunks reduce feedback frequency.

Causal confusion appears when a policy uses a correlate that predicts expert actions in the dataset but does not cause success. Evaluate under interventions: change backgrounds, object arrangements, demonstrator artifacts, or history while holding the task fixed.

## Paper discussion

Contrast the diagnosis in [Causal Confusion in Imitation Learning](https://arxiv.org/abs/1905.11979) with the empirical case for pretrained visual representations in [Pari et al.](https://arxiv.org/abs/2112.01511).

## Build milestone

Collect or synthesize demonstrations, train behavior cloning, then introduce initial-state noise. Add either DAgger or recovery data and compare closed-loop success—not just validation loss—over three seeds.

## Primary material

- [Official slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture3_imitation.pdf)
- [Lecture recording](https://youtu.be/Ef4R5s1LqoQ)
- [Public imitation-learning homework](https://github.com/mees-robot-learning-course/ethz-course-2026/tree/main/hw3_imitation_learning)
