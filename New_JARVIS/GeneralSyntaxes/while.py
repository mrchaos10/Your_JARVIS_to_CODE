tokens = (
    'NUMBER', 'WHILE', 'ITER','DEC','START','END','INC','EQ','VAR',
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
    r'while\sloop|while'
    return  t
def t_START(t):
    r'start|begin|beginning|starting'
    return  t

def t_END(t):
    r'end|ending'
    return  t
def t_EQ(t):
    r'equal(s)?|='
    #print(t)
    return t
def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    #print(t)
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
    'statement : WHILE'
    print("while()\n{\n}\n")

def p_statement_rule2(p):
    'statement : WHILE ITER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + v + "\r")
    print("int "+v+"=0;\nwhile("+v+"<" + str(p[2]).split(" ")[0] + ")\n{\n"+v+"++;\n}\n")
    f.close()


def p_statement_rule3(p):
    'statement : WHILE DEC ITER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + v + "\r")
    print("int "+v+"=" + str(p[3]).split(" ")[0] + ";\nwhile("+v+">=0)\n{\n"+v+"--;\n}\n")
    f.close()

def p_statement_rule4(p):
    'statement : WHILE START NUMBER END NUMBER'
    #print("int i;\nfor(i="+str(p[2])+";i>0"+";i--)\n{\n}\n")
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + v + "\r")
    if int(p[3])<=int(p[5]):
        print("int "+v+"="+str(p[3])+";\nwhile("+v+"<=" + str(p[5]) + ")\n{"+v+"++;\n}\n")
    else:
        print("int "+v+"=" + str(p[3]) + ";\nwhile("+v+">=" + str(p[5]) + ")\n{\n"+v+"--;\n}\n")
    f.close()

def p_statement_rule5(p):
    'statement : DEC ITER WHILE'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + v + "\r")
    print("int " + v + "=" + str(p[2]).split(" ")[0] + ";\nwhile(" + v + ">=0)\n{\n" + v + "--;\n}\n")
    f.close()

def p_statement_rule6(p):
    'statement : INC ITER WHILE'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + v + "\r")
    print("int " + v + "=0;\nwhile(" + v + "<" + str(p[2]).split(" ")[0] + ")\n{\n" + v + "++;\n}\n")
    f.close()


def p_statement_rule7(p):
   'statement : WHILE NUMBER NUMBER'
   # print("int i;\nfor(i="+str(p[2])+";i>0"+";i--)\n{\n}\n")
   f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
   v = getVar()
   f.write(v + "\r")
   f1 = open("E:\\codecompleter1\\ST.txt", "a")
   f1.write("%d " + v + "\r")
   if int(p[3]) <= int(p[5]):
       print("int " + v + "=" + str(p[2]) + ";\nwhile(" + v + "<=" + str(p[3]) + ")\n{" + v + "++;\n}\n")
   else:
       print("int " + v + "=" + str(p[2]) + ";\nwhile(" + v + ">=" + str(p[3]) + ")\n{\n" + v + "--;\n}\n")
   f.close()


def p_statement_rule8(p):
   'statement : WHILE INC ITER'
   f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
   v = getVar()
   f.write(v + "\r")
   f1 = open("E:\\codecompleter1\\ST.txt", "a")
   f1.write("%d " + v + "\r")
   print("int " + v + "=0;\nwhile(" + v + "<" + str(p[3]).split(" ")[0] + ")\n{\n" + v + "++;\n}\n")
   f.close()


def p_statement_rule9(p):
    'statement : WHILE VAR EQ NUMBER NUMBER'
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    if int(p[4])<=int(p[5]):
        print("int " + p[2] + "=" + p[4] + ";" + "\nwhile("+p[2] + "<" + p[5] + ")\n{\n" + p[2] + "++;\n}\n")
    else:
        print("int " + p[2] + "=" + p[4] + ";" + "\nwhile(" + p[2] + ">=" + p[5] + ")\n{\n" + p[2] + "--;\n}\n")
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

def infun(s1):
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
#print(s)
s.encode('UTF-8')
#print(s)
infun(s)

