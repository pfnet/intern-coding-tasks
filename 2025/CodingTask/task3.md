## Task 3

$N \times N$ のグリッド状のマスに区切られた正方形のキャンバスがあります。上から $i$ 番目、左から $j$ 番目のマス $(1 \le i \le N, 1 \le j \le N)$ をマス $(i, j)$ と表すことにします。初期状態では $N^2$ 個のマス全てが白く塗られていました。

There is a square canvas divided into an $N \times N$ grid of cells. The cell in the $i$-th row from the top and the $j$-th column from the left ($1 \le i \le N, 1 \le j \le N$) will be denoted as cell $(i, j)$. Initially, all $N^2$ cells are painted white.

A さんが以下の手順に従ってキャンバスに絵を描きました。

1. $1$ 以上 $N$ 以下の整数 $L$ を一様ランダムに生成する。
2. $1$ 以上 $N - L + 1$ 以下の整数 $X, Y$ をそれぞれ一様ランダムに生成する。
3. $X \le i \lt X + L$ かつ $Y \le j \lt Y + L$ を満たす全てのマス $(i, j)$ を黒く塗る。
4. $N^2$ 個のマス全てについて、独立に $P$% の確率で色を反転させる。すなわち、各マスについて、そのマスが白く塗られていたならば $P$% の確率で黒く塗り替える。逆に黒く塗られていたならば $P$% の確率で白く塗り替える。

Person A draws on the canvas according to the following procedure:

1. Generate an integer $L$ uniformly at random from the range $1$ to $N$, inclusive.
2. Generate integers $X$ and $Y$ uniformly at random from the range $1$ to $N - L + 1$, inclusive, respectively.
3. Paint all cells $(i, j)$ black that satisfy $X \le i \lt X + L$ and $Y \le j \lt Y + L$.
4. For each of the $N^2$ cells, independently flip its color with a probability of $P$%. That is, for each cell, if it was white, repaint it black with $P$% probability. Conversely, if it was black, repaint it white with $P$% probability.

なお上記の過程において、全ての乱数は互いに独立に生成されたものとします。

Note that in the process described above, all random numbers are generated independently of each other.

あなたは $N, P$ の具体的な値と最終的なキャンバスの状態のみが知らされます。このとき、 $N, P$ とキャンバスの最終状態のもとでの手順 3 を終えた時点のキャンバスの中間状態の条件付き確率を考えることができます。その条件付き確率が最も大きくなるような中間状態を出力してください。また、その条件付き確率の具体的な値も出力してください。

You are only given the specific values of $N, P$, and the final state of the canvas. At this point, you can consider the conditional probability of the intermediate state of the canvas (after step 3 is completed) given $N, P$, and the final state of the canvas. Output the intermediate state that maximizes this conditional probability. Also, output the specific value of that maximum conditional probability.

## 実装の詳細 / Implementation

### 入力ルール / Input Rules

このプログラムに、以下のフォーマットの標準入力が与えられます。

The standard input format is as below:

$N$ $P$  
$S_1$  
$\vdots$  
$S_N$

先頭の行に、キャンバスのグリッドの個数 $N$ とノイズのパラメータ $P$ の値が与えられます。 $N$ は $1$ 以上 $200$ 以下、 $P$ は $1$ 以上 $99$ 以下の整数です。続く $N$ 行に、最終的なキャンバスの状態を示す文字列が与えられます。各文字列 $S_i$ の長さは $N$ です。各 $(i, j)$ $(i = 1, \ldots, N, j = 1, \ldots, N)$ について、 $S_i$ の $j$ 文字目はマス $(i, j)$ が最終的に白く塗られているとき `.`, 黒く塗られているとき `#` です。

The first line contains the size of the canvas grid $N$ and the noise parameter $P$. $N$ is an integer between $1$ and $200$, inclusive. $P$ is an integer between $1$ and $99$, inclusive. The following $N$ lines contain strings representing the final state of the canvas. Each string $S_i$ has length $N$. For each $(i, j)$ ($i = 1, \ldots, N, j = 1, \ldots, N$), the $j$-th character of $S_i$ is `.` if cell $(i, j)$ is finally white, and `#` if it is finally black.

なお本問題の入力としては、最も条件付き確率が大きい中間状態が、ほかの任意の中間状態より $10^{-7}$ 以上大きい条件付き確率を持つようなもののみが与えられます。

