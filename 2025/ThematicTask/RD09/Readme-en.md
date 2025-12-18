# RD09 Development of MN-Core Compiler

## Coding Task
Please proceed to the following URL to access the coding task: (URL omitted)

The exam consists of three problems.
- Problem 1: (Undisclosed problem)
- Problem 2: Block Floating Point Numbers
- Problem 3: Noise Removal of Rectangle Images

Please provide the solutions using one of the following programming languages:
- Python3
- C++

## Thematic Task

Answer either one of Problem A or B.

### Problem A

Please answer both of Problem A-1 and Problem A-2 within two A4 pages total.

#### Problem A-1

The function `init_matrices()` implemented in `problem_a.py` returns a dense matrix and a sparse one with an identical content.
Conduct a benchmark of the implementations of matrix-vector multiplication `A @ x` in SciPy for both formats and discuss its result.

Requisites:

- Include the benchmark program to your submission
- Choose a computation environment and fix it through your report
- Choose a matrix dimension `N` which is sufficient for a fruitful discussion and fix it through your report
- Vary non-zero element density `p` and discuss its effect to performance
- Assume an application to iterate matrix-vector multiplications with a fixed matrix when designing the benchmark

Hints:

- It will be better to confirm that the absolute performance is reasonable in your report in addition to comparison of dense and sparse implementations
- Typically a range of `p` from 0 to about 0.2 is likely sufficient for a fruitful discussion
- Consider also Problem A-2 when choosing the computation environment

#### Problem A-2

Choose an application that sparse matrix-vector multiplication (SpMV) can be its performance bottleneck and estimate its performance with the computation environment and the SpMV implementation same with Problem A-1.
Then discuss its performance optimization specialized for the application and the computation environment.

### Problem B

Please answer the following questions.
Based on `problem_b.py`, please submit a single python file (.py) that includes the implementation for each question and can be executed without errors. (It's okay if some parts are unsolved.) Also, please submit a report including execution results and explanations according to the instructions for each question. The format should be text, markdown, or pdf.

In this task, we will consider embedding a simple DSL (Domain-Specific Language) consisting of addition, multiplication, and the sin function into python. We will see how a program written in the DSL (like the `f_test` function described later) can be interpreted and transformed in various ways by switching its interpretation (like `Eval`, `Grad`, `IRBuilder` described later).

Specifically, we consider the DSL operations `pure`, `add`, `mul`, and `sin`.
`pure` takes a float and converts it into a DSL value. `add`, `mul`, and `sin` calculate the sum, product, and sin of DSL values, respectively.

```python
def f_test(interpreter, x, y):
    term_sin = interpreter.sin(x)
    term_mul = interpreter.mul(y, interpreter.pure(2.0))
    result = interpreter.add(term_sin, term_mul)
    return result
```

The `f_test` function above expresses the calculation sin(x) + y * 2.0 in the DSL embedded in python. By providing an interpreter, we can define the behavior of `f_test`.

#### Problem B-1

Implement an interpreter that executes a program written in the DSL normally.

The `Eval` class interprets the operations within the DSL (`pure`, `add`, `mul`, `sin`) as standard numerical operations. The `eval` function uses this `Eval` interpreter to execute a given program `f`.

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

(a) Implement the `mul` and `sin` methods of the `Eval` class.

(b) Use `eval` to execute `f_test` with `x = 2.0`, `y = 3.0`, confirm that it calculates correctly, and describe this in your report.

#### Problem B-2

Next, implement differentiation (specifically, Forward Mode Automatic Differentiation) as an interpretation of the DSL.
In Forward Mode Automatic Differentiation, each value is treated as a pair of the value and its derivative, and by applying differentiation rules for each operation, the derivative of the entire function is calculated. For details, refer to [Wikipedia](https://en.wikipedia.org/wiki/Automatic_differentiation#Forward_and_reverse_accumulation) or similar resources.

The `Grad` class defines how each DSL operation transforms this pair of value and derivative. The `grad` function takes a DSL function `f` and an index `argnum` indicating which input variable to differentiate with respect to, and returns a new function (`grad_func`) that calculates the value of `f` partially differentiated with respect to the `argnum`-th argument.

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

(a) Implement the `mul` and `sin` methods of the `Grad` class.

(b) Implement `grad_func` inside the `grad` function. Execute `grad(f_test, argnum=0)(2.0, 3.0)` and `grad(f_test, argnum=1)(2.0, 3.0)` respectively, confirm that the expected derivatives are calculated correctly, and describe this in your report.

#### Problem B-3

Finally, implement the basics of JIT (Just-In-Time) compilation, which involves converting a function written in the DSL into an Intermediate Representation (IR) and then generating a python function from that IR.

The `IRBuilder` class in `problem_b.py` behaves as an interpreter like `Eval` and `Grad`, but instead of executing computations directly, it records the executed DSL operations as a list of instructions (`Instruction` objects) and finally constructs an `IR` object. The `build_ir` function takes a DSL function `f` and its number of arguments `num_args`, and uses `IRBuilder` to generate the `IR`.

(a) Execute `build_ir(f_test, 2)`, examine the resulting `IR` object, and explain in your report how the original `f_test` function is transformed.

(b) Using the `IR` obtained from `build_ir`, compile the DSL program (often converted to assembly language or C language, but here, for simplicity, convert it into a python function). Implement the `compile_ir_to_python_code` function used within the `jit` function. This function should take an `IR` object, generate the source code of a python function that performs computation equivalent to the `IR` as a string, and return it along with the generated function name. After implementation, confirm that the `jit` function works correctly and that `jit(f_test, 2)(2.0, 3.0)` returns the expected result, and describe this in your report. Note that executing `sin` requires the `math` module, so you need to add `import math` at the beginning of the generated function.

(c) The behavior of a function compiled with `jit` is not exactly the same as evaluating the original function with `eval`. For example, in the following `f_example`, `"hello"` is not displayed after JIT compilation. Define your own function, other than `f_example`, where the behavior differs between execution with `eval` and execution after compiling with `jit`. For that function, explain the behavior when executed with `eval` and `jit` respectively, and discuss why the difference occurs, considering the mechanisms, in your report.

```python
def f_example(alg, x):
    print("hello")
    return alg.add(x, x)

print(eval(f_example, 1.0))
# Output:
# hello
# 2.0

f_example_jitted = jit(f_example, 1)
print(f_example_jitted(1.0))
# Output:
# 2.0
```
