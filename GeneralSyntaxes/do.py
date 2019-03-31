tokens = (
    'NUMBER', 'DO', 'ITER','DEC','START','END','INC',
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

def t_DO(t):
    r'do\sloop'
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
    'statement : DO'
    print("do\n{\n}while();\n")

def p_statement_rule2(p):
    'statement : DO ITER'
    print("int i=0;\ndo\n{\ni++;\n}\nwhile(i<"+str(p[2]).split(" ")[0]+");")

def p_statement_rule3(p):
    'statement : DO DEC ITER'
    print("int i="+ str(p[3]).split(" ")[0] +";\ndo\n{\ni--;\n}\nwhile(i>=0);\n")

def p_statement_rule4(p):
    'statement : DO START NUMBER END NUMBER'
    #print("int i;\nfor(i="+str(p[2])+";i>0"+";i--)\n{\n}\n")

    if int(p[3])<=int(p[5]):
        print("int i="+str(p[3])+";\ndo\n{\ni++;\n}while(i<=" + str(p[5]) + ");")
    else:
       print("int i=" + str(p[3]) + ";\ndo\n{\ni--;\n}while(i>=" + str(p[5]) + ");")
def p_statement_rule5(p):
    'statement : DEC ITER DO'
    print("int i=" + str(p[2]).split(" ")[0] + ";do\n{\ni--;\n}while(i>=0);")
def p_statement_rule6(p):
    'statement : INC ITER DO'
    print("int i=0;\ndo\n{\ni++;\n}while(i<" + str(p[2]).split(" ")[0] + ");")


def p_statement_rule7(p):
   'statement : DO NUMBER NUMBER'
   # print("int i;\nfor(i="+str(p[2])+";i>0"+";i--)\n{\n}\n")

   if int(p[2]) <= int(p[3]):
      print("int i=" + str(p[2]) + ";\ndo\n{i++;\n}\nwhile(i<=" + str(p[3]) + ");")
   else:
      print("int i=" + str(p[2]) + ";\ndo\n{i--;\n}\nwhile(i>=" + str(p[3]) + ");")


def p_statement_rule8(p):
   'statement : DO INC ITER'
   print("int i=0;\ndo\n{\ni++;\n}while(i<" + str(p[3]).split(" ")[0] + ");")
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