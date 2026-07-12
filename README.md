# Robotics Study Group

An 11-week, theory-first path from robot-learning fundamentals to modern robot foundation models. This repository contains the study group's own explanations, diagrams, equations, discussion prompts, and implementation milestones.

![Robot learning system loop](assets/diagrams/week-01-learning-loop.svg)

Each theory page is a standalone visual guide with original diagrams, key equations, implementation notes, failure modes, evaluation checks, paper prompts, and a build milestone. Start at [Week 1](curriculum/week-01-introduction.md) or jump directly to the topic you need below.

## What we will learn

- Formulate control and decision-making problems as MDPs.
- Build behavior cloning, DAgger, value-based, and policy-gradient agents.
- Understand generative policies, action transformers, and world models.
- Read modern VLA and generalist-policy papers critically.
- Finish with a small, reproducible robot-learning capstone.

## Weekly roadmap

| Week | Topic | Theory guide | Build milestone |
| ---: | --- | --- | --- |
| 1 | Introduction to Robot Learning | [Read theory](curriculum/week-01-introduction.md) | Define a robot task and evaluation contract |
| 2 | Robot Control and MDPs | [Read theory](curriculum/week-02-control-and-mdps.md) | PID/control baseline plus a tiny MDP solver |
| 3 | Imitation Learning | [Read theory](curriculum/week-03-imitation-learning.md) | Behavior cloning and DAgger comparison |
| 4 | Reinforcement Learning I | [Read theory](curriculum/week-04-reinforcement-learning-i.md) | Value iteration and DQN baseline |
| 5 | Reinforcement Learning II | [Read theory](curriculum/week-05-reinforcement-learning-ii.md) | PPO or SAC with a clean evaluation loop |
| 6 | Generative Models for Control | [Read theory](curriculum/week-06-generative-models.md) | Multimodal action-policy prototype |
| 7 | Sequence Models and Transformers | [Read theory](curriculum/week-07-sequence-modeling.md) | Train an action-sequence transformer |
| 8 | World Models | [Read theory](curriculum/week-08-world-models.md) | Learn and test a latent dynamics model |
| 9 | Generalist Robot Policies | [Read theory](curriculum/week-09-generalist-policies.md) | Design a multi-task policy/data interface |
| 10 | Embodied Reasoning and Test-time Scaling | [Read theory](curriculum/week-10-embodied-reasoning.md) | Add candidate generation and verification |
| 11 | Frontiers and Open Problems | [Read theory](curriculum/week-11-frontiers.md) | Present a reproducible capstone proposal |

The full reading list, track structure, and recommended session format live in the [curriculum guide](curriculum/README.md).

## How each session runs

1. **Before:** read the theory guide; one member reads each assigned paper.
2. **Concept check (30 min):** explain the week's central idea without slides.
3. **Paper discussion (30 min):** identify the claim, evidence, assumptions, and failure modes.
4. **Build sprint (50 min):** implement the week's smallest measurable milestone.
5. **Wrap-up (10 min):** record results, blockers, and the owner of the next action.

## Definition of done

Every implementation should include a pinned environment, one reproducible command, at least three random seeds where practical, a non-learning baseline, and a small results table. Report failures as carefully as successes.

## Existing resources

- [Vanilla Policy Gradient tutorial](Tutorials/VPG_tutorial.md)
- [Earlier reinforcement-learning notes](week1/week1.md)

## Contributing

Use the [contribution guide](CONTRIBUTING.md) and the [session template](curriculum/session-template.md). Keep notes original and cite sources.

## Attribution

This is an independent SRA VJTI study-group resource, not an official ETH Zurich course mirror. See [ATTRIBUTION.md](ATTRIBUTION.md) for source and reuse details.

## Conducted by

- [Alqama Shaikh](https://github.com/aPR0T0)
