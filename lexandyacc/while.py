tokens = (
    'NUMBER', 'WHILE', 'ITER','DEC','START','END','INC','EQ','VAR'
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
    r'decrement|decrease|reduce|decrementing|decremental|decremented'
    return t
def t_INC(t):
    r'increment|increase|incrementing|incremental|incremented'
    return t

def t_WHILE(t):
    r'while\sloop'
    return  t
def t_START(t):
    r'start|begin|beginning|starting'
    return  t

def t_END(t):
    r'end|ending'
    return  t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
def t_VAR(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t
def t_EQ(t):
    r'equal|equals|='
    return t
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
    'statement : WHILE'
    print("while()\n{\n}\n")

def p_statement_rule2(p):
    'statement : WHILE ITER'
    print("int i=0;\nwhile(i<"+str(p[2]).split(" ")[0]+")\n{\ni++;\n}\n")

def p_statement_rule3(p):
    'statement : WHILE DEC ITER'
    print("int i="+ str(p[3]).split(" ")[0] +";\nwhile(i>=0)\n{\ni--;\n}\n")

def p_statement_rule4(p):
    'statement : WHILE START NUMBER END NUMBER'
    #print("int i;\nfor(i="+str(p[2])+";i>0"+";i--)\n{\n}\n")

    if int(p[3])<=int(p[5]):
        print("int i="+str(p[3])+";\nwhile(i<=" + str(p[5]) + ")\n{i++;\n}\n")
    else:
        print("int i=" + str(p[3]) + ";\nwhile(i>=" + str(p[5]) + ")\n{\ni--;\n}\n")
def p_statement_rule5(p):
    'statement : DEC ITER WHILE'
    print("int i=" + str(p[2]).split(" ")[0] + ";\nwhile(i>=0)\n{\ni--;\n}\n")
def p_statement_rule6(p):
    'statement : INC ITER WHILE'
    print("int i=0;\nwhile(i<" + str(p[2]).split(" ")[0] + ")\n{\ni++;\n}\n")


def p_statement_rule7(p):
   'statement : WHILE NUMBER NUMBER'
   # print("int i;\nfor(i="+str(p[2])+";i>0"+";i--)\n{\n}\n")

   if int(p[2]) <= int(p[3]):
      print("int i=" + str(p[2]) + ";\nwhile(i<=" + str(p[3]) + ")\n{i++;\n}\n")
   else:
      print("int i=" + str(p[2]) + ";\nwhile(i>=" + str(p[3]) + ")\n{\ni--;\n}\n")


def p_statement_rule8(p):
   'statement : WHILE INC ITER'
   print("int i=0;\nwhile(i<" + str(p[3]).split(" ")[0] + ")\n{\ni++;\n}\n")
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

def infun(s1):
    yacc.parse(s1)

s = input()
#print(s)
s.encode('UTF-8')
#print(s)
infun(s)

