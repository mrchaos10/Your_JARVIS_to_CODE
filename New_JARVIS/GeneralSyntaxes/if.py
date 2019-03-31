tokens = (
    'NUMBER', 'IF', 'VAR','EQ','COMPARE','GT','LT','GE','LE','NE'
)


# Tokens

#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
def t_NUMBER(t):
    r'(-)?\d+((.)\d+)?'
    return t


def t_IF(t):
    r'if|if\sblock'
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
    'statement : IF'
    print("if()\n{\n}\n")

def p_statement_rule2(p):
    'statement : IF COMPARE VAR EQ VAR'
    print("if("+str(p[3])+"=="+str(p[5])+")\n{\n}\n")
def p_statement_rule22(p):
    'statement : COMPARE VAR EQ VAR'
    print("if("+str(p[2])+"=="+str(p[4])+")\n{\n}\n")
def p_statement_rule23(p):
    'statement : IF VAR EQ VAR'
    print("if("+str(p[2])+"=="+str(p[4])+")\n{\n}\n")

def p_statement_rule3(p):
    'statement : IF COMPARE VAR GE VAR'
    print("if("+str(p[3])+">="+str(p[5])+")\n{\n}\n")
def p_statement_rule24(p):
    'statement : COMPARE VAR GE VAR'
    print("if("+str(p[2])+">="+str(p[4])+")\n{\n}\n")
def p_statement_rule25(p):
    'statement : IF VAR GE VAR'
    print("if("+str(p[2])+">="+str(p[4])+")\n{\n}\n")

def p_statement_rule4(p):
    'statement : IF COMPARE VAR LE VAR'
    print("if("+str(p[3])+"<="+str(p[5])+")\n{\n}\n")
def p_statement_rule26(p):
    'statement : COMPARE VAR LE VAR'
    print("if("+str(p[2])+"<="+str(p[4])+")\n{\n}\n")
def p_statement_rule27(p):
    'statement : IF VAR LE VAR'
    print("if("+str(p[2])+"<="+str(p[4])+")\n{\n}\n")

def p_statement_rule5(p):
    'statement : IF COMPARE VAR GT VAR'
    print("if("+str(p[3])+">"+str(p[5])+")\n{\n}\n")
def p_statement_rule28(p):
    'statement : COMPARE VAR GT VAR'
    print("if("+str(p[2])+">"+str(p[4])+")\n{\n}\n")
def p_statement_rule29(p):
    'statement : IF VAR GT VAR'
    print("if("+str(p[2])+">"+str(p[4])+")\n{\n}\n")

def p_statement_rule6(p):
    'statement : IF COMPARE VAR LT VAR'
    print("if("+str(p[3])+"<"+str(p[5])+")\n{\n}\n")
def p_statement_rule30(p):
    'statement : COMPARE VAR LT VAR'
    print("if("+str(p[2])+"<"+str(p[4])+")\n{\n}\n")
def p_statement_rule31(p):
    'statement : IF VAR LT VAR'
    print("if("+str(p[2])+"<"+str(p[4])+")\n{\n}\n")

def p_statement_rule7(p):
    'statement : IF COMPARE VAR EQ NUMBER'
    print("if("+str(p[3])+"=="+str(p[5])+")\n{\n}\n")
def p_statement_rule32(p):
    'statement : COMPARE VAR EQ NUMBER'
    print("if("+str(p[2])+"=="+str(p[4])+")\n{\n}\n")
def p_statement_rule33(p):
    'statement : IF VAR EQ NUMBER'
    print("if("+str(p[2])+"=="+str(p[4])+")\n{\n}\n")

def p_statement_rule8(p):
    'statement : IF COMPARE VAR GE NUMBER'
    print("if("+str(p[3])+">="+str(p[5])+")\n{\n}\n")

def p_statement_rule34(p):
    'statement : COMPARE VAR GE NUMBER'
    print("if("+str(p[2])+">="+str(p[4])+")\n{\n}\n")
def p_statement_rule35(p):
    'statement : IF VAR GE NUMBER'
    print("if("+str(p[2])+">="+str(p[4])+")\n{\n}\n")
def p_statement_rule9(p):
    'statement : IF COMPARE VAR LE NUMBER'
    print("if("+str(p[3])+"<="+str(p[5])+")\n{\n}\n")

