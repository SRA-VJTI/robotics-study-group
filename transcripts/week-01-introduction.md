# Week 01 - Introduction to Robot Learning: OCR transcript

[← Course home](../README.md) · **Default OCR view** · [Open optional slide gallery →](../curriculum/week-01-introduction.md)

> This is an automated OCR transcript generated from the locally rendered slide images. Use the image as the source of truth for equations, diagrams, citations, and small text.

## Slide 1

![Introduction to Robot Learning - slide 1](../assets/lectures/week-01/slide-1.jpg)

```text
Robot Learning: From Fundamentals to
Foundation Models

Lecture 1: Introduction to Robot Learning

Oier Mees BE Microsoft

16.02.2026
```

## Slide 2

![Introduction to Robot Learning - slide 2](../assets/lectures/week-01/slide-2.jpg)

```text
About Me

From Basque Country, Spain PhD in Freiburg, Germany _-PostDoc in Berkeley, USA Research at Microsoft

sy
po ee BERKELEY
```

## Slide 3

![Introduction to Robot Learning - slide 3](../assets/lectures/week-01/slide-3.jpg)

```text
Course Staff

Instructor: Oier Mees
Lead Research Scientist @ Microsoft Zurich
Email: oier. mees@inf.ethz.ch
```

## Slide 4

![Introduction to Robot Learning - slide 4](../assets/lectures/week-01/slide-4.jpg)

```text
Course Staff: TAs

Alexey Gavryushin Jonas Pai Liam Achenbach Nicola Irmiger
alexey.gavryushin@inf.ethz.ch jonpai@student.ethz.ch jonpai@student.ethz.ch nirmiger@ethz.ch

Tianxu An Simon Sukup Nicole Damblon Zador Pataki
tianan@ethz.ch ssukup @student.ethz.ch ndamblon@ethz.ch patakiz@ethz.ch
```

## Slide 5

![Introduction to Robot Learning - slide 5](../assets/lectures/week-01/slide-5.jpg)

```text
Course Staff: TAs

Carl Brander
cbrander@student.ethz.ch

Several open TA positions:
This could be you!
```

## Slide 6

![Introduction to Robot Learning - slide 6](../assets/lectures/week-01/slide-6.jpg)

```text
The Plan for Today

=" Course Goals & Logistics
« Why study Robot Learning?

Robot Learning

Oiler Mees
```

## Slide 7

![Introduction to Robot Learning - slide 7](../assets/lectures/week-01/slide-7.jpg)

```text
Course Goal

« Mastery of Fundamentals: Imitation, Reinforcement and
Policy Learning

« Practical Skills: Hands-on simulation and real-robot policy
deployment

« Frontier Models: Exploration of Foundation Models for
robotics

«" Systems Design: Scalable pipelines for perception,
control and reasoning
```

## Slide 8

![Introduction to Robot Learning - slide 8](../assets/lectures/week-01/slide-8.jpg)

```text
Course Goal: Inspire you!

4 Classy
regions

image proposals (-2k) CNN feat

Object Detection: R-CNN...

Robotics
eo OB OTIES

ChatGPT Moment
----_-_---

ChatGPT for Robotics?
------

you

Images Language

Transformer

Vision-Language Models,
Generative Models...
```

## Slide 9

![Introduction to Robot Learning - slide 9](../assets/lectures/week-01/slide-9.jpg)

```text
Course Structure

Website: https://cvg.ethz.ch/lectures/Robot-Learning
Mondays 16:15-17:45 :

=" Lecture 45 min + 45 min Paper Discussion

= Guest lectures throughout course
Thursdays 10:15-12:00

« TA Led Practice Sessions

Individual Homework: 4x assignments
Group Projects on real SO-101 robots
```

## Slide 10

![Introduction to Robot Learning - slide 10](../assets/lectures/week-01/slide-10.jpg)

```text
Paper Discussion

= 3x papers per lecture, available at project course
= 15 minutes per paper, groups of 4 students
= Group A presents & defends paper, Group B criticizes it

Lecture Tentative Schedule

Enter paper groups here:

OE eal |

https://docs.google.com/spreadsheets/d/1YSJAvOj4riU
wgBXzQIsAgiAGjVIJ30DI4TtdlcgJdB4/
```

## Slide 11

![Introduction to Robot Learning - slide 11](../assets/lectures/week-01/slide-11.jpg)

```text
Individual Homework

Assignments: https://github.com/mees-robot-learning-
course/ethz-course-2026

Submission: Gradescope

HW1: Pytorch & Numpy Tutorial 16.02-26.02
HW2: Robot Control & MDPs 23.02-05.03
HWs3: Imitation Learning 02.03-16.03

HW4: Reinforcement Learning 16.03-30.03

10
```

## Slide 12

