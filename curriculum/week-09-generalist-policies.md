# Week 09 — Generalist Robot Policies

## Outcomes

- Describe the data and interfaces needed by a multi-task robot policy.
- Separate semantic planning from embodiment-specific control.
- Evaluate transfer across tasks, environments, and robot bodies.

## Core notes

A generalist policy shares parameters across tasks and often across embodiments. Inputs may include images, language, proprioception, task identifiers, and history; outputs may be continuous controls, discrete action tokens, waypoints, or action chunks. Scale can create transfer, but only when data and interfaces make tasks mutually intelligible.

Language supplies a flexible task interface and connects robot data to pretrained vision-language representations. It does not by itself provide accurate geometry, contact dynamics, or calibration. Many systems therefore combine a broad semantic backbone with an embodiment-specific action head or adapter.

Dataset composition is as important as architecture. Record task definitions, success labels, control rates, camera conventions, action normalization, robot morphology, and data provenance. Large datasets can still be narrow if they repeat the same scene or demonstrator policy.

Generalization claims need explicit axes. Hold out object instances, layouts, instructions, tasks, environments, or embodiments separately. Compare a shared model with per-task specialists under the same data and compute budget. Track negative transfer, not just mean success.

## Paper discussion

Use [language-conditioned imitation](https://arxiv.org/abs/2005.07648) and [Gato](https://arxiv.org/abs/2205.06175) to compare task conditioning, action representation, and the evidence offered for generality.

## Build milestone

Design a common schema for two tasks or embodiments. Train a shared conditioned policy and two specialists. Report per-task success, parameter count, data volume, and any negative transfer.

## Primary material

- [Official slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture9_generalist_policies.pdf)
- [Lecture recording](https://youtu.be/dtofzDY9zuo)
