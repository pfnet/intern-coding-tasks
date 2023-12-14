## Task 1

You have a counter with a display showing an integer. Initially, 0 is shown in the display.
The counter also has N buttons. The i (1 ≤ i ≤ N)-th button has the integer 2<sup>i-1</sup> written in the center of the button.
When you push one of the buttons, the displayed number in the counter is increased by the number written in the button.

By pushing these buttons multiple times, you want to display X.
You may push the same button multiple times, or may decide not to push some buttons at all.
Please calculate the minimum number of pushes required to display X.

## Input
Your program should receive data from standard input.

The standard input's format is as below:

N X

Restrictions:
- N is an integer satisfying 1 ≤ N ≤ 11.
- X is an integer satisfying 1 ≤ X ≤ 2022.

## Output
Your program should write the minimum number of pushes required to display X to its standard output.

## Input & Output samples
### Sample 1
Sample Input 1
```plain
3 14
```
Sample Output 1
```plain
4
```
There are 3 buttons, 1, 2, 4, on the counter.
By pushing 2, 4, 4, 4 in order, the displayed number becomes 0 → 2 → 6 → 10 → 14.
Since you cannot create 14 with less than 4 pushes, the solution is 4.

### Sample 2
Sample Input 2
```plain
4 14
```
Sample Output 2
```plain
3
```
Since you can also use the button 8, you can display 14 with 3 button operations.

### Sample 3
Sample Input 3
```plain
10 1023
```
Sample Output 3
```plain
10
```

### Sample 4
Sample Input 4
```plain
1 2022
```
Sample Output 4
```plain
2022
```