![Introduction to Robot Learning - slide 12](../assets/lectures/week-01/slide-12.jpg)

```text
Homework Advice

=» Neural networks take some time to train!
= We try to make the homeworks fast to train

f(y = Me. waiting for my ne neural
"network to finishtraining

Don’t start the night before the deadline working on the
assignment!

11
```

## Slide 13

![Introduction to Robot Learning - slide 13](../assets/lectures/week-01/slide-13.jpg)

```text
Course Grading

= Paper Presentation & Discussion (Group): 20 %
= Practical Homework (Coding Assignments): 40 %
« Final Project (Group): 40 %

COURSE GRADING FORECAST

Paper Presentation Practical Homework Final Project
(20%) (40%) (40%)

12,
```

## Slide 14

![Introduction to Robot Learning - slide 14](../assets/lectures/week-01/slide-14.jpg)

```text
Feedback Welcome

= We are working hard to offer a great course
" We will probably make mistakes
=" We would love to hear your feedback!

ARE WE IMPROVISING AND GOING TO MAKE MISTAKES?
rwrue ryuaum
-- ~~

“>

q
")

rc Tamm FOR, SURE;;; ,

13
```

## Slide 15

![Introduction to Robot Learning - slide 15](../assets/lectures/week-01/slide-15.jpg)

```text
Robots in Science Fiction

The Jetsons, 1962 Transformers, 2007

Wall-E, 2008

14
```

## Slide 16

![Introduction to Robot Learning - slide 16](../assets/lectures/week-01/slide-16.jpg)

```text
Why Robots
```

## Slide 17

![Introduction to Robot Learning - slide 17](../assets/lectures/week-01/slide-17.jpg)

```text
Shakey the Robot

RESEARCH PERFORMED

by

Shakey the Robot, Stanford 1966

16
```

## Slide 18

![Introduction to Robot Learning - slide 18](../assets/lectures/week-01/slide-18.jpg)

```text
Robot Engineering

=» Sense-Plan-Act
» Similar to Shakey (1966)
=» Structured Environments

17
```

## Slide 19

![Introduction to Robot Learning - slide 19](../assets/lectures/week-01/slide-19.jpg)

```text
When State Estimation Fails

Boston Dynamics | TED

Boston Dynamics 2022

18
```

## Slide 20

![Introduction to Robot Learning - slide 20](../assets/lectures/week-01/slide-20.jpg)

```text
Moravec’s Paradox (1988)

" Abstract thinking: hard for animals, easy for Al
= Sensorimotor skills: easy for animals, hard for Al

Mees etal., 2019

19
```

## Slide 21

![Introduction to Robot Learning - slide 21](../assets/lectures/week-01/slide-21.jpg)

```text
Robot Learning

20
```

## Slide 22

![Introduction to Robot Learning - slide 22](../assets/lectures/week-01/slide-22.jpg)

```text
Robot Learning

Solving Robotics via M

Perception
Control

achine Learning

-_-~

Imitation Learning
Reinforcement Learning
Dynamics Learning
Representation Learning

21
```

## Slide 23

![Introduction to Robot Learning - slide 23](../assets/lectures/week-01/slide-23.jpg)

```text
Are These Robots?

(Wii,

ChatGPT ©

22
```

## Slide 24

![Introduction to Robot Learning - slide 24](../assets/lectures/week-01/slide-24.jpg)

```text
Why Don’t We Already Have
Autonomous Robots?

Robot is being
teleoperated!

Berger and Wyrobeck, Stanford 2007 23
```

## Slide 25

![Introduction to Robot Learning - slide 25](../assets/lectures/week-01/slide-25.jpg)

```text
Recent Hardware Advances

Humanoid Robots

NVIDIA GPUs

24
```

## Slide 26

![Introduction to Robot Learning - slide 26](../assets/lectures/week-01/slide-26.jpg)

```text
Recent Al Advances: Data Scaling

« Avg time for a human to read dataset

GPT-2
Imagenet
2 years C)
60 years

90,000 years
```

## Slide 27

![Introduction to Robot Learning - slide 27](../assets/lectures/week-01/slide-27.jpg)

```text
Recent Al Advances: Models

ALPHAGO

26
```

## Slide 28

![Introduction to Robot Learning - slide 28](../assets/lectures/week-01/slide-28.jpg)

```text
Goal: Generalist Robot Policies

Where do we get
this data from?

How can we model
the data distribution?

Robot
Foundation Model

Large Robot
Dataset

Any Task, Any Robot, Any
Environment

27
```

## Slide 29

![Introduction to Robot Learning - slide 29](../assets/lectures/week-01/slide-29.jpg)

```text
Goal: Plug-and-Play Generalist Robot Policies

pip install robot-brain
robot-brain run "d

Download Robot Brain Any Task, Any Robot, Any
Environment

28
```

