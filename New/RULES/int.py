tokens = (
     'INT','SIGNEDINT','UNSIGNEDINT','VAR','EQUALS','NUMBER','SIGNEDNUMBER','SHORTINT','LONGINT','SHORTSIGNEDINT','SHORTUNSIGNEDINT','LONGSIGNEDINT','LONGUNSIGNEDINT'
)


# Tokens
#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+'
    return t
def t_SIGNEDNUMBER(t):
    r'(-)\d+|(\+)\d+'
    return t

def t_INT(t):
    r'declare\sa(n)?\sint(eger)?|create\sa(n)?\sint(eger)?|int(eger)?'
    return t

def t_SIGNEDINT(t):
    r'declare\sa(n)?\ssigned\sint(eger)?|create\sa(n)?\ssigned\sint(eger)?|signed\sint(eger)?'
    return t

def t_UNSIGNEDINT(t):
    r'declare\sa(n)?\sunsigned\sint(eger)?|create\sa(n)?\sunsigned\sint(eger)?|unsigned\sint(eger)?'
    return t

def t_SHORTINT(t):
    r'declare\sa(n)?\sshort\sint(eger)?|create\sa(n)?\sshort\sint(eger)?|short\sint(eger)?'
    return t
def t_LONGINT(t):
    r'declare\sa(n)?\slong\sint(eger)?|create\sa(n)?\slong\sint(eger)?|long\sint(eger)?'
    return t

def t_SHORTSIGNEDINT(t):
    r'declare\sa(n)?\sshort\ssign(ed)?\sint(eger)?|declare\sa(n)?\ssign(ed)?\sshort\sint(eger)?|create\sa(n)?\sshort\ssign(ed)?\sint(eger)?|create\sa(n)?\ssign(ed)?\sshort\sint(eger)?|short\ssign(ed)?\sint(eger)?|sign(ed)?short\sint(eger)?'
    return t
def t_SHORTUNSIGNEDINT(t):
    r'declare\sa(n)?\sshort\sunsign(ed)?\sint(eger)?|declare\sa(n)?\sunsign(ed)?\sshort\sint(eger)?|create\sa(n)?\sshort\sunsign(ed)?\sint(eger)?|create\sa(n)?\sunsign(ed)?\sshort\sint(eger)?|short\sunsign(ed)?\sint(eger)?|unsign(ed)?short\sint(eger)?'

    return t

def t_LONGSIGNEDINT(t):
    r'declare\sa(n)?\slong\ssign(ed)?\sint(eger)?|declare\sa(n)?\ssign(ed)?\slong\sint(eger)?|create\sa(n)?\slong\ssign(ed)?\sint(eger)?|create\sa(n)?\ssign(ed)?\slong\sint(eger)?|long\ssign(ed)?\sint(eger)?|sign(ed)?long\sint(eger)?'
    return t
def t_LONGUNSIGNEDINT(t):
    r'declare\sa(n)?\slong\sunsign(ed)?\sint(eger)?|declare\sa(n)?\sunsign(ed)?\slong\sint(eger)?|create\sa(n)?\slong\sunsign(ed)?\sint(eger)?|create\sa(n)?\sunsign(ed)?\slong\sint(eger)?|long\sunsign(ed)?\sint(eger)?|unsign(ed)?long\sint(eger)?'
    return t

def t_EQUALS(t):
    r'equals\sto|equal\sto|equal(s)?|='
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
    'statement : INT'
    print("int a=0;")
def p_statement_rule2(p):
    'statement : SIGNEDINT'
    print("signed int a=0;")
def p_statement_rule3(p):
    'statement : UNSIGNEDINT'
    print("unsigned int a=0;")

def p_statement_rule4(p):
    'statement : SHORTINT'
    print("short int a=0;")

def p_statement_rule5(p):
    'statement : SHORTSIGNEDINT'
    print("signed short int a=0;")
def p_statement_rule6(p):
    'statement : SHORTUNSIGNEDINT'
    print("unsigned short int a=0;")

def p_statement_rule7(p):
    'statement : LONGINT'
    print("long int a=0;")

def p_statement_rule8(p):
    'statement : LONGSIGNEDINT'
    print("signed long int a=0;")
def p_statement_rule9(p):
    'statement : LONGUNSIGNEDINT'
    print("unsigned long int a=0;")


def p_statement_rule10(p):
    'statement : INT VAR'
    print("int "+str(p[2])+"=0;")
