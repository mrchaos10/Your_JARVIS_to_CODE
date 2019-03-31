tokens = (
    'DOUBLE', 'VAR', 'EQUALS', 'NUMBER', 'SIGNEDNUMBER','SIGNEDDOUBLE',
)


# Tokens
# t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+((.)\d+)?'
    return t


def t_SIGNEDNUMBER(t):
    r'(-)\d+((.)\d+)?|(\+)\d+((.)\d+)?'
    return t


def t_DOUBLE(t):
    r'declare\sa(n)?\sdouble|create\sa(n)?\sdouble|double'
    return t


def t_SIGNEDDOUBLE(t):
    r'declare\sa(n)?\ssigned\sdouble|create\sa(n)?\ssigned\sdouble|signed\sdouble'
    return t


def t_EQUALS(t):
    r'equals\sto|equal\sto|equal(s)?|='

    return t


def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'

    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_skip(t):
    r'.'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex

lex.lex()


# Parsing rules

# dictionary of names
# names = {}
def p_statement_rule1(p):
    'statement : DOUBLE'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    print("double "+v+"=0;")


def p_statement_rule2(p):
    'statement : SIGNEDDOUBLE'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    print("signed double "+v+"=0.0;")


def p_statement_rule3(p):
    'statement : DOUBLE VAR'
    print("double " + str(p[2]) + "=0.0;")


def p_statement_rule4(p):
    'statement : SIGNEDDOUBLE VAR'
    print("signed double " + str(p[2]) + "=0.0;")


def p_statement_rule5(p):
    'statement : DOUBLE VAR EQUALS NUMBER'
    print("double " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule6(p):
    'statement : DOUBLE VAR EQUALS SIGNEDNUMBER'
    print("signed double " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule7(p):
    'statement : SIGNEDDOUBLE VAR EQUALS NUMBER'
    print("signed double " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule8(p):
    'statement : SIGNEDDOUBLE VAR EQUALS SIGNEDNUMBER'
    print("signed double " + str(p[2]) + "=" + str(p[4]) + ";")


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


import ply.yacc as yacc

yacc.yacc()


def inputfunction(s1):
    yacc.parse(s1)
def getVar():
    f = open("E:\\codecompleter1\\SymbolTable.txt", "r")
    a = f.read()
    f.close()
    fl = 0
    v = ""
    for j in range(ord('a'), ord('z') + 1):
        for i in range(0, 10):
            if chr(j) + str(i) not in a:

                v = chr(j) + str(i)

                fl = 1
                break
        if fl == 1:
            break
    return v

s = input()
s.encode('UTF-8')
inputfunction(s)
