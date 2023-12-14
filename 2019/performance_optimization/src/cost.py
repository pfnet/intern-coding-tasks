import sys

import ply.lex
import ply.yacc

import lexer

tokens = lexer.tokens

COST = 0


def p_statement_scalar_assign(p):
    'statement : IDENT EQUALS expression'
    pass


def p_statement_array_assign(p):
    'statement : IDENT LSPAREN INT RSPAREN EQUALS expression'
    pass


def p_expression_binop(p):
    '''expression : primitive PLUS primitive
                  | primitive MINUS primitive
                  | primitive TIMES primitive
                  | primitive'''
    global COST
    if len(p) == 4:
        if p[2] in ('+', '-'):
            COST += 1
        elif p[2] == '*':
            COST += 2
    elif len(p) == 2:
        pass
    else:
        assert False


def p_primitive_const(p):
    'primitive : CONST'
    pass


def p_primitive_f(p):
    'primitive : IDENT LPAREN INT COMMA INT RPAREN'
    pass


def p_primitive_scalar(p):
    'primitive : IDENT'
    pass


def p_primitive_array(p):
    'primitive : IDENT LSPAREN INT RSPAREN'
    pass


def p_error(p):
    raise Exception('syntax error at "{}"'.format(p.value))


ply.lex.lex(module=lexer)
ply.yacc.yacc()


def main():
    for s in sys.stdin.readlines():
        ply.yacc.parse(s)
    print(COST)


if __name__ == '__main__':
    main()
