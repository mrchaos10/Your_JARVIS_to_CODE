tokens = (
    'NUMBER', 'VAR','EQ','COMPARE','GT','LT','GE','LE','NE'
)


# Tokens

#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_NUMBER(t):
    r'(-)?\d+((.)\d+)?'
    return t



def t_GE(t):
    r'great(er)?\sequal(s)?|great(er)?\sthan\sequal(s)?\sto|great(er)?\sthan\sequal(s)?|great(er)?\sequal(s)?|loosely\sgreat(er)?|>='
    return  t

def t_LE(t):
    r'less(er)?\sequal(s)?|less(er)?\sthan\sequal(s)?\sto|less(er)?\sthan\sequal(s)?|less(er)?\sequal(s)?|loosely\sless(er)?|<='
    return  t

def t_EQ(t):
    r'equal(s)?|==|='
    #print(t)
    return t

def t_COMPARE(t):
    r'comparing|compare|compared|compared\sto|compared\swith|check|where'

    return t



def t_GT(t):
    r'great(er)?\sthan|great(er)?|simply\sgreat(er)?\s(than)?|strictly\sgreat(er)?\s(than)?|>'
    return  t

def t_LT(t):
    r'less(er)?\sthan|less(er)?|simply\sless(er)?\s(than)?|strictly\sless(er)?(than)?|<'
    return  t

def t_NE(t):
    r'not\sequal(s)?\s(to)?'
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
    'statement : COMPARE VAR VAR'
    print(str(p[2])+"<"+str(p[3]))


def p_statement_rule2(p):
    'statement : COMPARE VAR EQ VAR'
    print("if("+str(p[2])+"=="+str(p[4])+")\n{\n}\n")


def p_statement_rule3(p):
    'statement : COMPARE VAR GE VAR'
    print("if("+str(p[2])+">="+str(p[4])+")\n{\n}\n")



def p_statement_rule4(p):
    'statement : COMPARE VAR LE VAR'
    print("if("+str(p[2])+"<="+str(p[4])+")\n{\n}\n")


def p_statement_rule5(p):
    'statement : COMPARE VAR GT VAR'
    print("if("+str(p[2])+">"+str(p[4])+")\n{\n}\n")



def p_statement_rule6(p):
    'statement : COMPARE VAR LT VAR'
    print("if("+str(p[2])+"<"+str(p[4])+")\n{\n}\n")



def p_statement_rule7(p):
    'statement : COMPARE VAR EQ NUMBER'
    print("if("+str(p[2])+"=="+str(p[4])+")\n{\n}\n")



def p_statement_rule8(p):
    'statement : COMPARE VAR GE NUMBER'
    print("if("+str(p[2])+">="+str(p[4])+")\n{\n}\n")



def p_statement_rule9(p):
    'statement : COMPARE VAR LE NUMBER'
    print("if("+str(p[2])+"<="+str(p[4])+")\n{\n}\n")




def p_statement_rule10(p):
    'statement : COMPARE VAR GT NUMBER'
    print("if("+str(p[2])+">"+str(p[4])+")\n{\n}\n")



def p_statement_rule11(p):
    'statement : COMPARE VAR LT NUMBER'
    print("if("+str(p[2])+"<"+str(p[4])+")\n{\n}\n")


def p_statement_rule12(p):
    'statement : COMPARE NUMBER EQ NUMBER'
    print("if("+str(p[2])+"=="+str(p[4])+")\n{\n}\n")



def p_statement_rule13(p):
    'statement : COMPARE NUMBER GE NUMBER'
    print("if("+str(p[2])+">="+str(p[4])+")\n{\n}\n")



def p_statement_rule14(p):
    'statement : COMPARE NUMBER LE NUMBER'
    print("if("+str(p[2])+"<="+str(p[4])+")\n{\n}\n")

def p_statement_rule15(p):
    'statement : COMPARE NUMBER GT NUMBER'
    print("if("+str(p[2])+">"+str(p[4])+")\n{\n}\n")

def p_statement_rule16(p):
    'statement : COMPARE NUMBER LT NUMBER'
    print("if("+str(p[2])+"<"+str(p[4])+")\n{\n}\n")





def p_statement_rule17(p):
    'statement : COMPARE NUMBER EQ VAR'
    print("if("+str(p[2])+"=="+str(p[4])+")\n{\n}\n")



def p_statement_rule18(p):
    'statement : COMPARE NUMBER GE VAR'
    print("if("+str(p[2])+">="+str(p[4])+")\n{\n}\n")


def p_statement_rule19(p):
    'statement : COMPARE NUMBER LE VAR'
    print("if("+str(p[2])+"<="+str(p[4])+")\n{\n}\n")



def p_statement_rule20(p):
    'statement : COMPARE NUMBER GT VAR'
    print("if("+str(p[2])+">"+str(p[4])+")\n{\n}\n")


def p_statement_rule21(p):
    'statement : COMPARE NUMBER LT VAR'
    print("if("+str(p[2])+"<"+str(p[4])+")\n{\n}\n")


def p_statement_rule22(p):
    'statement : COMPARE NUMBER NE VAR'
    print("if("+str(p[2])+"!="+str(p[4])+")\n{\n}\n")

def p_statement_rule23(p):
    'statement : COMPARE NUMBER NE NUMBER'
    print("if("+str(p[2])+"!="+str(p[4])+")\n{\n}\n")

def p_statement_rule24(p):
    'statement : COMPARE VAR NE VAR'
    print("if("+str(p[2])+"!="+str(p[4])+")\n{\n}\n")

def p_statement_rule25(p):
    'statement : COMPARE VAR NE NUMBER'
    print("if("+str(p[2])+"!="+str(p[4])+")\n{\n}\n")

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

def inputfunction(s1):
    yacc.parse(s1)

s = input()
s.encode('UTF-8')
inputfunction(s)