Note that for the inputs in this problem, it is guaranteed that the intermediate state with the highest conditional probability has a probability at least $10^{-7}$ greater than any other intermediate state.

### 出力ルール / Output Rules
1行目から $N$ 行目にかけて、手順 3 を終えた時点のキャンバスの中間状態として、特に条件付き確率が最大となるようなものを出力してください。この形式は、入力の $S_1, \ldots, S_N$ の形式と同様とします。最後に、 $N + 1$ 行目にその中間状態に対応する条件付き確率の値を出力してください。

From the 1st line to the $N$-th line, output the intermediate state of the canvas (after step 3) that corresponds to the maximum conditional probability. This format should be the same as the input format for $S_1, \ldots, S_N$. Finally, on the $(N + 1)$-th line, output the value of the conditional probability corresponding to that intermediate state.

なお各テストケースの正誤判定時に、条件付き確率の値に関しては $10^{-7}$ までの絶対誤差が許容されます。

Note that when judging the correctness for each test case, an absolute error of up to $10^{-7}$ is allowed for the conditional probability value.

### 得点 / Score

- テストケースは 100 個存在し、全て公開されています。
- 正しい結果が出力できたテストケースの個数がそのまま得点になります。
- 全体の 50% のテストケースについて、答えの条件付き確率の値が $1 - 10^{-7}$ より大きいことが保証されます。先述した許容誤差の関係上、これらのテストケースでは（中間状態の推定さえ適切であれば）条件付き確率として単に $1$ と出力しても正答となります。
- 全体の 40% のテストケースが $1 \le N \le 20$ を満たします。また、全体の 40% のテストケースが $21 \le N \le 100$ を満たします。

* There are 100 test cases, and all are public.
* The score is the number of test cases for which the correct result is output.
* For 50% of all test cases, it is guaranteed that the conditional probability of the answer is greater than $1 - 10^{-7}$. Due to the aforementioned error tolerance, for these test cases, outputting simply $1$ as the conditional probability will be considered correct (provided the intermediate state estimation is appropriate).
* 40% of all test cases satisfy $1 \le N \le 20$. Additionally, 40% of all test cases satisfy $21 \le N \le 100$.

## 入出力例 / Input & Output Samples
### 例 1 / Sample 1
標準入力 / Sample Input (`00_sample001.in`)
```plain
5 1
#....
.....
..##.
..##.
.....
```

標準出力 / Sample Output
```plain
.....
.....
..##.
..##.
.....
0.999996658
```

### 例 2 / Sample 2
標準入力 / Sample Input (`00_sample002.in`)
```plain
20 5
.....##.............
.......#.#..........
......#.............
....................
......#.............
##########.###......
#######..###.#......
###############...#.
##############...##.
##############......
##.###########......
##############..#...
#####.########......
##############......
#############.......
#.######.####.......
##############......
##############......
##.###########......
......#.............
```

標準出力 / Sample Output
```plain
....................
....................
....................
....................
....................
##############......
##############......
##############......
##############......
##############......
##############......
##############......
##############......
##############......
##############......
##############......
##############......
##############......
##############......
....................
1.0
```

### 例 3 / Sample 3
標準入力 / Sample Input (`00_sample003.in`)
```plain
20 1
##...#...#.#.#..####
.##.#.###..##..##.##
#..#.#.##.#....###.#
##.#.#..##.##.###.#.
.#.###.###.###.###.#
.#.#.#.##.#.###.#..#
.#..#...####..###.#.
...#.#.#...#.##.#..#
###..###.#..########
###..###.##.##.###.#
..###.##...#..#.####
#.###.#.#.##.#.#.#..
..####.#..##..#.####
....#...##.####.###.
..##.##......#.####.
#######...#.#.#..###
..#..#..#.#..###.#..
.##..#.##.##..##..#.
#...#.#....###..#..#
.#..##.......#.#####
```

標準出力 / Sample Output
```plain
..##################
..##################
..##################
..##################
..##################
..##################
..##################
..##################
..##################
..##################
..##################
..##################
..##################
..##################
..##################
..##################
..##################
..##################
....................
....................
0.983001796
```

A さんが行う手順では極めて生成されにくいような最終状態が入力として与えられることもあります。

It is possible for the input to represent a final state that is extremely unlikely to be generated by Person A's procedure.
