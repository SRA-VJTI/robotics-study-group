# Robotics Study Group

An 11-week, build-first path from robot-learning fundamentals to modern robot foundation models. The roadmap is adapted for the SRA VJTI study group from ETH Zurich's **Robot Learning: From Fundamentals to Foundation Models** course.

> [!IMPORTANT]
> All 515 slides from the 11 ETH lecture decks are rendered locally under redistribution permission confirmed for this repository. The deck renders retain their original copyright and are not covered by this repository's MIT license. No deck password is stored here.

![Robot learning system loop](assets/diagrams/week-01-learning-loop.svg)

Each lecture page contains the complete source deck plus original study-group diagrams, key equations, implementation notes, failure modes, evaluation checks, paper prompts, and a build milestone. Start at [Week 1](curriculum/week-01-introduction.md) or jump directly to the topic you need below.

## What we will learn

- Formulate control and decision-making problems as MDPs.
- Build behavior cloning, DAgger, value-based, and policy-gradient agents.
- Understand generative policies, action transformers, and world models.
- Read modern VLA and generalist-policy papers critically.
- Finish with a small, reproducible robot-learning capstone.

## Weekly roadmap

| Week | Topic | Complete lecture | Slides | Build milestone |
| ---: | --- | --- | ---: | --- |
| 1 | Introduction to Robot Learning | [Open lecture](curriculum/week-01-introduction.md) | 44 | Define a robot task and evaluation contract |
| 2 | Robot Control and MDPs | [Open lecture](curriculum/week-02-control-and-mdps.md) | 46 | PID/control baseline plus a tiny MDP solver |
| 3 | Imitation Learning | [Open lecture](curriculum/week-03-imitation-learning.md) | 45 | Behavior cloning and DAgger comparison |
| 4 | Reinforcement Learning I | [Open lecture](curriculum/week-04-reinforcement-learning-i.md) | 45 | Value iteration and DQN baseline |
| 5 | Reinforcement Learning II | [Open lecture](curriculum/week-05-reinforcement-learning-ii.md) | 36 | PPO or SAC with a clean evaluation loop |
| 6 | Generative Models for Control | [Open lecture](curriculum/week-06-generative-models.md) | 39 | Multimodal action-policy prototype |
| 7 | Sequence Models and Transformers | [Open lecture](curriculum/week-07-sequence-modeling.md) | 39 | Train an action-sequence transformer |
| 8 | World Models | [Open lecture](curriculum/week-08-world-models.md) | 55 | Learn and test a latent dynamics model |
| 9 | Generalist Robot Policies | [Open lecture](curriculum/week-09-generalist-policies.md) | 59 | Design a multi-task policy/data interface |
| 10 | Embodied Reasoning and Test-time Scaling | [Open lecture](curriculum/week-10-embodied-reasoning.md) | 57 | Add candidate generation and verification |
| 11 | Frontiers and Open Problems | [Open lecture](curriculum/week-11-frontiers.md) | 50 | Present a reproducible capstone proposal |

The full reading list, track structure, and recommended session format live in the [curriculum guide](curriculum/README.md).

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

Use the [contribution guide](CONTRIBUTING.md) and the [session template](curriculum/session-template.md). Keep notes original, cite sources, and never commit credentials or additional restricted material without documented permission.

## Attribution

This is an independent SRA VJTI study-group resource, not the official ETH Zurich course website. See [ATTRIBUTION.md](ATTRIBUTION.md) for source and reuse details.

## Conducted by

- [Alqama Shaikh](https://github.com/aPR0T0)
