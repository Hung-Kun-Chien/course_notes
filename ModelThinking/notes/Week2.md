# Week2

## Aggregation

- Aggregation
  - Actions
    - Prediction points understand data
  - Single rule
    - normal distribution of Bell curve
  - Family rules
    - under standing patterns
  - Preferences
    - Working through logic

### Probability of Distribution

- Outcomes and Frequency
 
### Central limit theorem

- Example
  - Flip coins N times
    - Mean = N/2
    - curve approximate Bell curve
  - Binomial distribution
    - mean = pN, p is probability
- Add random variables
  - independent
  - finite variance
- Sum to a normal distribution.
- A model to describe all independent events sum up
  - to predict how possibility of the outcomes.
- Not everything all normal distribution
  - stock salves 

### Six Sigma

- A normal distribution
  - 1-$\sigma$: 68%
  - 2-$\sigma$: 95%
  - 3-$\sigma$: 99.5%
  - 6-$\sigma$: 1/3.4e6 (very small...)
- When quality is achieve 6 sigma above average, its failure rate is low.
- Control the total amount(in stock)
- control the standard derivation to meet failure in 6 sigma

### Game of Life

- A simple model to illustration the Aggregation behavior
- John Conway, 數學家
- NetLogo Simulator
- A simple rule aggregated can compound complicated output
- Self Organization: Pattern appear without a designer
- Emergence
  - Functionalities appear:
    - gliders, glider guns counter computers
- Logic Right:
  - Simple rules produce incredible phenomena

### 1D Cellular Automate

- Introduction 
  - 逢諾伊曼 design the game.
  - books: Stephen Wolfram A new kind of science
- Example Table of next generation 

| l neighborhood | current one | r neighborhood | next(rule#30) | next(rule#1) | next(rule#255) |
| -------------- | ----------- | -------------- | ------------- | ------------ | -------------- |
| 0              | 0           | 0              | 0             | 1            | 1              |
| 0              | 0           | 1              | 1             | 0            | 1              |
| 0              | 1           | 0              | 1             | 0            | 1              |
| 0              | 1           | 1              | 1             | 0            | 1              |
| 1              | 0           | 0              | 1             | 0            | 1              |
| 1              | 0           | 1              | 0             | 0            | 1              |
| 1              | 1           | 0              | 0             | 0            | 1              |
| 1              | 1           | 1              | 0             | 0            | 1              |

- "It from bit : every thing come from simple role" by John Wheeler.
- Lambda number : number of survival probability
  - When $\lambda = 4$ makes most Chaos or complex results!
    - immediate dependents.
  | $\lambda$ | all rule | class 3(Chaos) | class 4(complex) |
  | --------- | -------- | -------------- | ---------------- |
  | 0/8       | 1        | 0              | 0                |
  | 1/8       | 8        | 0              | 0                |
  | 2/8       | 28       | 2              | 0                |
  | 3/8       | 56       | 4              | 1                |
  | 4/8       | 70       | 20             | 4                |
  | 5/8       | 56       | 4              | 1                |
  | 6/8       | 28       | 2              | 0                |
  | 7/8       | 8        | 0              | 0                |
  | 8/8       | 1        | 0              | 0                |

- When learned
  - Simple rules combines to form anything
  - it from bit
  - Complexity and randomness requires interdependency

### Aggregation preference

- Preference ordering
  - how many preference ordering: example of 3 things => 8 possibility
  - Rational preference:  transitivity => A > B, B  > C implies prefer A more than C
    - only 6 ways of rational preferences
- Paradox of Preference:
  - Each person rational, Collective NOT !
  - example
  | user | preference |
  | ---- | ---------- |
  | X    | A>B>C      |
  | Y    | B>C>A      |
  | Z    | C>A>B      |
  - Collection prefernce
    - A > B : 2
    - B > C : 2
    - C > A : 2
    - A > B > C > A
  
## Decision model

- Normative(規範性): make us better at deciding 
- Positive: predict behavior of others
  - policy choice, nominations, platforms, investments, technologies choice
- Class of Decision model
  - Multi-criterion: a list of criteria and choice solution according to the criteria
    - Measurement distance between the criteria dimensions and the desired goal.
  - Probabilistic: handling uncertainty
    - decision according to current event and following outcomes.
    - value of information

### Multi-dimension decision 

- list of a criterion and alternatives table
- check meet criterion items
- give quantity of each criterion index

### Spatial choice model

- Geographical distance
- Antony Downs
- distance of the spectrum of two side.(left and right side)
- given ideal goal point => measure distance in multi-dimensional => choice the one closest to the ideal

### Probability 

### Decision Tree

- Draw the tree 
- Write down payoff and probabilities
- Solve backwards

### value of information

- Calculate value without the information
- Calculate value with the information
- Calculate the difference
- How much to worth to know the information