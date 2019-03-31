tokens = (
     'SCAN','NUMBER','VAR','GENERAL','CHAR','PRECISION','FLOAT','INTEGER','FLOATER','CHARACTER','STRING'
)


# Tokens
#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+'
    return t
def t_FLOAT(t):
    r'[0-9]?.\d+'
    return t
def t_CHAR(t):
    r'(char(acter)?)?[a-zA-Z]'
    return t

def t_GENERAL(t):
    r'scanf(.*)'
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

def t_PRECISION(t):
    r'(with|or|for)?\sthe\sprecision'
    return t

def t_SCAN(t):
    r'(declare(\sa(n)?)?\s)?scan(f)?(\sstatement)?|(create(\sa(n)?)?)?\sscan(f)?)(\sstatement)?|scan(f)?|put((\sto\sthe)?\sinput(\sstream)?)?|stdin|standard\sin(put)?|(declare|scan)\sthe\sfollowing\sto\sthe\sinput|'
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
    'statement : SCAN'
    print("scanf();")
def p_statement_rule2(p):
    'statement : GENERAL'
    print(str(p[1])+";")

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

s = raw_input()
s.encode('UTF-8')
inputfunction(s)