def p_statement_rule36(p):
    'statement : COMPARE VAR LE NUMBER'
    print("if("+str(p[2])+"<="+str(p[4])+")\n{\n}\n")
def p_statement_rule37(p):
    'statement : IF VAR LE NUMBER'
    print("if("+str(p[2])+"<="+str(p[4])+")\n{\n}\n")

def p_statement_rule10(p):
    'statement : IF COMPARE VAR GT NUMBER'
    print("if("+str(p[3])+">"+str(p[5])+")\n{\n}\n")

def p_statement_rule38(p):
    'statement : COMPARE VAR GT NUMBER'
    print("if("+str(p[2])+">"+str(p[4])+")\n{\n}\n")
def p_statement_rule39(p):
    'statement : IF VAR GT NUMBER'
    print("if("+str(p[2])+">"+str(p[4])+")\n{\n}\n")

def p_statement_rule11(p):
    'statement : IF COMPARE VAR LT NUMBER'
    print("if("+str(p[3])+"<"+str(p[5])+")\n{\n}\n")
def p_statement_rule40(p):
    'statement : COMPARE VAR LT NUMBER'
    print("if("+str(p[2])+"<"+str(p[4])+")\n{\n}\n")
def p_statement_rule41(p):
    'statement : IF VAR LT NUMBER'
    print("if("+str(p[2])+"<"+str(p[4])+")\n{\n}\n")

def p_statement_rule12(p):
    'statement : IF COMPARE NUMBER EQ NUMBER'
    print("if("+str(p[3])+"=="+str(p[5])+")\n{\n}\n")
def p_statement_rule42(p):
    'statement : COMPARE NUMBER EQ NUMBER'
    print("if("+str(p[2])+"=="+str(p[4])+")\n{\n}\n")
def p_statement_rule43(p):
    'statement : IF NUMBER EQ NUMBER'
    print("if("+str(p[2])+"=="+str(p[4])+")\n{\n}\n")

def p_statement_rule13(p):
    'statement : IF COMPARE NUMBER GE NUMBER'
    print("if("+str(p[3])+">="+str(p[5])+")\n{\n}\n")

def p_statement_rule44(p):
    'statement : COMPARE NUMBER GE NUMBER'
    print("if("+str(p[2])+">="+str(p[4])+")\n{\n}\n")

def p_statement_rule45(p):
    'statement : IF NUMBER GE NUMBER'
    print("if("+str(p[2])+">="+str(p[4])+")\n{\n}\n")

def p_statement_rule14(p):
    'statement : IF COMPARE NUMBER LE NUMBER'
    print("if("+str(p[3])+"<="+str(p[5])+")\n{\n}\n")

def p_statement_rule46(p):
    'statement : COMPARE NUMBER LE NUMBER'
    print("if("+str(p[2])+"<="+str(p[4])+")\n{\n}\n")

def p_statement_rule47(p):
    'statement : IF NUMBER LE NUMBER'
    print("if("+str(p[2])+"<="+str(p[4])+")\n{\n}\n")
def p_statement_rule15(p):
    'statement : IF COMPARE NUMBER GT NUMBER'
    print("if("+str(p[3])+">"+str(p[5])+")\n{\n}\n")
def p_statement_rule48(p):
    'statement : COMPARE NUMBER GT NUMBER'
    print("if("+str(p[2])+">"+str(p[4])+")\n{\n}\n")
def p_statement_rule49(p):
    'statement : IF NUMBER GT NUMBER'
    print("if("+str(p[2])+">"+str(p[4])+")\n{\n}\n")

def p_statement_rule16(p):
    'statement : IF COMPARE NUMBER LT NUMBER'
    print("if("+str(p[3])+"<"+str(p[5])+")\n{\n}\n")

def p_statement_rule50(p):
    'statement : COMPARE NUMBER LT NUMBER'
    print("if("+str(p[2])+"<"+str(p[4])+")\n{\n}\n")

def p_statement_rule51(p):
    'statement : IF NUMBER LT NUMBER'
    print("if("+str(p[2])+"<"+str(p[4])+")\n{\n}\n")

def p_statement_rule17(p):
    'statement : IF COMPARE NUMBER EQ VAR'
    print("if("+str(p[3])+"=="+str(p[5])+")\n{\n}\n")

def p_statement_rule52(p):
    'statement : COMPARE NUMBER EQ VAR'
    print("if("+str(p[2])+"=="+str(p[4])+")\n{\n}\n")

