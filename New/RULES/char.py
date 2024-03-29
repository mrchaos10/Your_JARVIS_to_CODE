tokens = (
     'CHAR','SIGNEDCHAR','UNSIGNEDCHAR','VAR','EQUALS','NUMBER','CHARACTER'
)


# Tokens
#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d'
    return t

def t_CHAR(t):
    r'declare\sa(n)?\schar|create\sa(n)?\schar|char'
    return t

def t_SIGNEDCHAR(t):
    r'declare\sa(n)?\ssigned\schar|create\sa(n)?\ssigned\schar|signed\schar'
    return t

def t_UNSIGNEDCHAR(t):
    r'declare\sa(n)?\sunsigned\schar|create\sa(n)?\sunsigned\schar|unsigned\schar'
    return t

def t_EQUALS(t):
    r'equals\sto|equal\sto|equal(s)?|='
    print(t)
    return t



def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    print(t)
    return t

def t_CHARACTER(t):
    r'[a-zA-Z]'
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
    'statement : CHAR'
    print("char a='0';")
def p_statement_rule2(p):
    'statement : SIGNEDCHAR'
    print("signed char a='0';")
def p_statement_rule3(p):
    'statement : UNSIGNEDCHAR'
    print("unsigned char a='0';")

def p_statement_rule4(p):
    'statement : CHAR VAR'
    print("char "+str(p[2])+"='0';")
def p_statement_rule5(p):
    'statement : SIGNEDCHAR VAR'
    print("signed char "+str(p[2])+"='0';")
def p_statement_rule6(p):
    'statement : UNSIGNEDCHAR VAR'
    print("unsigned char "+str(p[2])+"='0';")

def p_statement_rule7(p):
    'statement : CHAR VAR EQUALS NUMBER'
    print("char "+str(p[2])+"='"+str(p[4])+"';")
def p_statement_rule8(p):
    'statement : CHAR VAR EQUALS CHARACTER'
    print("signed char "+str(p[2])+"='"+str(p[4])+"';")
def p_statement_rule9(p):
    'statement : CHAR VAR EQUALS VAR'
    print("signed char "+str(p[2])+"='"+str(p[4])+"';")

def p_statement_rule10(p):
    'statement : SIGNEDCHAR VAR EQUALS NUMBER'
    print("signed char "+str(p[2])+"='"+str(p[4])+"';")

def p_statement_rule11(p):
    'statement : SIGNEDCHAR VAR EQUALS CHARACTER'
    print("signed char "+str(p[2])+"='"+str(p[4])+"';")
def p_statement_rule12(p):
    'statement : SIGNEDCHAR VAR EQUALS VAR'
    print("signed char "+str(p[2])+"='"+str(p[4])+"';")

def p_statement_rule13(p):
    'statement : UNSIGNEDCHAR VAR EQUALS NUMBER'
    print("unsigned char "+str(p[2])+"='"+str(p[4])+"';")

def p_statement_rule14(p):
    'statement : UNSIGNEDCHAR VAR EQUALS CHARACTER'
    print("unsigned char "+str(p[2])+"='"+str(p[4])+"';")
def p_statement_rule15(p):
    'statement : UNSIGNEDCHAR VAR EQUALS VAR'
    print("unsigned char "+str(p[2])+"='"+str(p[4])+"';")
    
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

