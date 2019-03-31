tokens = (
    'NUMBER', 'FOR', 'ITER','DEC','START','END','INC','EQ','VAR',
)


# Tokens

#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_ITER(t):
    r'\d+\stimes'
    print(t) 
    return t
def t_NUMBER(t):
    r'\d+'
    print(t)
    return t


def t_DEC(t):
    r'decrement|decrease|reduce|decrementing|decremental|decremented'
    print(t)
    return t
def t_INC(t):
    r'increment|increase|incrementing|incremental|incremented'
    print(t)
    return t

def t_FOR(t):
    r'for\sloop|for'
    print(t)
    return  t
def t_START(t):
    r'start|begin|beginning|starting'
    print(t)
    return  t

def t_END(t):
    r'end'
    print(t)
    return  t
def t_EQ(t):
    r'equal(s)?|='
    print(t)
    return t
def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    print(t)
    return t

def t_newline(t):
    r'\n+'
    print t
    t.lexer.lineno += t.value.count("\n")

def t_skip(t):
    r'.'
    print(t)

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
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v+"\r")
    print("int " + v + ";\nfor(" + v + "=0;" + v + "<" + str(p[2]).split(" ")[0] + ";" + v + "++)\n{\n}\n")
    f.close()


def p_statement_rule3(p):
    'statement : FOR DEC ITER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    print("int "+v+";\nfor("+v+"=" + str(p[3]).split(" ")[0] + ";"+v+">=0;"+v+"--)\n{\n}\n")
    f.close()


def p_statement_rule4(p):
    'statement : FOR START NUMBER END NUMBER'
    #print("int i;\nfor(i="+str(p[2])+";i>0"+";i--)\n{\n}\n")
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    if int(p[3])<=int(p[5]):
        print("int "+v+";\nfor("+v+"="+str(p[3])+";"+v+"<=" + str(p[5]) + ";"+v+"++)\n{\n}\n")
    else:
        print("int "+v+";\nfor("+v+"=" + str(p[3]) + ";"+v+">=" + str(p[5]) + ";"+v+"--)\n{\n}\n")
    f.close()

def p_statement_rule5(p):
    'statement : DEC ITER FOR'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    print("int " + v + ";\nfor(" + v + "=" + str(p[2]).split(" ")[0] + ";" + v + ">=0;" + v + "--)\n{\n}\n")
    f.close()

def p_statement_rule6(p):
    'statement : INC ITER FOR'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    print("int " + v + ";\nfor(" + v + "=0;" + v + "<" + str(p[2]).split(" ")[0] + ";" + v + "++)\n{\n}\n")
    f.close()

def p_statement_rule7(p):
    'statement : FOR NUMBER NUMBER'
    #print("int i;\nfor(i="+str(p[2])+";i>0"+";i--)\n{\n}\n")
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    if int(p[2])<=int(p[3]):
        print("int " + v + ";\nfor(" + v + "=" + str(p[2]) + ";" + v + "<=" + str(p[3]) + ";" + v + "++)\n{\n}\n")
    else:
        print("int " + v + ";\nfor(" + v + "=" + str(p[2]) + ";" + v + ">=" + str(p[3]) + ";" + v + "--)\n{\n}\n")
    f.close()

def p_statement_rule8(p):
    'statement : FOR INC ITER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    print("int " + v + ";\nfor(" + v + "=0;" + v + "<" + str(p[3]).split(" ")[0] + ";" + v + "++)\n{\n}\n")
    f.close()

def p_statement_rule9(p):
    'statement : FOR VAR EQ NUMBER NUMBER'
    if int(p[4])<=int(p[5]):
        print("int " + p[2] + ";\nfor(" + p[2] + "=" + p[4] + ";" + p[2] + "<" + p[5] + ";" + p[2] + "++)\n{\n}\n")
    else:
        print("int " + p[2] + ";\nfor(" + p[2] + "=" + p[4] + ";" + p[2] + ">=" + p[5] + ";" + p[2] + "--)\n{\n}\n")

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
s = raw_input()
#print(s)
s.encode('UTF-8')
#print(s)
infun(s)
'''while 1:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)'''
