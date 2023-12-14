## Task 2

You are packing a subset of N items to a knapsack.
Each item has a unique number from 1 to N. The i-th item's weight, value, and rating are defined as w<sub>i</sub>, v<sub>i</sub>, and r<sub>i</sub>, respectively.
The limitation for the total weight of items is W.
You are trying to increase the sum of values and the sum of ratings, but they cannot always be maximized at the same time.
Therefore, you decide to count the number of packing patterns satisfying the following condition.

Let X be the selected pattern. For each other possible packing pattern Y, at least one of the following is true:

- The total value of X is larger than that of Y.
- The total rating of X is larger than that of Y.
- The total value and the total rating of X are equal to those of Y.

## Input
Your program should receive data from standard input.

The standard input's format is as below:

N W  
w<sub>1</sub> v<sub>1</sub> r<sub>1</sub>  
w<sub>2</sub> v<sub>2</sub> r<sub>2</sub>  
:  
w<sub>N</sub> v<sub>N</sub> r<sub>N</sub>

Restrictions:
- 1 ≤ N ≤ 20, Integer
- 1 ≤ W ≤ 1,000,000,000, Integer
- 1 ≤ w<sub>i</sub>, v<sub>i</sub>, r<sub>i</sub> ≤ 10,000,000, Integer

## Output
Your program should write the number of the packing patterns defined in the problem statement to the standard output.

## Input & Output samples
### Sample 1
Sample Input 1
```plain
4 7
3 1 4
3 4 1
2 2 2
4 3 3
```
Sample Output 1
```plain
4
```

- If you pack 1st item and 2nd item, the sum of values is 5 and the sum of rating is 5.
- If you pack 1st item and 4th item, the sum of values is 4 and the sum of rating is 7.
- If you pack 2nd item and 4th item, the sum of values is 7 and the sum of rating is 4.
- If you pack 3rd item and 4th item, the sum of values is 5 and the sum of rating is 5.


### Sample 2
Sample Input 2
```plain
5 2
1 1 5
1 2 4
1 3 3
1 4 2
1 5 1
```
Sample Output 2
```plain
10
```
