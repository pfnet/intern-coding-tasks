## Task 4

We prepare some 100-sided dice, conduct an experiment and report the results to you. Write a program to estimate the number of dice. You can assume that the number of dice is up to 5.

The experiment and report are as follows:

- Throw all dice and report the maximum number of them.
- Repeat this operation 10 times.

These dice have 100 faces numbered from 1 to 100, and these faces appear with equal probability.
The inputs are randomly generated.

**In this problem, even the expected algorithm may fail to estimate the correct number in some inputs. We evaluate what theory or idea is used in your program rather than score.**

## Input
Your program should receive data from standard input.

The standard input's format is as below:

m<sub>1</sub> ... m<sub>10</sub>

m<sub>i</sub> represents the maximum number of rolls for the i-th play.

Restrictions:
- 1 ≤ m<sub>i</sub> ≤ 100, Integer

## Output
Your program should write the estimated number of dice to its standard output. You can assume that the number of dice is up to 5.

## Input & Output samples
### Sample 1
Sample Input 1
```plain
87 98 48 58 59 97 43 100 96 73
```
Sample Output 1
```plain
3
```

### Sample 2
Sample Input 2
```plain
73 78 91 78 27 92 79 93 85 89
```
Sample Output 2
```plain
5
```
