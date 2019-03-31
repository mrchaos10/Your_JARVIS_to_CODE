tokens = (
    'FLOAT', 'VAR', 'EQUALS', 'NUMBER', 'SIGNEDNUMBER','SIGNEDFLOAT',
)


# Tokens
# t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+((.)\d+)?'
    return t


def t_SIGNEDNUMBER(t):
    r'(-)\d+((.)\d+)?|(\+)\d+((.)\d+)?'
    return t


def t_FLOAT(t):
    r'declare\sa(n)?\sfloat|create\sa(n)?\sfloat|float'
    return t


def t_SIGNEDFLOAT(t):
    r'declare\sa(n)?\ssigned\sfloat|create\sa(n)?\ssigned\sfloat|signed\sfloat'
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
    'statement : FLOAT'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%f " + v + "\r")
    print("float "+v+"=0;")


def p_statement_rule2(p):
    'statement : SIGNEDFLOAT'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%f " + v + "\r")
    print("signed float "+v+"=0.0;")


def p_statement_rule3(p):
    'statement : FLOAT VAR'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")

    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%f " + p[2] + "\r")
    print("float " + str(p[2]) + "=0.0;")


def p_statement_rule4(p):
    'statement : SIGNEDFLOAT VAR'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")

    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%f " + p[2] + "\r")
    print("signed float " + str(p[2]) + "=0.0;")


def p_statement_rule5(p):
    'statement : FLOAT VAR EQUALS NUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")

    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%f " + p[2] + "\r")
    print("float " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule6(p):
    'statement : FLOAT VAR EQUALS SIGNEDNUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")

    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%f " + p[2] + "\r")
    print("signed float " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule7(p):
    'statement : SIGNEDFLOAT VAR EQUALS NUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")

    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%f " + p[2] + "\r")
    print("signed float " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule8(p):
    'statement : SIGNEDFLOAT VAR EQUALS SIGNEDNUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")

    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%f " + p[2] + "\r")
    print("signed float " + str(p[2]) + "=" + str(p[4]) + ";")


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
