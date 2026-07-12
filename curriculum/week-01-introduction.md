# Week 01 — Introduction to Robot Learning

## Outcomes

- Distinguish model-based control, imitation learning, reinforcement learning, and generalist-policy training.
- Write an unambiguous robot-learning task contract.
- Separate training objectives from evaluation metrics.

## Core notes

Robot learning sits at the intersection of perception, decision-making, and control. A policy maps the information available to the robot—state, observations, language, history, or all four—to an action or action sequence. Learning is useful when writing that mapping by hand is brittle, when demonstrations contain valuable behavior, or when interaction can improve a policy.

The method should follow the supervision available:

- **Control/model-based planning:** dynamics and objectives are known well enough to optimize directly.
- **Imitation learning:** an expert provides observation-action examples.
- **Reinforcement learning:** interaction provides rewards rather than correct actions.
- **Offline or foundation-model training:** heterogeneous logged data provides scale, but creates distribution and embodiment mismatches.

Before choosing an algorithm, define the task. Specify observations, actions, control frequency, horizon, reset rules, success criteria, safety limits, and the training/evaluation distributions. “It looks good” is not a metric. Report success rate, time-to-success, violations, and resource cost separately.

## Concept checks

1. A robot has thousands of demonstrations but cannot collect new data. Which learning regimes remain feasible, and what distribution-shift risk dominates?
2. Why can a lower training loss produce a worse closed-loop policy?

## Build milestone

Create a one-page task card for a simulated reach, push, or pick task. Include a scripted/random baseline, three seeds, a success metric, a safety metric, and one out-of-distribution split. No learning is required this week.

## Primary material

- [Official slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture1_intro.pdf)
- [Lecture recording](https://www.youtube.com/watch?v=X0k14u6pSxw)
- [Official course exercises](https://github.com/mees-robot-learning-course/ethz-course-2026)