## Slide 30

![Introduction to Robot Learning - slide 30](../assets/lectures/week-01/slide-30.jpg)

```text
Recent Advances in Robot Learning

Large Datasets Large Models

R Octo

Isaac GROOT
ee a ce ee RT-2
Open x.Embouiment: Robotic Loaming batacers ond REX Models sae

Open X-Embodiment Collaboration, Mees et al., ICRA, 2024.
Best Conference Paper Award (out of 1765 papers)

29
```

## Slide 31

![Introduction to Robot Learning - slide 31](../assets/lectures/week-01/slide-31.jpg)

```text
“Pick up the
spoon”

Policy

ACTION:
[ax, A9, AGrip] = ...

30
```

## Slide 32

![Introduction to Robot Learning - slide 32](../assets/lectures/week-01/slide-32.jpg)

```text
“The picture
shows

the Statue of
Liberty in NY”

“Caption the
scene”

31
```

## Slide 33

![Introduction to Robot Learning - slide 33](../assets/lectures/week-01/slide-33.jpg)

```text
“Caption the
scene”

Vision-Language
Model

“The picture
shows

the Statue of
Liberty in NY”

32
```

## Slide 34

![Introduction to Robot Learning - slide 34](../assets/lectures/week-01/slide-34.jpg)

```text
Key: Robotics as Multimodal Sequence Modeling

Language Image Answer Action

Cpe CIC) GecaoCcy) CJ) CC) Cy)

“Pick up the

spoon”

33
```

## Slide 35

![Introduction to Robot Learning - slide 35](../assets/lectures/week-01/slide-35.jpg)

```text
So we train a large transformer on robot data
and we are done?

Not quite...

34
```

## Slide 36

![Introduction to Robot Learning - slide 36](../assets/lectures/week-01/slide-36.jpg)

```text
Ingredients for Scaling Robot Learning

Large Datasets Large Models’ Scalable Evaluation

Robot Data is Scarce Robot Data is Robot Evals are
Multimodal & Tedious & Expensive
Heterogeneous
Collecting Data Robots need High Difficult to reproduce
requires Human Frequency Control
Supervision

Robot
Foundation Model

35
```

## Slide 37

![Introduction to Robot Learning - slide 37](../assets/lectures/week-01/slide-37.jpg)

```text
Algorithms for Robotic Learning

Imitation Learning

Given labeled data:
D= {Vi}
learn f(x) = y

Assumes:
inputs x are independently,
identically distributed (i.i.d.)

Supervised
Dataset |" Learning

Reinforcement Learning

Learn behavior:

Tt(als)

data is not i.i.d., actions
affect future states

GN

reward

RL

36
```

## Slide 38

![Introduction to Robot Learning - slide 38](../assets/lectures/week-01/slide-38.jpg)

```text
Course Syllabus: 1st Half

=" Robot Learning Fundamentals & Algorithms
= Robot Control & MDPs
« Imitation Learning
« Reinforcement Learning (Online & Offline)

left_wrist
REC | ep 0/2 | su 10

SPACE rec | ENTER end reset | ESC quit

Homework Assignments in Simulation

37
```

## Slide 39

![Introduction to Robot Learning - slide 39](../assets/lectures/week-01/slide-39.jpg)

```text
Course Syllabus: 2nd Half

" Scaling Robot Learning
= Generative Models
=» Sequence Modeling & Transformers
=" World Models
= Robot Foundation Models & Embodied Reasoning

Group Projects with Real Robots

38
```

## Slide 40

![Introduction to Robot Learning - slide 40](../assets/lectures/week-01/slide-40.jpg)

```text
After the Course

# You will understand:

Berger and Wyrobeck, Stanford 2007

wutonomous, unseen, 2x speed, 01:19

Physical Intelligence, 2025

39
```

## Slide 41

![Introduction to Robot Learning - slide 41](../assets/lectures/week-01/slide-41.jpg)

```text
After the Course

# You will understand:

Tesla, 2025

40
```

## Slide 42

![Introduction to Robot Learning - slide 42](../assets/lectures/week-01/slide-42.jpg)

```text
After the Course

# You will understand:

IRPLEX FAR ley s FAIRPLEX

DARPA Robotics Challenge 2015

Figure Al, 2026

41
```

## Slide 43

![Introduction to Robot Learning - slide 43](../assets/lectures/week-01/slide-43.jpg)

```text
Why You Should Study Robot Learning

" Broad skills from foundation model training to PID control
» Advances often applicable to all robotic applications

42
```

## Slide 44

![Introduction to Robot Learning - slide 44](../assets/lectures/week-01/slide-44.jpg)

```text
Thank you for your attention

and enjoy the course!
```

---

[← Course home](../README.md) · [Open optional slide gallery →](../curriculum/week-01-introduction.md)
