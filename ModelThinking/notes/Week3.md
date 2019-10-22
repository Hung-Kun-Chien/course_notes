# Think Electrons: Modeling People

- Topics: 
  - Rational actor Model
    - objective function: maximize what's
    - optimize: optimize the objective
  - Behavior Model
    - observe
    - Neuroscience(神經)
  - Rule Based Model
    - Schelling(謝林) model

## Rational Actors Model

- Objective: Goal, purpose, cost function
- Optimize:
  - Ex.
    - Firm(公司): maximize profits
      - revenue= price $x$ quantity
        - quantity = q, price = 50-p => $R = q\times(50-q)$ , best $q=25$
    - individual: maximize utility
      - investments
      - purchases(購買)
      - Education level
      - Vote
    - Candidate: maxim votes
- Selfish objective: objective = my happiness
- Altruistic(利他) objective: happiness of others

- Decision vs Game
  - Game: objective depends on action of others
  - Decision 
    - Large stakes(大賭注)
    - repeated
    - group decisions
    - easy problem
- Why make Rational behavior
  - Benchmarking
  - unique answer
  - easiest model
  - people learn: experiments study
  - mistake cancel: on-average behavior

## Behavioral Models

- observation
- Neurology
- Background book: 
  - thinking fast and slow
  - Nudge(推動)
- Examples
  - Prospect(期望值) Theory
    - Case 1: A win 500, B Will 1000 in 50% or 0 in 50%
    - Case 2: A -500, B Will -1000 in 50% or 0 in 50%
  - Hyperbolic discount
    - https://en.wikipedia.org/wiki/Hyperbolic_discounting
    - A 1000 in today, B 1005 in tomorrow
    - A 1000 in a year, B 1005 in a year+ 1 day. 
  - Status Quo Bias
    - Check box effect: only low % to check the box.
    - https://zh.wikipedia.org/wiki/%E7%8E%B0%E7%8A%B6%E5%81%8F%E5%B7%AE
  - Base Rate Bias
    - https://en.wikipedia.org/wiki/Base_rate_fallacy

- Lots of bias
  - Weird
  - people learn
  - computationally difficult
- Based on rational model and add learned bias effect

## Rule Based 

- Types of rule
|          | Decision         | Game        |
| -------- | ---------------- | ----------- |
| Fixed    | divide evenly    | Tit for tat |
| Adaptive | gradients/random |             |

- Random choice
  - most direct route
- Fixed strategies
  - decision divide evenly
  - Tit for tat
- Adaptive rules
  - gradients/random
- Adaptive strategies
  - best response
  - mimicry (copy the action)

- observation # 1: Sometimes optimal rules are simples
  - Objective: Happiness 
  - optimal behavior...
- Observation 2: simple rules can offend be exploited(利用)
- Why use rule based
  - easy to model
  - capture main effects
  - Ad Hoc
  - exploited

## When Does Behavior Model Matters

- Rational is easily to benchmarking 
- irrational(Human) makes some bias
- some bias will cause different outcomes
- Example of the game of guess of mean
  - rule: who will win the money if his guess is 2/3 of average of all.
  - if all rational => final outcome will be zero
  - if some irrational => outcome will be $\frac{(2\times\sum X_i)}{3\times N+M}$
    - $N$: number of irrational
    - $M$: number of rational
    - $X_i$: irrational $i$ guess value
    - $(\sum X_i + M\times R)/(M+N)\times (2/3) = R$