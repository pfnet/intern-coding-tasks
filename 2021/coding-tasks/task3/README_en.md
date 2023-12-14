## Task 3

This problem deals with a data structure that imitates a version control system.

This version control system manages a single project. The system assigns "version" to the project history and holds "commit" information representing a change in the project. At the beginning of the project, the project version is 0. The first commit is numbered 1, the second is numbered 2, and so on. Project history created by commit i has a version i. In this problem, we consider the case where there are N commits.

There are two types of commits -- "update commit" that updates the project from one of past versions and "merge commit" that merges the two versions' contents. The update commit has information about the original version, and the merge commit has information about the two versions.

We want to add a feature to discover when a new bug occurred to this version control system. There is a list of versions that have no bugs and a list of versions that have bugs. The task is to count  the number of versions where the bug may have occurred for the first time. Here, we assume that the bug occurred in precisely one version, and later versions have no new bugs or bug fixes.

## Input & Output

### Input
Your program should receive standard input.

The standard input's format is as below:

N A B  
commit<sub>1</sub>  
:  
commit<sub>N</sub>  
p<sub>1</sub> ... p<sub>A</sub>  
q<sub>1</sub> ... q<sub>B</sub>

The first line shows the number of commits N, the number of versions confirmed to be bug-free A, and the number of versions confirmed to have a bug B. (1 ≤ N ≤ 1000, 1 ≤ A, B ≤ N )
The following N lines give commit information. Each commit information is given in the following format:

- Updates

UPDATE v

v represents the original version.

- Merges

MERGE v<sub>1</sub> v<sub>2</sub>

v<sub>1</sub> and v<sub>2</sub> represent the two original versions. (v<sub>1</sub> ≠ v<sub>2</sub>)

For both update and merge commits, the original versions are guaranteed to be smaller than the version created by the commit.

The next two lines give a list of confirmed bug-free versions p and a list of confirmed buggy versions q.

It is guaranteed that at least one version can be seen as a cause of the bug.
Thus, inconsistent input will not be given. For example, the same version will not appear in both p and q at the same time.

### Output
Print the number of versions where the bug occurs for the first time in a single line to standard output.

## Input & Output samples
### Sample 1
Sample Input 1
```
3 1 1
UPDATE 0
UPDATE 1
MERGE 1 2
1
3
```
Sample Output 1
```
2
```
The bug has occurred in version 2 or 3.
If version 2 causes the bug, versions 0 and 1 do not have the bug, and versions 2 and 3 have the bug.
If version 3 causes the bug, versions 0, 1, and 2 do not have the bug, and version 3 has the bug.

### Sample 2
Sample Input 2
```
12 3 3
UPDATE 0
UPDATE 1
UPDATE 2
UPDATE 3
MERGE 4 0
MERGE 2 1
MERGE 5 6
UPDATE 7
MERGE 8 4
UPDATE 9
MERGE 10 2
UPDATE 11
3 2 6
11 9 5
```
Sample Output 2
```
2
```
The bug has occurred in version 4 or 5.
If version 4 causes the bug, versions 0, 1, 2, 3, and 6 do not have the bug, and versions 4, 5, 7, 8, 9, 10, 11, and 12 have the bug.
If version 5 causes the bug, versions 0, 1, 2, 3, 4, and 6 do not have the bug, and versions 5, 7, 8, 9, 10, 11, and 12 have the bug.
