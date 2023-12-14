import argparse
import sys

import numpy as np
import ply.lex
import ply.yacc
import scipy as sp
import scipy.fftpack

import lexer

tokens = lexer.tokens

variables = {}


def p_statement_scalar_assign(p):
    'statement : IDENT EQUALS expression'
    variables[p[1]] = p[3]


def p_statement_array_assign(p):
    'statement : IDENT LSPAREN INT RSPAREN EQUALS expression'
    variables[p[1]][p[3]] = p[6]


def p_expression_binop(p):
    '''expression : primitive PLUS primitive
                  | primitive MINUS primitive
                  | primitive TIMES primitive
                  | primitive'''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '*':
            p[0] = p[1] * p[3]
    elif len(p) == 2:
        p[0] = p[1]
    else:
        assert False


def p_primitive_const(p):
    'primitive : CONST'
    p[0] = p[1]


def p_primitive_f(p):
    'primitive : IDENT LPAREN INT COMMA INT RPAREN'
    if p[1] != 'f':
        raise Exception('function other than "f" is not defined')
    p[0] = np.exp(-2j * np.pi * (p[3] / p[5]))


def p_primitive_scalar(p):
    'primitive : IDENT'
    try:
        value = variables[p[1]]
        if not isinstance(value, (complex, np.complex)):
            raise Exception('type of {} should be complex scalar'.format(p[1]))
        p[0] = value
    except LookupError:
        raise Exception('undefined variable "{}"'.format(p[1]))


def p_primitive_array(p):
    'primitive : IDENT LSPAREN INT RSPAREN'
    try:
        value = variables[p[1]]
        if type(value) != np.ndarray:
            raise Exception('type of {} should be ndarray'.format(p[1]))
        p[0] = value[p[3]]
    except LookupError:
        raise Exception('undefined variable "{}"'.format(p[1]))


def p_error(p):
    raise Exception('syntax error at "{}"'.format(p.value))


ply.lex.lex(module=lexer)
ply.yacc.yacc()


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(dest='dim', type=int)
    parser.add_argument('-i', dest='initializer',
                        type=str, default='sin', choices=('const', 'sin', 'sawtooth', 'chirp'))
    args = parser.parse_args()

    N = args.dim
    if args.initializer == 'const':
        x = np.ones(N, dtype=np.complex) * (0.5+0.5j)
    elif args.initializer == 'sin':
        x = (0.25 * np.sin(np.linspace(0.0, 6.0 * np.pi, num=N)) +
             0.5j * np.cos(np.linspace(0.1 * np.pi, 6.25 * np.pi, num=N)))
    elif args.initializer == 'sawtooth':
        x = (np.arange(2, N + 2) % 5 - 2) * (0.5+0.25j)
    elif args.initializer == 'chirp':
        t = np.linspace(0.0, 1.0, num=N)
        ts = 2.0 * np.pi * (0.3 + 7.0 * t + 12.0 * t * t)
        tc = 2.0 * np.pi * (0.4 + 7.0 * t + 13.0 * t * t)
        x = np.sin(ts) + 1j * np.cos(tc)
        x *= (2.0 - t) / 2.0
    y = np.zeros_like(x)
    variables['x'] = x
    variables['y'] = y
    for s in sys.stdin.readlines():
        ply.yacc.parse(s)
    for v in y:
        print(v)
    max_error = np.amax(np.abs(y - sp.fftpack.fft(x)))
    print('max_error:', max_error)


if __name__ == '__main__':
    main()
