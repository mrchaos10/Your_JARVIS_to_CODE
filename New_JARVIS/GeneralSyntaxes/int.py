tokens = (
    'INT', 'SIGNEDINT', 'UNSIGNEDINT', 'VAR', 'EQUALS', 'NUMBER', 'SIGNEDNUMBER', 'SHORTINT', 'LONGINT',
    'SHORTSIGNEDINT', 'SHORTUNSIGNEDINT', 'LONGSIGNEDINT', 'LONGUNSIGNEDINT'
)


# Tokens
# t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_SIGNEDNUMBER(t):
    r'(-)\d+|(\+)\d+'
    return t
def t_NUMBER(t):
    r'\d+'
    return t





def t_INT(t):
    r'declare\s(a(n)?\s)?int(eger)?|create\s(a(n)?\s)?int(eger)?|int(eger)?'
    return t


def t_SIGNEDINT(t):
    r'declare\s(a(n)?\s)?signed\sint(eger)?|create\s(a(n)?\s)?signed\sint(eger)?|signed\sint(eger)?'
    return t


def t_UNSIGNEDINT(t):
    r'declare\s(a(n)?\s)?unsigned\sint(eger)?|create\s(a(n)?\s)?unsigned\sint(eger)?|unsigned\sint(eger)?'
    return t


def t_SHORTINT(t):
    r'declare\s(a(n)?\s)?short\sint(eger)?|create\s(a(n)?\s)?short\sint(eger)?|short\sint(eger)?'
    return t


def t_LONGINT(t):
    r'declare\s(a(n)?\s)?long\sint(eger)?|create\s(a(n)?\s)?long\sint(eger)?|long\sint(eger)?'
    return t


def t_SHORTSIGNEDINT(t):
    r'declare\s(a(n)?\s)?short\ssign(ed)?\sint(eger)?|declare\s(a(n)?\s)?sign(ed)?\sshort\sint(eger)?|create\sa(n)?\sshort\ssign(ed)?\sint(eger)?|create\sa(n)?\ssign(ed)?\sshort\sint(eger)?|short\ssign(ed)?\sint(eger)?|sign(ed)?short\sint(eger)?'
    return t


def t_SHORTUNSIGNEDINT(t):
    r'declare\s(a(n)?\s)?short\sunsign(ed)?\sint(eger)?|declare\s(a(n)?\s)?unsign(ed)?\sshort\sint(eger)?|create\s(a(n)?\s)?short\sunsign(ed)?\sint(eger)?|create\s(a(n)?\s)?unsign(ed)?\sshort\sint(eger)?|short\sunsign(ed)?\sint(eger)?|unsign(ed)?short\sint(eger)?'

    return t


def t_LONGSIGNEDINT(t):
    r'declare\s(a(n)?\s)?long\ssign(ed)?\sint(eger)?|declare\s(a(n)?\s)?sign(ed)?\slong\sint(eger)?|create\s(a(n)?\s)?long\ssign(ed)?\sint(eger)?|create\s(a(n)?\s)?sign(ed)?\slong\sint(eger)?|long\ssign(ed)?\sint(eger)?|sign(ed)?long\sint(eger)?'
    return t


def t_LONGUNSIGNEDINT(t):
    r'declare\s(a(n)?\s)?long\sunsign(ed)?\sint(eger)?|declare\s(a(n)?\s)?unsign(ed)?\slong\sint(eger)?|create\s(a(n)?\s)?long\sunsign(ed)?\sint(eger)?|create\s(a(n)?\s)?unsign(ed)?\slong\sint(eger)?|long\sunsign(ed)?\sint(eger)?|unsign(ed)?long\sint(eger)?'
    return t


def t_EQUALS(t):
    r'equals\sto|equal\sto|equal(s)?|='
    # print(t)
    return t


def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    # print(t)
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
# names = {}
def p_statement_rule1(p):
    'statement : INT'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d "+v+"\r")
    print("int "+v+" =0;")


def p_statement_rule2(p):
    'statement : SIGNEDINT'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + v + "\r")
    print("signed int "+v+" =0;")


def p_statement_rule3(p):
    'statement : UNSIGNEDINT'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + v + "\r")
    print("unsigned int "+v+" =0;")


def p_statement_rule4(p):
    'statement : SHORTINT'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + v + "\r")
    print("short int "+v+" =0;")


def p_statement_rule5(p):
    'statement : SHORTSIGNEDINT'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + v + "\r")
    print("signed short int "+v+" =0;")