def p_statement_rule11(p):
    'statement : SIGNEDINT VAR'
    print("signed int "+str(p[2])+"=0;")
def p_statement_rule12(p):
    'statement : UNSIGNEDINT VAR'
    print("unsigned int "+str(p[2])+"=0;")

def p_statement_rule13(p):
    'statement : SHORTINT VAR'
    print("short int "+str(p[2])+"=0;")

def p_statement_rule14(p):
    'statement : SHORTSIGNEDINT VAR'
    print("signed short int "+str(p[2])+"=0;")
def p_statement_rule15(p):
    'statement : SHORTUNSIGNEDINT VAR'
    print("unsigned short int "+str(p[2])+"=0;")

def p_statement_rule16(p):
    'statement : LONGINT VAR'
    print("long int "+str(p[2])+"=0;")

def p_statement_rule17(p):
    'statement : LONGSIGNEDINT VAR'
    print("signed long int "+str(p[2])+"=0;")
def p_statement_rule18(p):
    'statement : LONGUNSIGNEDINT VAR'
    print("unsigned long int "+str(p[2])+"=0;")




def p_statement_rule19(p):
    'statement : INT VAR EQUALS NUMBER'
    print("int "+str(p[2])+"="+str(p[4])+";")
def p_statement_rule20(p):
    'statement : INT VAR EQUALS SIGNEDNUMBER'
    print("int "+str(p[2])+"="+str(p[4])[1:]+";")
def p_statement_rule21(p):
    'statement : SIGNEDINT VAR EQUALS NUMBER'
    print("signed int "+str(p[2])+"="+str(p[4])+";")

def p_statement_rule22(p):
    'statement : SIGNEDINT VAR EQUALS SIGNEDNUMBER'
    print("signed int "+str(p[2])+"="+str(p[4])+";")
def p_statement_rule23(p):
    'statement : UNSIGNEDINT VAR EQUALS NUMBER'
    print("unsigned int "+str(p[2])+"="+str(p[4])+";")

def p_statement_rule24(p):
    'statement : UNSIGNEDINT VAR EQUALS SIGNEDNUMBER'
    print("unsigned int "+str(p[2])+"="+str(p[4])[1:]+";")


def p_statement_rule26(p):
    'statement : SHORTSIGNEDINT VAR EQUALS NUMBER'
    print("signed short int "+str(p[2])+"="+str(p[4])+";")

def p_statement_rule27(p):
    'statement : SHORTSIGNEDINT VAR EQUALS SIGNEDNUMBER'
    print("signed short int "+str(p[2])+"="+str(p[4])+";")



def p_statement_rule28(p):
    'statement : SHORTUNSIGNEDINT VAR EQUALS NUMBER'
    print("unsigned short int "+str(p[2])+"="+str(p[4])+";")

def p_statement_rule29(p):
    'statement : SHORTUNSIGNEDINT VAR EQUALS SIGNEDNUMBER'
    print("unsigned short int "+str(p[2])+"="+str(p[4])[1:]+";")



def p_statement_rule30(p):
    'statement : LONGSIGNEDINT VAR EQUALS NUMBER'
    print("signed long int "+str(p[2])+"="+str(p[4])+";")

def p_statement_rule31(p):
    'statement : LONGSIGNEDINT VAR EQUALS SIGNEDNUMBER'
    print("signed long int "+str(p[2])+"="+str(p[4])+";")



def p_statement_rule32(p):
    'statement : LONGUNSIGNEDINT VAR EQUALS NUMBER'
    print("unsigned long int "+str(p[2])+"="+str(p[4])+";")

def p_statement_rule33(p):
    'statement : LONGUNSIGNEDINT VAR EQUALS SIGNEDNUMBER'
    print("unsigned long int "+str(p[2])+"="+str(p[4])[1:]+";")

def p_statement_rule34(p):
    'statement : SHORTINT VAR EQUALS NUMBER'
    print("short int "+str(p[2])+"="+str(p[4])+";")

def p_statement_rule35(p):
    'statement : SHORTINT VAR EQUALS SIGNEDNUMBER'
    print("short int "+str(p[2])+"="+str(p[4])+";")


def p_statement_rule36(p):
    'statement : LONGINT VAR EQUALS NUMBER'
    print("long int "+str(p[2])+"="+str(p[4])+";")

def p_statement_rule37(p):
    'statement : LONGINT VAR EQUALS SIGNEDNUMBER'
    print("long int "+str(p[2])+"="+str(p[4])+";")


    
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