def p_statement_rule53(p):
    'statement : IF NUMBER EQ VAR'
    print("if("+str(p[2])+"=="+str(p[4])+")\n{\n}\n")

def p_statement_rule18(p):
    'statement : IF COMPARE NUMBER GE VAR'
    print("if("+str(p[3])+">="+str(p[5])+")\n{\n}\n")

def p_statement_rule54(p):
    'statement : COMPARE NUMBER GE VAR'
    print("if("+str(p[2])+">="+str(p[4])+")\n{\n}\n")

def p_statement_rule55(p):
    'statement : IF NUMBER GE VAR'
    print("if("+str(p[2])+">="+str(p[4])+")\n{\n}\n")

def p_statement_rule19(p):
    'statement : IF COMPARE NUMBER LE VAR'
    print("if("+str(p[3])+"<="+str(p[5])+")\n{\n}\n")

def p_statement_rule56(p):
    'statement : COMPARE NUMBER LE VAR'
    print("if("+str(p[2])+"<="+str(p[4])+")\n{\n}\n")

def p_statement_rule57(p):
    'statement : IF NUMBER LE VAR'
    print("if("+str(p[2])+"<="+str(p[4])+")\n{\n}\n")

def p_statement_rule20(p):
    'statement : IF COMPARE NUMBER GT VAR'
    print("if("+str(p[3])+">"+str(p[5])+")\n{\n}\n")
def p_statement_rule58(p):
    'statement : COMPARE NUMBER GT VAR'
    print("if("+str(p[2])+">"+str(p[4])+")\n{\n}\n")

def p_statement_rule59(p):
    'statement : IF NUMBER GT VAR'
    print("if("+str(p[2])+">"+str(p[4])+")\n{\n}\n")

def p_statement_rule21(p):
    'statement : IF COMPARE NUMBER LT VAR'
    print("if("+str(p[3])+"<"+str(p[5])+")\n{\n}\n")
def p_statement_rule60(p):
    'statement : COMPARE NUMBER LT VAR'
    print("if("+str(p[2])+"<"+str(p[4])+")\n{\n}\n")

def p_statement_rule61(p):
    'statement : IF NUMBER LT VAR'
    print("if("+str(p[2])+"<"+str(p[4])+")\n{\n}\n")
def p_statement_rule62(p):
    'statement : IF NUMBER NE VAR'
    print("if("+str(p[2])+"!="+str(p[4])+")\n{\n}\n")
def p_statement_rule63(p):
    'statement : COMPARE NUMBER NE VAR'
    print("if("+str(p[2])+"!="+str(p[4])+")\n{\n}\n")
def p_statement_rule64(p):
    'statement : IF COMPARE NUMBER NE VAR'
    print("if("+str(p[3])+"!="+str(p[5])+")\n{\n}\n")
def p_statement_rule65(p):
    'statement : IF NUMBER NE NUMBER'
    print("if("+str(p[2])+"!="+str(p[4])+")\n{\n}\n")
def p_statement_rule66(p):
    'statement : COMPARE NUMBER NE NUMBER'
    print("if("+str(p[2])+"!="+str(p[4])+")\n{\n}\n")
def p_statement_rule67(p):
    'statement : IF COMPARE NUMBER NE NUMBER'
    print("if("+str(p[3])+"!="+str(p[5])+")\n{\n}\n")
def p_statement_rule68(p):
    'statement : IF VAR NE VAR'
    print("if("+str(p[2])+"!="+str(p[4])+")\n{\n}\n")
def p_statement_rule69(p):
    'statement : COMPARE VAR NE VAR'
    print("if("+str(p[2])+"!="+str(p[4])+")\n{\n}\n")
def p_statement_rule70(p):
    'statement : IF COMPARE VAR NE VAR'
    print("if("+str(p[3])+"!="+str(p[5])+")\n{\n}\n")
def p_statement_rule71(p):
    'statement : IF VAR NE NUMBER'
    print("if("+str(p[2])+"!="+str(p[4])+")\n{\n}\n")
def p_statement_rule72(p):
    'statement : COMPARE VAR NE NUMBER'
    print("if("+str(p[2])+"!="+str(p[4])+")\n{\n}\n")
def p_statement_rule73(p):
    'statement : IF COMPARE VAR NE NUMBER'
    print("if("+str(p[3])+"!="+str(p[5])+")\n{\n}\n")
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
