tokens = (
     'ELSE',
)

def t_ELSE(t):
    r'else|else\s(for\s)?above\sstatement|else\s(for\s)?above\sif\sstatement|else\sblock|(put\san\s)?else\sblock'

    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_skip(t):
    r'.'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()

def p_statement_rule1(p):
    'statement : ELSE'
    print("else\n{\n}\n")
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

def inputfunction(s1):
    yacc.parse(s1)

s = input()
s.encode('UTF-8')
inputfunction(s)