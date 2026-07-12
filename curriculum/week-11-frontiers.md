# Week 11 — Frontiers and Open Problems

## Outcomes

- Turn a broad robotics idea into a falsifiable research question.
- Locate bottlenecks in data, objectives, embodiment, evaluation, and safety.
- Design a capstone with a credible baseline and stop condition.

## Core notes

Modern robot learning still faces a gap between benchmark competence and dependable autonomy. Important bottlenecks include scarce high-quality interaction data, inconsistent embodiment interfaces, long-tail failures, partial observability, weak causal understanding, unsafe exploration, and evaluation that is too small or too forgiving.

Three useful research instincts pull in different directions:

- The **Bitter Lesson** favors scalable learning and computation over hand-built domain structure.
- **Intelligence without Representation** emphasizes situated interaction and cautions against unnecessary internal abstractions.
- World-model and joint-embedding proposals argue that predictive internal state is necessary for planning and abstraction.

Treat these as competing design hypotheses, not slogans. Ask what information, compute, and environment each approach assumes; what measurable capability it predicts; and what experiment could prove it wrong.

A good capstone is narrow. State one intervention and one primary metric. Freeze the task, data budget, compute budget, and baseline before running. Include an ablation, expected failure mode, and stop condition. A negative result with a trustworthy protocol is more useful than an unmeasured demo.

## Paper discussion

Triangulate [A Path Towards Autonomous Machine Intelligence](https://openreview.net/forum?id=BZ5a1r-kVsf), [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), and [Intelligence without Representation](https://people.csail.mit.edu/brooks/papers/representation.pdf). Which claims conflict, and which operate at different layers?

## Build milestone

Present a one-page proposal: question, hypothesis, baseline, intervention, task/data, primary metric, seed/compute budget, two ablations, safety constraints, and stop condition. Another team must be able to reproduce the plan without asking you questions.

## Primary material

- [Official slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture11_frontiers.pdf)
- [Lecture recording](https://youtu.be/eL4lcy1KNzE)
