tokens = (
    'NUMBER', 'FOR', 'ITER','DEC','START','END','INC',
)


# Tokens

#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_ITER(t):
    r'\d+\stimes'
    return t
def t_NUMBER(t):
    r'\d+'
    return t


def t_DEC(t):
    r'decrement|decrease|reduce'
    return t
def t_INC(t):
    r'increment|increase'
    return t

def t_FOR(t):
    r'for\sloop'
    return  t
def t_START(t):
    r'start|begin|beginning'
    return  t

def t_END(t):
    r'end'
    return  t

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
    'statement : FOR'
    print("for(;;)\n{\n}\n")

def p_statement_rule2(p):
    'statement : FOR ITER'
    print("int i;\nfor(i=0;i<"+str(p[2]).split(" ")[0]+";i++)\n{\n}\n")

def p_statement_rule3(p):
    'statement : FOR DEC ITER'
    print("int i;\nfor(i="+str(p[3]).split(" ")[0]+";i>=0"+";i--)\n{\n}\n")

def p_statement_rule4(p):
    'statement : FOR START NUMBER END NUMBER'
    #print("int i;\nfor(i="+str(p[2])+";i>0"+";i--)\n{\n}\n")
    print(p[3])
    print(p[5])
    if int(p[3])<=int(p[5]):
        print("int i;\nfor(i="+str(p[3])+";i<=" + str(p[5]) + ";i++)\n{\n}\n")
    else:
        print("int i;\nfor(i=" + str(p[3]) + ";i>=" + str(p[5]) + ";i--)\n{\n}\n")
def p_statement_rule5(p):
    'statement : DEC ITER FOR'
    print("int i;\nfor(i=" + str(p[2]).split(" ")[0] + ";i>=0" + ";i--)\n{\n}\n")
def p_statement_rule6(p):
    'statement : INC ITER FOR'
    print("int i;\nfor(i=0;i<"+str(p[2]).split(" ")[0] + ";i++)\n{\n}\n")
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)