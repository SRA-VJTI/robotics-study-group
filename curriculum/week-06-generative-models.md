# Week 06 — Generative Models for Control

## Outcomes

- Explain why robot action distributions are often multimodal.
- Compare explicit, implicit, and diffusion policy objectives.
- Evaluate generated action sequences in closed loop.

## Core notes

A deterministic regressor assumes one preferred action for each input. Robotics often violates that assumption: an object can be grasped from several sides, an obstacle can be passed on either side, and demonstrations can contain distinct styles. Averaging modes can create an action no expert would take.

Generative policies model a distribution over actions or trajectories. Energy-based policies learn a compatibility score and select low-energy actions through optimization or sampling. Diffusion policies learn to denoise a corrupted action sequence conditioned on observations, turning iterative denoising into conditional trajectory generation. Both can represent multiple valid solutions, but inference is more expensive than one forward pass.

Generating an action chunk provides temporal coherence and reduces the number of policy queries. Receding-horizon execution restores feedback: predict a chunk, execute only its first portion, observe again, and replan. Important design choices include action horizon, observation history, normalization, noise schedule, sampler steps, and the fraction of each chunk executed.

Evaluate more than imitation loss. Measure task success, inference latency, smoothness, constraint violations, robustness to observation changes, and diversity only when diversity is actually useful.

## Paper discussion

Compare planning-as-denoising in [Diffuser](https://arxiv.org/abs/2205.09991) with action selection in [Implicit Behavioral Cloning](https://arxiv.org/abs/2109.00137).

## Build milestone

Construct a toy two-mode action dataset. Compare mean regression with a mixture, energy-based, or diffusion model. Visualize whether generated actions cover both valid modes and whether closed-loop execution remains stable.

## Primary material

- [Official slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture6_generative.pdf)
- [Lecture recording](https://youtu.be/qd6Ldsuu46I)
