tokens = (
     'PRINT','NUMBER','VAR','CHAR','PRECISION','FLOAT','INTEGER','FLOATER','CHARACTER','STRING'
)


# Tokens
#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_PRINT(t):
    r'print'
    return t
def t_NUMBER(t):
    r'\d+'
    return t
def t_FLOAT(t):
    r'[0-9]+(.)\d+'
    return t
def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'

    return t
def t_CHAR(t):
    r'(char(acter)?)?[a-zA-Z]'
    return t
def t_STRING(t):
    r'".*"'
    return t

def t_INTEGER(t):
    r'int(eger)?\s(variable)?'
    return t
def t_FLOATER(t):
    r'float\s(variable)?'
    return t
def t_CHARACTER(t):
    r'char(acter)?\s(variable)?'
    return t


def t_PRECISION(t):
    r'(with|or|for)?\sthe\sprecision'
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
#names = {}
def p_statement_rule1(p):
    'statement : PRINT'
    print("printf();")


def p_statement_rule3(p):
    'statement : PRINT CHAR'
    print("printf(\"%c\"," + p[2] + ");")

def p_statement_rule4(p):
    'statement : PRINT NUMBER'
    print("printf(\"%d\","+p[2]+");")

def p_statement_rule5(p):
    'statement : PRINT FLOAT'
    print("printf(\"%f\"," + p[2] + ");")

def p_statement_rule6(p):
    'statement : PRINT FLOAT PRECISION NUMBER'
    print("printf(\"%"+str(p[4])+"f\","+str(p[2])+");")
def p_statement_rule7(p):
    'statement : PRINT INTEGER VAR'
    print("printf(\"%d\","+str(p[3])+");")
def p_statement_rule8(p):
    'statement : PRINT FLOATER VAR'
    print("printf(\"%f\","+str(p[3])+");")
def p_statement_rule9(p):
    'statement : PRINT CHARACTER VAR'
    print("printf(\"%c\","+str(p[3])+");")
def p_statement_rule10(p):
    'statement : PRINT STRING VAR'
    print("printf(\"%s\","+str(p[3])+");")
def p_statement_rule12(p):
    'statement : PRINT STRING'
    print("printf("+str(p[2])+");")
def p_statement_rule11(p):
    'statement : PRINT VAR'
    c = find(p[2])

    print("printf(\""+c+"\","+str(p[2])+");")

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

def inputfunction(s1):
    yacc.parse(s1)
def find(x):
    f = open("E:\\codecompleter1\\ST.txt", "r")
    line = f.readline()
    while line:
        if x in line:

            c=line.split(" ")
            f.close()
            return c[0]
        else:
            line = f.readline()

s = input()
s.encode('UTF-8')
inputfunction(s)