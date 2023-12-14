## Task 1

You are given a 6-digit hexadecimal number X. Return the minimum value (in decimal) Y made by extracting 3 digits from X and concatenating them without reordering. X and Y can have leading zeros.

## Input & Output

### Input
Your program should receive standard input.

The standard input's format is as below:

X

Restrictions:
- X is a sequence of characters of length 6, consisting of '0'-'9' and 'a'-'f'.

### Output
Your program should write the minimum possible value of Y in base 10 to its standard output.

## Input & Output samples
### Sample 1
Sample Input 1
```
aebf35
```
Sample Output 1
```
2613
```
We can obtain 'a35' by choosing the first, fifth and sixth digits from the left. This value, 2613 in base 10, is the minimum possible value.

### Sample 2
Sample Input 2
```
def123
```
Sample Output 2
```
291
```

### Sample 3
Sample Input 3
```
be3a70
```
Sample Output 3
```
880
```

### Sample 4
Sample Input 4
```
05330a
```
Sample Output 4
```
10
```
The minimum possible value is '00a'. Note that the most significant digit can be '0'.
