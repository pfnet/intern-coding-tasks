import re

import numpy as np


tokens = ('IDENT', 'INT', 'CONST',
          'PLUS', 'MINUS', 'TIMES', 'EQUALS',
          'COMMA', 'LPAREN', 'RPAREN', 'LSPAREN', 'RSPAREN')
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_EQUALS = r'='
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSPAREN = r'\['
t_RSPAREN = r'\]'
t_IDENT = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_ignore = ' \t\n'


def t_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t


def t_CONST(t):
    r'\([\djeE.+-]+\)'
    t.value = complex(t.value)
    return t


def t_error(t):
    raise Exception('illegal character "{}"'.format(t.value[0]))
