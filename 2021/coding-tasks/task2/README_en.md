## Task 2

In this problem, we deal with convolutional operations, which are commonly used in image processing.

For one dimensional array A of n elements and B of m (≤ n) elements, the convolution of A and B, denoted by (A * B), is an array of n-m+1 elements, where each element is defined as follows.

(A * B)<sub>i</sub> = Σ<sub>j=1</sub><sup>m</sup> A<sub>i+j-1</sub> B<sub>j</sub>

(Note: There was a mistake in the subscript at the coding test. We corrected it for publication.)

For example, [1, 2, -3, 4] * [2, -1] = [0, 7, -10].

Consider the case when the number of elements in A is represented as n=k(m-1)+1 for some positive integer k.
When we repeat the operation to perform convolution on A with B k times, it will result in an array of a single element.
Using some array C, this result can be represented as

(((A * B) * B) * ... * ) * B = A * C

for any A. Here, B will appear exactly k times in the above equation.
Find the array C that satisfies the above equation.

#### Note

In signal processing and some of other fields, the operation * is called cross-correlation.

## Input & Output

### Input
Your program should receive standard input.

The standard input's format is as below:

m k  
B<sub>1</sub> ... B<sub>m</sub>


Restrictions:
- 2 ≤ m ≤ 6, Integer
- 1 ≤ k ≤ 10, Integer
- -5 ≤ B<sub>i</sub> ≤ 5, Integer

### Output
Your program should write the answer to its standard output.

The standard output's format is as below:

C<sub>1</sub> ... C<sub>k(m-1)+1</sub>

- On the 1st line, print the content of array C separated by a single space.

## Input & Output samples
### Sample 1
Sample Input 1
```
2 1
2 -1
```
Sample Output 1
```
2 -1
```
When the number of convolutions is 1, the answer is the same with B.

### Sample 2
Sample Input 2
```
2 2
2 -1
```
Sample Output 2
```
4 -4 1
```

[A<sub>1</sub>, A<sub>2</sub>, A<sub>3</sub>] * [2, -1] = [2A<sub>1</sub>-A<sub>2</sub>, 2A<sub>2</sub>-A<sub>3</sub>].
Performing one more convolutional calculation, we obtain
[2A<sub>1</sub>-A<sub>2</sub>, 2A<sub>2</sub>-A<sub>3</sub>] * [2, -1] = [4A<sub>1</sub>-4A<sub>2</sub>+A<sub>3</sub>] = [A<sub>1</sub>, A<sub>2</sub>, A<sub>3</sub>] * [4, -4, 1].

### Sample 3
Sample Input 3
```
6 10
5 5 5 5 5 5
```
Sample Output 3
```
9765625 97656250 537109375 2148437500 6982421875 19550781250 48779296875 110742187500 232031250000 453320312500 832304687500 1444726562500 2382080078125 3744824218750 5630517578125 8117226562500 11243847656250 14990625000000 19263964843750 23889648437500 28617724609375 33140722656250 37124365234375 40246679687500 42239355468750 42924375000000 42239355468750 40246679687500 37124365234375 33140722656250 28617724609375 23889648437500 19263964843750 14990625000000 11243847656250 8117226562500 5630517578125 3744824218750 2382080078125 1444726562500 832304687500 453320312500 232031250000 110742187500 48779296875 19550781250 6982421875 2148437500 537109375 97656250 9765625
```

The answer may exceed the range that can be handled by a 32-bit integer.
