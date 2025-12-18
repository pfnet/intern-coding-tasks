import math

class Eval:
    def pure(self, val):
        return float(val)
    def add(self, x, y):
        return x + y
    def mul(self, x, y):
        # 問1
        pass
    def sin(self, x):
        # 問1
        pass

def eval(f, *args):
    interpreter = Eval()
    return f(interpreter, *args)

class Grad:
    def pure(self, val):
        return (float(val), 0.0)
    def add(self, tx, ty):
        px, dx = tx
        py, dy = ty
        return (px + py, dx + dy)
    def mul(self, tx, ty):
        # 問2
        pass
    def sin(self, tx):
        # 問2
        pass

def grad(f, argnum=0):
    def grad_func(*args):
        # 問2
        pass
    return grad_func

class Instruction:
    def __init__(self, op_name, args_indices, result_index, const_val=None):
        self.op_name = op_name
        self.args_indices = args_indices
        self.result_index = result_index
        self.const_val = const_val
    def __repr__(self):
        if self.op_name == 'pure':
            return f"v{self.result_index} = pure({self.const_val})"
        else:
            arg_str = ', '.join(f"v{i}" for i in self.args_indices)
            return f"v{self.result_index} = {self.op_name}({arg_str})"

class IR:
    def __init__(self, instructions, num_args, result_index, var_count):
        self.instructions = instructions
        self.num_args = num_args
        self.result_index = result_index
        self.var_count = var_count
    def __repr__(self):
        header = f"IR(num_args={self.num_args}, result=v{self.result_index}, var_count={self.var_count}):"
        instrs = "\n  ".join(repr(inst) for inst in self.instructions)
        return f"{header}\n  {instrs}"

class IRBuilder:
    def __init__(self, num_args):
        self.instructions = []
        self.var_count = num_args
        self.arg_indices = list(range(num_args))
    def _new_var(self):
        idx = self.var_count
        self.var_count += 1
        return idx
    def pure(self, val):
        result_idx = self._new_var()
        self.instructions.append(Instruction('pure', [], result_idx, const_val=float(val)))
        return result_idx
    def add(self, x_idx, y_idx):
        result_idx = self._new_var()
        self.instructions.append(Instruction('add', [x_idx, y_idx], result_idx))
        return result_idx
    def mul(self, x_idx, y_idx):
        result_idx = self._new_var()
        self.instructions.append(Instruction('mul', [x_idx, y_idx], result_idx))
        return result_idx
    def sin(self, x_idx):
        result_idx = self._new_var()
        self.instructions.append(Instruction('sin', [x_idx], result_idx))
        return result_idx
    def build(self, result_index):
        return IR(self.instructions, len(self.arg_indices), result_index, self.var_count)

def build_ir(f, num_args):
    builder = IRBuilder(num_args)
    args_indices = builder.arg_indices
    result_index = f(builder, *args_indices)
    return builder.build(result_index)

def compile_ir_to_python_code(ir):
    # 問3
    # python_code は、IR を Python のコードに変換した文字列
    # func_name は、生成した関数の名前
    return python_code, func_name

def jit(f, num_args):
    ir = build_ir(f, num_args)
    python_code_str, compiled_func_name = compile_ir_to_python_code(ir)
    execution_namespace = {}
    try:
        exec(python_code_str, globals(), execution_namespace)
    except Exception as e:
        raise e
    compiled_function = execution_namespace.get(compiled_func_name)
    if not callable(compiled_function):
        raise RuntimeError(f"Failed to define/retrieve function '{compiled_func_name}'.")
    return compiled_function

# user functions

def f_test(interpreter, x, y):
    term_sin = interpreter.sin(x)
    term_mul = interpreter.mul(y, interpreter.pure(2.0))
    result = interpreter.add(term_sin, term_mul)
    return result

def f_example(interpreter, x):
    print("hello")
    return interpreter.add(x, x)
