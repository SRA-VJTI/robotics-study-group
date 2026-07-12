# Robotics Study Group

An 11-week, build-first path from robot-learning fundamentals to modern robot foundation models. The roadmap is adapted for the SRA VJTI study group from ETH Zurich's **Robot Learning: From Fundamentals to Foundation Models** course.

> [!IMPORTANT]
> The ETH lecture decks are access-controlled and are **not mirrored here**. Use the official slide links if you have legitimate access. This repository contains original study-group notes, discussion prompts, and implementation milestones.

## What we will learn

- Formulate control and decision-making problems as MDPs.
- Build behavior cloning, DAgger, value-based, and policy-gradient agents.
- Understand generative policies, action transformers, and world models.
- Read modern VLA and generalist-policy papers critically.
- Finish with a small, reproducible robot-learning capstone.

## Weekly roadmap

| Week | Topic | Study guide | Official material | Build milestone |
| ---: | --- | --- | --- | --- |
| 1 | Introduction to Robot Learning | [Notes](curriculum/week-01-introduction.md) | [Slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture1_intro.pdf) · [Recording](https://www.youtube.com/watch?v=X0k14u6pSxw) | Define a robot task and evaluation contract |
| 2 | Robot Control and MDPs | [Notes](curriculum/week-02-control-and-mdps.md) | [Slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture2_control_mdp.pdf) · [Recording](https://www.youtube.com/watch?v=5-Bb84eTTqQ) | PID/control baseline plus a tiny MDP solver |
| 3 | Imitation Learning | [Notes](curriculum/week-03-imitation-learning.md) | [Slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture3_imitation.pdf) · [Recording](https://youtu.be/Ef4R5s1LqoQ) | Behavior cloning and DAgger comparison |
| 4 | Reinforcement Learning I | [Notes](curriculum/week-04-reinforcement-learning-i.md) | [Slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture4_rl_I.pdf) · [Recording](https://youtu.be/90raNpc11tQ) | Value iteration and DQN baseline |
| 5 | Reinforcement Learning II | [Notes](curriculum/week-05-reinforcement-learning-ii.md) | [Slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture5_rl_II.pdf) · [Recording](https://youtu.be/AdTGz8YnnlE) | PPO or SAC with a clean evaluation loop |
| 6 | Generative Models for Control | [Notes](curriculum/week-06-generative-models.md) | [Slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture6_generative.pdf) · [Recording](https://youtu.be/qd6Ldsuu46I) | Multimodal action-policy prototype |
| 7 | Sequence Models and Transformers | [Notes](curriculum/week-07-sequence-modeling.md) | [Slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture7_sequence_modeling.pdf) · [Recording](https://youtu.be/imSTfMJjp7M) | Train an action-sequence transformer |
| 8 | World Models | [Notes](curriculum/week-08-world-models.md) | [Slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture8_world_models.pdf) · [Recording](https://youtu.be/cTTmUZlOF2s) | Learn and test a latent dynamics model |
| 9 | Generalist Robot Policies | [Notes](curriculum/week-09-generalist-policies.md) | [Slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture9_generalist_policies.pdf) · [Recording](https://youtu.be/dtofzDY9zuo) | Design a multi-task policy/data interface |
| 10 | Embodied Reasoning and Test-time Scaling | [Notes](curriculum/week-10-embodied-reasoning.md) | [Slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture10_reasoning.pdf) · [Recording](https://youtu.be/CxhrjQuGEuE) | Add candidate generation and verification |
| 11 | Frontiers and Open Problems | [Notes](curriculum/week-11-frontiers.md) | [Slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture11_frontiers.pdf) · [Recording](https://youtu.be/eL4lcy1KNzE) | Present a reproducible capstone proposal |

The full reading list and recommended session format live in the [curriculum guide](curriculum/README.md).

## How each session runs

1. **Before:** watch the lecture or skim the guide; one member reads each assigned paper.
2. **Concept check (30 min):** explain the week's central idea without slides.
3. **Paper discussion (30 min):** identify the claim, evidence, assumptions, and failure modes.
4. **Build sprint (50 min):** implement the week's smallest measurable milestone.
5. **Wrap-up (10 min):** record results, blockers, and the owner of the next action.

## Definition of done

Every implementation should include a pinned environment, one reproducible command, at least three random seeds where practical, a non-learning baseline, and a small results table. Report failures as carefully as successes.

## Existing resources

- [Vanilla Policy Gradient tutorial](Tutorials/VPG_tutorial.md)
- [Earlier reinforcement-learning notes](week1/week1.md)
- [Official ETH course repository](https://github.com/mees-robot-learning-course/ethz-course-2026) for publicly released exercises

## Contributing

Use the [contribution guide](CONTRIBUTING.md) and the [session template](curriculum/session-template.md). Keep notes original, cite sources, and do not upload access-controlled course files.

## Attribution

This is an independent SRA VJTI study-group resource, not an official ETH Zurich course mirror. See [ATTRIBUTION.md](ATTRIBUTION.md) for source and reuse details.

## Conducted by

- [Alqama Shaikh](https://github.com/aPR0T0)
