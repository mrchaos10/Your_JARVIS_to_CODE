tokens = (
     'FLOAT','DOUBLE','LONGDOUBLE','VAR','EQUALS','NUMBER','SIGNEDNUMBER'
)


# Tokens
#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+'
    return t
def t_SIGNEDNUMBER(t):
    r'(-)\d+|(\+)\d+'
    return t

def t_FLOAT(t):
    r'declare\sa(n)?\sfloat|create\sa(n)?\sfloat|float'
    return t

def t_SIGNEDFLOAT(t):
    r'declare\sa(n)?\ssigned\sfloat|create\sa(n)?\ssigned\sfloat|signed\sfloat'
    return t


def t_EQUALS(t):
    r'equals\sto|equal\sto|equal(s)?|='
    print(t)
    return t



def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    print(t)
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
    'statement : FLOAT'
    print("float a=0;")
def p_statement_rule2(p):
    'statement : SIGNEDFLOAT'
    print("signed float a=0;")

def p_statement_rule3(p):
    'statement : FLOAT VAR'
    print("float "+str(p[2])+"=0;")
def p_statement_rule4(p):
    'statement : SIGNEDFLOAT VAR'
    print("signed float "+str(p[2])+"=0;")

def p_statement_rule5(p):
    'statement : FLOAT VAR EQUALS NUMBER'
    print("float "+str(p[2])+"="+str(p[4])+";")
def p_statement_rule6(p):
    'statement : FLOAT VAR EQUALS SIGNEDNUMBER'
    print("signed float "+str(p[2])+"="+str(p[4])+";")
def p_statement_rule7(p):
    'statement : SIGNEDFLOAT VAR EQUALS NUMBER'
    print("signed float "+str(p[2])+"="+str(p[4])+";")

def p_statement_rule8(p):
    'statement : SIGNEDFLOAT VAR EQUALS SIGNEDNUMBER'
    print("signed float "+str(p[2])+"="+str(p[4])+";")
    
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

def inputfunction(s1):
    yacc.parse(s1)

s = raw_input()
s.encode('UTF-8')
inputfunction(s)

