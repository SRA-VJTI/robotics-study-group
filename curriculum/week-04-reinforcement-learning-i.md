# Week 04 — Reinforcement Learning I

## Outcomes

- Derive the role of bootstrapping in value-based RL.
- Explain replay buffers, target networks, and exploration in DQN.
- Build an evaluation protocol that does not hide RL instability.

## Core notes

Reinforcement learning optimizes expected return from interaction. Monte Carlo targets use complete sampled returns and can have high variance. Temporal-difference methods bootstrap from an estimate of the next state's value, reducing target horizon while introducing bias and moving-target instability.

Q-learning learns the value of taking an action and then acting optimally. With function approximation, DQN stabilizes training using replayed transitions and a slower target network. Replay improves data reuse and weakens temporal correlation; the target network stops every update from immediately changing its own target.

The central practical loop is: collect transitions, store them, sample a batch, construct a Bellman target, minimize prediction error, and periodically update the target network. Exploration must be stated explicitly; epsilon-greedy is a baseline, not a universal solution.

RL results are distributions. Report learning curves, final performance, seed count, environment steps, wall-clock cost, and evaluation without exploration noise. Compare against random, scripted, and classical-control baselines where applicable.

## Paper discussion

Compare gradient-free [evolution strategies](https://arxiv.org/abs/1703.03864) with value-based learning. Which method is easier to parallelize, and which uses each transition more efficiently?

## Build milestone

Solve a tabular task with value iteration, then train DQN on a small discrete-control task. Add an ablation removing either replay or the target network and explain the resulting curve.

## Primary material

- [Official slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture4_rl_I.pdf)
- [Lecture recording](https://youtu.be/90raNpc11tQ)
- [Public reinforcement-learning homework](https://github.com/mees-robot-learning-course/ethz-course-2026/tree/main/hw4_reinforcement_learning)
