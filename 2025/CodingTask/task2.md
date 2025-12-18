## Task 2

単精度浮動小数点数が 4 個入力で与えられます。これらに対して以下に述べる指数部共通化処理（ブロックフロート化）を行い、結果として得られる 4 個の特殊なフォーマットの浮動小数点数を出力してください。

Four single-precision floating-point numbers are given as input. Perform the exponent unification process (block floating) described below on these numbers, and output the resulting four floating-point numbers in a special format.

### 本問題で扱う浮動小数点数の仕様と入出力フォーマット / Specification and Input/Output Format of Floating-Point Numbers Used in This Problem

本問題で扱う浮動小数点数は、それぞれ符号ビット、指数部、仮数部を表す 3 つの非負整数のタプル $(\mathrm{sign}, e, m)$ です。各要素の取り得る値の範囲には制限があり、符号ビット $\mathrm{sign}$ は $0$ か $1$ のみ、指数部 $e$ は $1$ 以上 $2^8 - 2$ 以下、仮数部 $m$ は $0$ 以上 $2^{23} - 1$ 以下です。本問題で作成していただくプログラムへの入出力の際には、それぞれの整数は二進法で表記の上、符号ビットは長さ 1, 指数部は長さ 8, 仮数部は長さ 23 になるように上位の桁をゼロ詰めし、この順に半角空白区切りで結合した形式で記述するものとします。

The floating-point numbers handled in this problem are tuples of three non-negative integers $(\mathrm{sign}, e, m)$ representing the sign bit, exponent, and mantissa, respectively. There are restrictions on the range of values each element can take: the sign bit $\mathrm{sign}$ can only be $0$ or $1$, the exponent $e$ must be between $1$ and $2^8 - 2$ (inclusive), and the mantissa $m$ must be between $0$ and $2^{23} - 1$ (inclusive). For the input and output of the program you will create, each integer is represented in binary notation, zero-padded in the upper digits to lengths of 1 for the sign bit, 8 for the exponent, and 23 for the mantissa. They are then joined in this order, separated by single spaces.

それぞれの浮動小数点数はある実数を表しています。符号ビットと指数部の値がそれぞれ $\mathrm{sign}, e$ で、仮数部の二進表記を長さ 23 の文字列として解釈したとき先頭から $i$ 文字目が $m_i$ であったとします。

Each floating-point number represents a real number. Assume the sign bit and exponent values are $\mathrm{sign}$ and $e$, respectively, and when the binary representation of the mantissa is interpreted as a string of length 23, the $i$-th character from the beginning is $m_i$.

**本問題の入力として与えられる浮動小数点数については**、これが表す値は

$$
(-1)^{\mathrm{sign}} \cdot 2^{-127 + e} \cdot \left( 1 + \sum_{i=1}^{23} 2^{-i} m_i \right)
$$

です（これは IEEE 754 の binary32 形式における正規化数の規格と同様です。なお、本問題では簡単のため NaN やゼロや無限大や非正規化数は考えないことにします）。

**Regarding the floating-point numbers given as input in this problem**, the value they represent is:

$$
(-1)^{\mathrm{sign}} \cdot 2^{-127 + e} \cdot \left( 1 + \sum_{i=1}^{23} 2^{-i} m_i \right)
$$

(This is similar to the standard for normalized numbers in the IEEE 754 binary32 format. Note that for simplicity, NaN, zero, infinity, and denormalized numbers are not considered in this problem).

一方、 **本問題で最終的に出力すべき浮動小数点数については**、これが表す値は

$$
(-1)^{\mathrm{sign}} \cdot 2^{-127 + e} \cdot \sum_{i=1}^{23} 2^{1 - i} m_i
$$

です（入力の場合と仮数部の扱いが異なり「けち表現」が使われていないことに注意してください）。例えば `0 10000010 11010000000000000000000` と記述される浮動小数点数は、

- 符号ビット `0` は $\mathrm{sign} = 0$
- 指数部 `10000010` は $e = 2^7 + 2^1 = 130$
- 仮数部 `11010000000000000000000` は $\sum_{i=1}^{23} 2^{1 - i} m_i = 2^{0} + 2^{-1} + 2^{-3} = 1.625$

と解釈され、実数値 $(-1)^0 \cdot 2^{-127 + 130} \cdot 1.625 = 13$ を表します。

On the other hand, **regarding the floating-point numbers that should ultimately be output in this problem**, the value they represent is:

$$
(-1)^{\mathrm{sign}} \cdot 2^{-127 + e} \cdot \sum_{i=1}^{23} 2^{1 - i} m_i
$$

(Note that the handling of the mantissa differs from the input case, and the "hidden bit" representation is not used). For example, the floating-point number described as `0 10000010 11010000000000000000000` is interpreted as:

- Sign bit `0` means $\mathrm{sign} = 0$
- Exponent `10000010` means $e = 2^7 + 2^1 = 130$
- Mantissa `11010000000000000000000` means $\sum_{i=1}^{23} 2^{1 - i} m_i = 2^{0} + 2^{-1} + 2^{-3} = 1.625$

representing the real value $(-1)^0 \cdot 2^{-127 + 130} \cdot 1.625 = 13$.

### 課題 / Task

上述の仕様・フォーマットに従った 4 個の浮動小数点数が入力で与えられます。各々の浮動小数点数に対して以下の処理（ブロックフロート化）を行ってください。処理結果の 4 個の浮動小数点数を、入力と同じ順序で出力してください。

Four floating-point numbers conforming to the specifications and format described above are given as input. Perform the following process (block floating) on each floating-point number. Output the four resulting floating-point numbers in the same order as the input.

