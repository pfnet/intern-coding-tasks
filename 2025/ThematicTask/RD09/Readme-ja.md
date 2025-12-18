# RD09 MN-Core向けのコンパイラ及び周辺ライブラリの開発（最強のコンパイラを作ろう！）

## コーディング課題
以下の URL から受験してください。 (URL 省略)

問題は全部で 3 問あります。
- 問題 1: (非公開の問題)
- 問題 2: 浮動小数点数のブロックフロート化
- 問題 3: 長方形画像のノイズ除去

コーディング課題の回答にあたっては、以下のいずれかの言語を用いて回答してください。
- Python3
- C++

## テーマ別課題

以下の問題Aと問題Bのどちらか一方に回答してください。

### 問題 A

問題A-1とA-2の両方に、合計でA4 2枚以内で回答してください。

#### 問題 A-1

`problem_a.py` に実装された `init_matrices()` 関数は同内容の密行列と疎行列を返します。
それぞれについて、SciPy標準の行列ベクトル積 `A @ x` のベンチマークを取り、結果を論じてください。ただし、以下を守ってください。

- 回答にはベンチマークプログラムも含めてください
- 計算機環境は自由にひとつ選んで固定してください
- 行列次元 `N` は、興味深い議論ができる値を適当にひとつ選んで固定してください
- 非ゼロ要素密度 `p` は適宜変化させ、その影響を論じてください
- ベンチマークを取る際は、行列を固定して行列ベクトル積を何度も繰り返すアプリケーションを想定してください

以下はヒントです。

- 密行列と疎行列の比較だけでなく、それぞれの絶対的な性能が妥当かの考察も行うとよいでしょう
- `p` は典型的には0から0.2程度まで変化させれば十分な議論ができるようです
- 計算機環境の選択については、問題 A-2の回答しやすさも考慮してください

#### 問題 A-2

疎行列ベクトル積がボトルネックになりうるアプリケーションをひとつ選び、問題A-1と同じ計算機環境および疎行列ベクトル積実装を用いたときの性能予測を行ってください。その後、そのアプリケーションと計算機環境に特化した性能最適化について論じてください。

### 問題 B

以下の問題に答えてください。
配布された `problem_b.py` をベースに、各問題に対する実装を含みエラーなく実行できる単一の python ファイル (.py) を提出してください。(解けなかった部分があっても構いません) また、各問題の指示にしたがい、実行結果や説明を含むレポートも提出してください。形式は text か markdown か pdf で提出してください。

---

この課題では、加算と乗算とsin関数からなる単純な DSL（ドメイン固有言語）を python に埋め込むことを考えます。DSL で記述されたプログラム（例えば後述の `f_test` 関数）に対して、その解釈（後述の `Eval`, `Grad`, `IRBuilder`）を切り替えることで、さまざまな形に解釈・変換できることを見ていきます。

具体的には、DSL 内の操作として `pure`, `add`, `mul`, `sin` を考えます。
`pure` は float を受け取って DSL の値に変換します。`add` と `mul` と `sin` は DSL の値の和と積と sin を計算します。

```python
def f_test(interpreter, x, y):
    term_sin = interpreter.sin(x)
    term_mul = interpreter.mul(y, interpreter.pure(2.0))
    result = interpreter.add(term_sin, term_mul)
    return result
```

上記の `f_test` は sin(x) + y * 2.0 という計算を DSL で表現し python に埋め込んだものです。`interpreter` として解釈を与えることで、`f_test` の動作を決めることができます。

#### 問題 B-1

DSL で書かれたプログラムを通常通り実行するインタープリタを実装します。

`Eval` クラスは、計算プロセス内の操作 ( `pure`, `add`, `mul`,`sin`) を通常の数値演算として解釈します。`eval` 関数は、この `Eval` インタープリタを使って、与えられたプログラム `f` を実行します。


```python
class Eval:
    def pure(self, val):
        return float(val)
    def add(self, x, y):
        return x + y
    def mul(self, x, y):
        pass
    def sin(self, x):
        pass

def eval(f, *args):
    interpreter = Eval()
    return f(interpreter, *args)
```

