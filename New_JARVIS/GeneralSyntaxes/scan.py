tokens = (
     'SCAN','VAR','INTEGER','FLOATER','CHARACTER','STRING'
)


# Tokens
#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_SCAN(t):
    r'scan'
    return  t
def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
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
def t_STRING(t):
    r'(string|literal)\s(variable)?'
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
    'statement : SCAN VAR'
    c = find(p[2])

    print("scanf(\"" + c + "\",&" + str(p[2]) + ");")

def p_statement_rule2(p):
    'statement : SCAN '
    print("scanf();")
def p_statement_rule7(p):
    'statement : SCAN INTEGER VAR'
    print("scanf(\"%d\",&"+str(p[3])+");")
def p_statement_rule8(p):
    'statement : SCAN FLOATER VAR'
    print("scanf(\"%f\",&"+str(p[3])+");")
def p_statement_rule9(p):
    'statement : SCAN CHARACTER VAR'
    print("scanf(\"%c\",&"+str(p[3])+");")
def p_statement_rule10(p):
    'statement : SCAN STRING VAR'
    print("scanf(\"%s\",&"+str(p[3])+");")

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