#### ブロックフロート化 / Block Floating

入力で与えられた 4 個の浮動小数点数の各々について、処理結果の浮動小数点数の符号ビット、指数部、仮数部はそれぞれ以下の規則に従って定めます。

- 処理結果の符号ビットは、入力の符号ビットに等しいものとする。
- 処理結果の指数部は、入力として与えられた全ての浮動小数点数の指数部の最大値に等しいものとする。
- ここまでの処理を前提として、処理結果の仮数部は、出力の表す値の絶対値が入力の表す値の絶対値を超えない範囲で、入力と出力が表す値の絶対誤差ができるだけ小さくなるように定める（すなわち常にゼロ方向に丸める）ものとする。

For each of the four input floating-point numbers, the sign bit, exponent, and mantissa of the resulting floating-point number are determined according to the following rules:

- The sign bit of the result shall be equal to the sign bit of the input.
- The exponent of the result shall be equal to the maximum value among the exponents of all input floating-point numbers.
- Based on the sign and the shared exponent determined above, the mantissa of the result is determined to minimize the absolute error between the real value represented by the original input and the real value represented by the output, under the constraint that the absolute value of the output number does not exceed the absolute value of the input number (i.e., always round towards zero).

### （余談）本問題の背景 / (Aside) Background of This Problem

PFN が開発している AI チップ MN-Core シリーズでは、行列演算などの浮動小数点数演算を効率的に実行するため、浮動小数点数の指数部が揃った特殊なフォーマット（ブロックフロート形式）を一部の内部処理で採用しています。本問題は、実際の MN-Core におけるブロックフロート化の仕様を簡略化した上で出題しています。

In the MN-Core series of AI chips developed by PFN, a special format with unified exponents for floating-point numbers (block float format) is used in some internal processing to efficiently perform floating-point operations such as matrix calculations. This problem is based on a simplified version of the block floating specification used in the actual MN-Core.

## 実装の詳細 / Implementation

### 入力ルール / Input Rules

このプログラムに、以下のフォーマットの標準入力が与えられます。

The standard input format is as below:

$\mathrm{sign}_1$ $e_1$ $m_1$  
$\mathrm{sign}_2$ $e_2$ $m_2$  
$\mathrm{sign}_3$ $e_3$ $m_3$  
$\mathrm{sign}_4$ $e_4$ $m_4$

入力は 4 行からなります。各行は 3 つの文字列が半角空白区切りで与えられます。全ての文字列は、文字 `0` または `1` のみから構成されます。第 $i$ 行 $(i = 1, 2, 3, 4)$ には、入力で与えられる $i$ 番目の浮動小数点数の情報が、符号ビット $\mathrm{sign}_i,$ 指数部 $e_i,$ 仮数部 $m_i$ の順に半角空白区切りで与えられます。

The input consists of 4 lines. Each line contains three strings separated by single spaces. All strings consist only of the characters `0` or `1`. The $i$-th line $(i = 1, 2, 3, 4)$ provides the information for the $i$-th input floating-point number, in the order of sign bit $\mathrm{sign}_i,$ exponent $e_i,$ and mantissa $m_i$, separated by single spaces.

### 出力ルール / Output Rules

4行に渡って出力してください。 $i$ 行目 $(i = 1, 2, 3, 4)$ には、与えられた入力に対する処理の結果の $i$ 番目の浮動小数点数の情報を出力してください。

Output should span 4 lines. On the $i$-th line ($i = 1, 2, 3, 4$), output the information for the $i$-th resulting floating-point number after processing the corresponding input.

### 得点 / Score

- テストケースは 100 個存在し、全て公開されています。
- 正しい結果が出力できたテストケースの個数がそのまま得点になります。
- 全体の 20% のテストケースについて、入力で与えられる全ての浮動小数点数の指数部が一致しています。

- There are 100 test cases, and all are public.
- The number of test cases for which the correct result is output will be the score.
- For 20% of all test cases, the exponents of all input floating-point numbers are identical.

## 入出力例 / Input & Output Samples

### 例 1 / Sample 1
標準入力 / Sample Input (`00_sample001.in`)
```plain
0 10010110 11010000000000000000000
1 10000111 11010000000000000000000
1 10000010 11010000000000000000000
0 01111110 11010000000000000000000
```

入力で与えられる 4 個の浮動小数点数が表す値はそれぞれ $15204352$, $-464$, $-14.5$, $0.90625$ です。

The values represented by the four input floating-point numbers are $15204352$, $-464$, $-14.5$, and $0.90625$, respectively.

標準出力 / Sample Output
```plain
0 10010110 11101000000000000000000
1 10010110 00000000000000011101000
1 10010110 00000000000000000000111
0 10010110 00000000000000000000000
```

出力される 4 個の浮動小数点数が表す値はそれぞれ $15204352$, $-464$, $-14$, $0$ です。入力と出力でフォーマットが異なること、および 3 個目と 4 個目の浮動小数点数が表す値が入力と出力で異なることに注意してください。

The values represented by the four output floating-point numbers are $15204352$, $-464$, $-14$, and $0$, respectively. Note that the format differs between input and output, and the values represented by the third and fourth floating-point numbers differ between input and output.

### 例 2 / Sample 2
標準入力 / Sample Input (`00_sample002.in`)
```plain
0 10011000 11010000000000000001111
1 01011001 11011101101010010101010
1 10001111 11111111111111111111111
1 10011000 00000000000000000001111
```

標準出力 / Sample Output
```plain
0 10011000 11101000000000000000111
1 10011000 00000000000000000000000
1 10011000 00000000011111111111111
1 10011000 10000000000000000000111
```