(a) `Eval` クラスの `mul` メソッドと `sin` メソッドを実装してください。

(b) `eval` を使って `f_test` を `x = 2.0`, `y = 3.0` で実行し、正しく計算できていることを確かめ、その旨をレポートに記述してください。

#### 問題 B-2

次に、DSL の解釈として微分（具体的には Forward Mode 自動微分）を実装します。
Forward Mode 自動微分では、各値を微分係数とのペアとして扱い、演算ごとに微分法則を適用していくことで、関数全体の微分係数を計算します。詳細は [Wikipedia](https://en.wikipedia.org/wiki/Automatic_differentiation#Forward_and_reverse_accumulation) 等を参照してください。

`Grad` クラスは DSL の各操作がこの値と微分係数のペアをどう変換するかを定義します。`grad` は DSL で書かれた関数 `f` と、どの入力変数に関して微分するかを表すインデックス `argnum` を受け取り、`f` を `argnum` 番目の引数で偏微分した値を計算する新しい関数 (`grad_func`) を返します。

```python
class Grad:
    def pure(self, val):
        return (float(val), 0.0)
    def add(self, tx, ty):
        px, dx = tx
        py, dy = ty
        return (px + py, dx + dy)
    def mul(self, tx, ty):
        pass
    def sin(self, tx):
        pass

def grad(f, argnum=0):
    def grad_func(*args):
        pass
    return grad_func
```

(a) `Grad` クラスの `mul` メソッドと `sin` メソッドを実装してください。

(b) `grad` 関数の中にある `grad_func` を実装し、`grad(f_test, argnum=0)(2.0, 3.0)` と `grad(f_test, argnum=1)(2.0, 3.0)` をそれぞれ実行し、期待される微分係数が正しく計算できていることを確認し、レポートに記述してください。


#### 問題 B-3

最後に、DSL で書かれた関数を、中間表現（IR: Intermediate Representation）に変換し、さらにその IR から python 関数を生成する JIT (Just-In-Time) コンパイルの基礎を実装します。

`problem_b.py` の `IRBuilder` クラスは、`Eval` や `Grad` と同様にインタープリタとして振る舞いますが、計算を直接実行する代わりに、実行された DSL 操作を命令 (`Instruction` オブジェクト) のリストとして記録し、最終的に `IR` オブジェクトを構築します。`build_ir` 関数は、DSL 関数 `f` とその引数の数 `num_args` を受け取り、`IRBuilder` を用いて `IR` を生成します。

(a) `build_ir(f_test, 2)` を実行して得られる `IR` オブジェクトを確認し、元の `f_test` 関数がどのように変換されているかをレポートで説明してください。

(b) `build_ir` で得られた `IR` を使い、DSL プログラムをコンパイル（アセンブリ言語やC言語に変換することが多いが、ここでは簡単のため python 関数へ変換）します。jit 関数内で使用される `compile_ir_to_python_code` 関数を実装してください。この関数は `IR` オブジェクトを受け取り、その `IR` と等価な計算を行う python 関数のソースコードを文字列として生成し、生成した関数名と共に返す関数です。実装後、`jit` 関数が正しく動作し、`jit(f_test, 2)(2.0, 3.0)` が期待される結果を返すことを確認し、レポートに記述してください。なお、`sin` の実行には `math` モジュールが必要なので、生成した関数の先頭に `import math` を追加する必要があることに注意してください。

(c) `jit` でコンパイルされた関数の動作は、元の関数を `eval` で評価した場合と全く同じではありません。例えば以下の `f_example` では jit 後は `"hello"` が表示されません。`f_example` 以外で、`eval` で実行した場合と `jit` でコンパイルして実行した場合で動作が異なるような関数を自分で定義してください。その関数について、`eval` と `jit` それぞれで実行した場合の動作を説明し、なぜ違いが生じるのかを踏まえて考察し、レポートに記述してください。

```python
def f_example(alg, x):
    print("hello")
    return alg.add(x, x)

print(eval(f_example, 1.0))
# 出力:
# hello
# 2.0

f_example_jitted = jit(f_example, 1)
print(f_example_jitted(1.0))
# 出力:
# 2.0
```
