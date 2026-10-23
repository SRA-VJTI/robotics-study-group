# Robotics Study Group

A build-first path from robot-learning fundamentals to modern robot foundation models, adapted for the SRA VJTI study group from ETH Zurich's **Robot Learning: From Fundamentals to Foundation Models** course.

![Robot learning system loop](assets/diagrams/week-01-learning-loop.svg)

Each topic gets a written notes page with original study-group diagrams, key equations, implementation notes, and failure modes. Notes are written up as we cover each topic — [Imitation Learning](curriculum/week-03-imitation-learning.md) is the current worked example of the format.

## What we will learn

- Formulate control and decision-making problems as MDPs.
- Build behavior cloning, DAgger, value-based, and policy-gradient agents.
- Understand generative policies, action transformers, and world models.
- Read modern VLA and generalist-policy papers critically.
- Finish with a small, reproducible robot-learning capstone.

## Topics

| Topic | Notes | Build milestone |
| --- | --- | --- |
| Introduction to Robot Learning | [Open](curriculum/week-01-introduction.md) | Define a robot task and evaluation contract |
| Robot Control and MDPs | [Open](curriculum/week-02-control-and-mdps.md) | PID/control baseline plus a tiny MDP solver |
| Imitation Learning | [Open](curriculum/week-03-imitation-learning.md) | Behavior cloning and DAgger comparison |
| Reinforcement Learning I | [Open](curriculum/week-04-reinforcement-learning-i.md) | Value iteration and DQN baseline |
| Reinforcement Learning II | [Open](curriculum/week-05-reinforcement-learning-ii.md) | PPO or SAC with a clean evaluation loop |
| Generative Models for Control | [Open](curriculum/week-06-generative-models.md) | Multimodal action-policy prototype |
| Sequence Models and Transformers | [Open](curriculum/week-07-sequence-modeling.md) | Train an action-sequence transformer |
| World Models | [Open](curriculum/week-08-world-models.md) | Learn and test a latent dynamics model |
| Generalist Robot Policies | [Open](curriculum/week-09-generalist-policies.md) | Design a multi-task policy/data interface |
| Embodied Reasoning and Test-time Scaling | [Open](curriculum/week-10-embodied-reasoning.md) | Add candidate generation and verification |
| Frontiers and Open Problems | [Open](curriculum/week-11-frontiers.md) | Present a reproducible capstone proposal |

The full reading list, track structure, and recommended session format live in the [curriculum guide](curriculum/README.md).

## How each session runs

1. **Before:** skim the notes; one member reads each assigned paper.
2. **Concept check (30 min):** explain the topic's central idea from memory.
3. **Paper discussion (30 min):** identify the claim, evidence, assumptions, and failure modes.
4. **Build sprint (50 min):** implement the topic's smallest measurable milestone.
5. **Wrap-up (10 min):** record results, blockers, and the owner of the next action.

## Definition of done

Every implementation should include a pinned environment, one reproducible command, at least three random seeds where practical, a non-learning baseline, and a small results table. Report failures as carefully as successes.

## Existing resources

- [Vanilla Policy Gradient tutorial](Tutorials/VPG_tutorial.md)
- [Earlier reinforcement-learning notes](week1/week1.md)
- [Official ETH course repository](https://github.com/mees-robot-learning-course/ethz-course-2026) for publicly released exercises

## Contributing

Use the [contribution guide](CONTRIBUTING.md) and the [session template](curriculum/session-template.md). Keep notes original, cite sources, and never commit credentials or additional restricted material without documented permission.

## Attribution

This is an independent SRA VJTI study-group resource, not the official ETH Zurich course website. See [ATTRIBUTION.md](ATTRIBUTION.md) for source and reuse details.

## Conducted by

- [Alqama Shaikh](https://github.com/aPR0T0)
