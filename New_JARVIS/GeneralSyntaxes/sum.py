tokens = (
    'ADD','VAR','NUMBER'
)


# Tokens

#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_ADD(t):
    r'add|sum'
    return t
def t_VAR(t):
    r'[a-zA-Z][^ ]*'

    return t
def t_NUMBER(t):
    r'(\+)?(\-)?\d+((.)\d+)?'

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
    'statement : VAR ADD VAR'
    print(str(p[1])+"+"+str(p[3]))
def p_statement_rule2(p):
    'statement : VAR ADD NUMBER'
    print(str(p[1])+"+"+str(p[3]))
def p_statement_rule3(p):
    'statement : NUMBER ADD VAR'
    print(str(p[1])+"+"+str(p[3]))
def p_statement_rule4(p):
    'statement : NUMBER ADD NUMBER'
    print(str(p[1])+"+"+str(p[3]))
def p_statement_rule5(p):
    'statement : ADD VAR VAR'
    print(str(p[2])+"+"+str(p[3]))
def p_statement_rule6(p):
    'statement : ADD VAR NUMBER'
    print(str(p[2])+"+"+str(p[3]))
def p_statement_rule7(p):
    'statement : ADD NUMBER VAR'
    print(str(p[2])+"+"+str(p[3]))
def p_statement_rule8(p):
    'statement : ADD NUMBER NUMBER'
    print(str(p[2])+"+"+str(p[3]))


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