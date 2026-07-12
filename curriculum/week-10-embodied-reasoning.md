# Week 10 — Embodied Reasoning and Test-time Scaling

## Outcomes

- Identify tasks that benefit from extra inference-time computation.
- Design candidate generation, verification, and replanning loops.
- Distinguish verbal plausibility from grounded task progress.

## Core notes

Some robot tasks require more than a single reactive policy pass: long-horizon instructions, tool choice, recovery, spatial constraints, or unfamiliar combinations. Test-time scaling spends additional computation to sample plans, search a tree, critique candidates, use tools, simulate outcomes, or replan after new observations.

The useful pattern is **propose → ground → verify → execute → observe → replan**. A language model may propose subgoals, but grounded modules must connect them to visible objects, reachable poses, controller capabilities, and safety constraints. Verification can use a value model, learned world model, geometric checker, simulator, or explicit predicate tests.

More inference is not automatically better. Candidate samples may be correlated, verifiers may reward polished explanations instead of feasible actions, and latency may exceed the control budget. Compare against an equal-latency reactive baseline and report accuracy or success as a function of samples, search depth, and wall-clock time.

In-context imitation provides another route: condition on example trajectories and predict the next action without updating weights. The key test is whether the policy recombines task structure or merely matches surface similarity.

## Paper discussion

Compare embodied learning from examples in [In-Context Imitation Learning](https://arxiv.org/abs/2408.15980) with iterative skill acquisition in [Voyager](https://arxiv.org/abs/2305.16291).

## Build milestone

Add candidate generation and a simple verifier to a multi-step task. Sweep the number of candidates and plot success versus latency. Include at least one adversarial case where the verifier selects a bad plan.

## Primary material

- [Official slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture10_reasoning.pdf)
- [Lecture recording](https://youtu.be/CxhrjQuGEuE)