def p_statement_rule6(p):
    'statement : SHORTUNSIGNEDINT'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + v + "\r")
    print("unsigned short int "+v+" =0;")


def p_statement_rule7(p):
    'statement : LONGINT'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + v + "\r")
    print("long int "+v+"=0;")


def p_statement_rule8(p):
    'statement : LONGSIGNEDINT'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + v + "\r")
    print("signed long int "+v+" =0;")


def p_statement_rule9(p):
    'statement : LONGUNSIGNEDINT'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    v = getVar()
    f.write(v + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + v + "\r")
    print("unsigned long int "+v+" =0;")


def p_statement_rule10(p):
    'statement : INT VAR'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("int " + str(p[2]) + "=0;")


def p_statement_rule11(p):
    'statement : SIGNEDINT VAR'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("signed int " + str(p[2]) + "=0;")


def p_statement_rule12(p):
    'statement : UNSIGNEDINT VAR'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("unsigned int " + str(p[2]) + "=0;")


def p_statement_rule13(p):
    'statement : SHORTINT VAR'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("short int " + str(p[2]) + "=0;")


def p_statement_rule14(p):
    'statement : SHORTSIGNEDINT VAR'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("signed short int " + str(p[2]) + "=0;")


def p_statement_rule15(p):
    'statement : SHORTUNSIGNEDINT VAR'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("unsigned short int " + str(p[2]) + "=0;")


def p_statement_rule16(p):
    'statement : LONGINT VAR'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("long int " + str(p[2]) + "=0;")


def p_statement_rule17(p):
    'statement : LONGSIGNEDINT VAR'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("signed long int " + str(p[2]) + "=0;")


def p_statement_rule18(p):
    'statement : LONGUNSIGNEDINT VAR'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("unsigned long int " + str(p[2]) + "=0;")


def p_statement_rule19(p):
    'statement : INT VAR EQUALS NUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule20(p):
    'statement : INT VAR EQUALS SIGNEDNUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("int " + str(p[2]) + "=" + str(p[4])[1:] + ";")


def p_statement_rule21(p):
    'statement : SIGNEDINT VAR EQUALS NUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("signed int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule22(p):
    'statement : SIGNEDINT VAR EQUALS SIGNEDNUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("signed int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule23(p):
    'statement : UNSIGNEDINT VAR EQUALS NUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("unsigned int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule24(p):
    'statement : UNSIGNEDINT VAR EQUALS SIGNEDNUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("unsigned int " + str(p[2]) + "=" + str(p[4])[1:] + ";")


def p_statement_rule26(p):
    'statement : SHORTSIGNEDINT VAR EQUALS NUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("signed short int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule27(p):
    'statement : SHORTSIGNEDINT VAR EQUALS SIGNEDNUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("signed short int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule28(p):
    'statement : SHORTUNSIGNEDINT VAR EQUALS NUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("unsigned short int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule29(p):
    'statement : SHORTUNSIGNEDINT VAR EQUALS SIGNEDNUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("unsigned short int " + str(p[2]) + "=" + str(p[4])[1:] + ";")


def p_statement_rule30(p):
    'statement : LONGSIGNEDINT VAR EQUALS NUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("signed long int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule31(p):
    'statement : LONGSIGNEDINT VAR EQUALS SIGNEDNUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("signed long int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule32(p):
    'statement : LONGUNSIGNEDINT VAR EQUALS NUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("unsigned long int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule33(p):
    'statement : LONGUNSIGNEDINT VAR EQUALS SIGNEDNUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("unsigned long int " + str(p[2]) + "=" + str(p[4])[1:] + ";")


def p_statement_rule34(p):
    'statement : SHORTINT VAR EQUALS NUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("short int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule35(p):
    'statement : SHORTINT VAR EQUALS SIGNEDNUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("short int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule36(p):
    'statement : LONGINT VAR EQUALS NUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("long int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_statement_rule37(p):
    'statement : LONGINT VAR EQUALS SIGNEDNUMBER'
    f = open("E:\\codecompleter1\\SymbolTable.txt", "a")
    f.write(p[2] + "\r")
    f1 = open("E:\\codecompleter1\\ST.txt", "a")
    f1.write("%d " + p[2] + "\r")
    print("long int " + str(p[2]) + "=" + str(p[4]) + ";")


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


import ply.yacc as yacc

yacc.yacc()

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
def inputfunction(s1):
    yacc.parse(s1)


s = input()
s.encode('UTF-8')
inputfunction(s)
