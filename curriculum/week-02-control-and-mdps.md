# Week 02 — Robot Control and MDPs

## Outcomes

- Connect feedback control to sequential decision-making.
- Define an MDP and identify when the chosen state is not Markov.
- Implement a control baseline and a tabular planning baseline.

## Core notes

Classical feedback control chooses actions from the current error. A proportional controller reacts to present error; integral action corrects persistent bias; derivative action damps fast change. This is often the strongest first baseline for a low-level robot task.

An MDP is described by states, actions, transitions, rewards, and a discount or finite horizon. A policy induces trajectories; the return aggregates future rewards; value functions predict expected return. Bellman equations express a value as immediate reward plus the value of the next state. Dynamic programming repeatedly applies this structure through policy evaluation, policy iteration, or value iteration.

The Markov assumption is a modeling decision, not a property guaranteed by the environment. A single camera frame may hide velocity, contact state, or intent. Frame stacking, recurrence, state estimation, or belief-state methods can repair missing information.

Rewards are specifications and can be exploited. Keep the true evaluation metric outside the shaped training reward, test simple pathological policies, and log individual reward terms.

## Paper discussion

Use [random search for RL](https://arxiv.org/abs/1803.07055) and [Deep RL Doesn't Work Yet](https://www.alexirpan.com/2018/02/14/rl-hard.html) to ask: how strong must a baseline be before a learned controller is convincing?

## Build milestone

Implement a PID controller for one continuous task and value iteration for one tiny discrete MDP. Plot tracking error for the controller and verify the Bellman residual for the MDP solution.

## Primary material

- [Official slides](https://cvg.ethz.ch/lectures/Robot-Learning/lectures/lecture2_control_mdp.pdf)
- [Lecture recording](https://www.youtube.com/watch?v=5-Bb84eTTqQ)
- [Public control/MDP homework](https://github.com/mees-robot-learning-course/ethz-course-2026/tree/main/hw2_robot_control_mdps)
