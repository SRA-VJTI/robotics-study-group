# Week 08 — World Models

## Outcomes

- Separate representation, dynamics, reward, and policy components.
- Explain latent rollout and model-predictive control.
- Measure when a learned model is useful for decisions rather than pixels.

## Core notes

A world model predicts how relevant aspects of the environment evolve under actions. A typical system encodes observations into a latent state, predicts future latents conditioned on actions, and optionally predicts rewards, terminations, or observations. A policy can then learn inside imagined rollouts or choose actions by planning through the model.

The model need not reconstruct every pixel. Decision-relevant representations should preserve objects, geometry, contact, controllability, and uncertainty. Pixel quality can be visually impressive while action consequences are wrong. Evaluate multi-step state or reward prediction, planning performance, and calibration under interventions.

Model-predictive control samples or optimizes candidate action sequences, scores predicted outcomes, executes a short prefix, and replans from the next real observation. Frequent replanning limits accumulated model error. The remaining failure modes include compounding rollout error, exploitation of model mistakes, partial observability, and uncertainty far from the training distribution.

Video generation can provide a useful behavioral prior or goal-conditioned prediction, but converting visual futures into executable, embodiment-specific actions remains a central interface problem.

## Paper discussion

Ask whether [text-guided video policies](https://arxiv.org/abs/2302.00111) and [World Action Models](https://dreamzero0.github.io/DreamZero.pdf) are best understood as planners, policies, or representation learners—and what evidence would distinguish those roles.

## Build milestone

Learn a one-step dynamics model in a compact state space, roll it out for increasing horizons, and plot prediction error. Use it in a short-horizon planner and compare task return with random shooting in the real simulator.

## Primary material

- [Official slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture8_world_models.pdf)
- [Lecture recording](https://youtu.be/cTTmUZlOF2s)
