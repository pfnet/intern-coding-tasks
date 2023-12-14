## Task 3

You have many tiles of the same size.
Each tile is colored either red, green, or blue.
Let us call a set of tiles forming a rectangle of H rows and W columns a *pattern*.

You are considering a puzzle game converting one pattern to another.
You can conduct the following operation at arbitrary times in the game.

Operation: Select a rectangle of P rows and Q columns (you can choose any pair of P, Q for each operation) and reverse the rectangle by one of the following axes:
- the vertical axis through the center of the rectangle.
- the horizontal axis through the center of the rectangle.
- the diagonal axis from the upper-left corner to the lower-right corner (only when P = Q).
- the diagonal axis from the upper-right corner to the lower-left corner (only when P = Q). 

To estimate the difficulty of the puzzle, you want to know the minimum number of the operations required to convert one pattern to the other for a given pair of two patterns.

## Input
Your program should receive data from standard input.

The standard input's format is as below:

H W  
S<sub>1</sub>  
:  
S<sub>H</sub>  
T<sub>1</sub>  
:  
T<sub>H</sub>

Restrictions:
- 1 ≤ H ≤ 3, an integer
- 1 ≤ W ≤ 3, an integer
- S<sub>i</sub> (1 ≤ i ≤ H) , a string of W characters
  - Each character of S<sub>i</sub> is one of `r`, `g`, and `b`.
  - The j (1 ≤ j ≤ W) -th character of S<sub>i</sub> is the color of the tile of the i-th row and the j-th column of the first pattern (`r`, `g`, and `b` represent red, green, and blue, respectively).
- T<sub>i</sub> (1 ≤ i ≤ H) , a string of W characters
  - T<sub>1</sub>, ..., T<sub>H</sub> represent the colors of the tiles of the second pattern.
  - The other constraints of T<sub>i</sub> are the same as that of S<sub>i</sub>.
- The first and the second patterns are different. That is, there is some i (1 ≤ i ≤ H)  satisfying S<sub>i</sub> ≠ T<sub>i</sub> .

## Output
Your program should write the minimum number of the operations required for converting the first pattern to the second one to its standard output. If it is impossible to convert, please write `-1` instead.

## Input & Output samples
### Sample 1
Sample Input 1
```plain
2 3
ggb
rrg
rbr
ggg
```
Sample Output 1
```plain
2
```
The first pattern is as follows (`r`, `g`, `b` represents red, green, and blue, respectively).<table border=1><tr><td>g</td><td>g</td><td>b</td></tr><tr><td>r</td><td>r</td><td>g</td></tr></table>

By the following 2 operations, you can convert it to the second one. (Bold characters represent the tiles reversed by the corresponding operation.)
- Select the rectangle of 2 × 2 whose upper-left corner is  the 1st row and the 1st column of the pattern, and reverse by the horizontal axis.<table border=1><tr><th>r</th><th>r</th><td>b</td></tr><tr><th>g</th><th>g</th><td>g</td></tr></table>
- Select the rectangle of 1 × 2 whose upper-left corner is  the 1st row and the 2nd column of the pattern, and reverse by the vertical axis.<table border=1><tr><td>r</td><th>b</th><th>r</th></tr><tr><td>g</td><td>g</td><td>g</td></tr></table>

### Sample 2
Sample Input 2
```plain
2 2
rr
bg
rb
rg
```
Sample Output 2
```plain
1
```
By reversing the whole rectangle by the diagonal axis from the upper-left corner to the lower-right corner, you can convert to the second pattern.

### Sample 3
Sample Input 3
```plain
1 1
r
b
```
Sample Output 3
```plain
-1
```
In some test cases, it may be impossible to convert.
