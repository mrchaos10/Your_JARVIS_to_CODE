tokens = (
     'ELSE','NUMBER','ELSEIF','VAR','EQ','COMPARE','GT','LT','GE','LE'
)


# Tokens
#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'(-)?\d+'
    return t


def t_ELSEIF(t):
    r'else\sif|else\sif\s(for\s)?above\sstatement|else\sif\s(for\s)?above\sif\sstatement|else\sif\sblock|(put\san\s)?else\sif\sblock|(create\san\s)?else\sif\sblock'
    print(t)
    return t

def t_COMPARE(t):
    r'comparing|compare|compared|compared\sto|compared\swith|check|where'
    return t

def t_GE(t):
    r'great(er)?\sthan\sequal(s)?\sto|great(er)?\sthan\sequal(s)?|great(er)?\sequal(s)?|loosely\sgreat(er)?|>='
    #print(t)
    return  t

def t_LE(t):
    r'less(er)?\sthan\sequal(s)?\sto|less(er)?\sthan\sequal(s)?|less(er)?\sequal(s)?|loosely\sless(er)?|<='
    print(t)
    return  t

def t_EQ(t):
    r'equal(s)?|=='
    #print(t)
    return t





def t_GT(t):
    r'great(er)?\sthan|great(er)?|simply\sgreat(er)?\s(than)?|strictly\sgreat(er)?\s(than)?|>'
    return  t

def t_LT(t):
    r'less(er)?\sthan|less(er)?|simply\sless(er)?\s(than)?|strictly\sless(er)?(than)?|<'
    return  t



def t_ELSE(t):
    r'else|else\s(for\s)?above\sstatement|else\s(for\s)?above\sif\sstatement|else\sblock|(put\san\s)?else\sblock'
    print(t)
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
    'statement : ELSE'
    print("else()\n{\n}\n")
def p_statement_rule2(p):
    'statement : ELSEIF'
    print("else if()\n{\n}\n")

def p_statement_rule3(p):
    'statement : ELSEIF COMPARE VAR EQ VAR'
    print("else if("+str(p[3])+"=="+str(p[5])+")\n{\n}\n")

def p_statement_rule4(p):
    'statement : ELSEIF COMPARE VAR GE VAR'
    print("else if("+str(p[3])+">="+str(p[5])+")\n{\n}\n")

def p_statement_rule5(p):
    'statement : ELSEIF COMPARE VAR LE VAR'
    print("else if("+str(p[3])+"<="+str(p[5])+")\n{\n}\n")

def p_statement_rule6(p):
    'statement : ELSEIF COMPARE VAR GT VAR'
    print("else if("+str(p[3])+">"+str(p[5])+")\n{\n}\n")

def p_statement_rule7(p):
    'statement : ELSEIF COMPARE VAR LT VAR'
    print("else if("+str(p[3])+"<"+str(p[5])+")\n{\n}\n")

def p_statement_rule8(p):
    'statement : ELSEIF COMPARE VAR EQ NUMBER'
    print("else if("+str(p[3])+"=="+str(p[5])+")\n{\n}\n")

def p_statement_rule9(p):
    'statement : ELSEIF COMPARE VAR GE NUMBER'
    print("else if("+str(p[3])+">="+str(p[5])+")\n{\n}\n")

def p_statement_rule10(p):
    'statement : ELSEIF COMPARE VAR LE NUMBER'
    print("else if("+str(p[3])+"<="+str(p[5])+")\n{\n}\n")

def p_statement_rule11(p):
    'statement : ELSEIF COMPARE VAR GT NUMBER'
    print("else if("+str(p[3])+">"+str(p[5])+")\n{\n}\n")

def p_statement_rule12(p):
    'statement : ELSEIF COMPARE VAR LT NUMBER'
    print("else if("+str(p[3])+"<"+str(p[5])+")\n{\n}\n")

def p_statement_rule13(p):
    'statement : ELSEIF COMPARE NUMBER EQ NUMBER'
    print("else if("+str(p[3])+"=="+str(p[5])+")\n{\n}\n")

def p_statement_rule14(p):
    'statement : ELSEIF COMPARE NUMBER GE NUMBER'
    print("else if("+str(p[3])+">="+str(p[5])+")\n{\n}\n")

def p_statement_rule15(p):
    'statement : ELSEIF COMPARE NUMBER LE NUMBER'
    print("else if("+str(p[3])+"<="+str(p[5])+")\n{\n}\n")

def p_statement_rule16(p):
    'statement : ELSEIF COMPARE NUMBER GT NUMBER'
    print("else if("+str(p[3])+">"+str(p[5])+")\n{\n}\n")

def p_statement_rule17(p):
    'statement : ELSEIF COMPARE NUMBER LT NUMBER'
    print("else if("+str(p[3])+"<"+str(p[5])+")\n{\n}\n")

def p_statement_rule18(p):
    'statement : ELSEIF COMPARE NUMBER EQ VAR'
    print("else if("+str(p[3])+"=="+str(p[5])+")\n{\n}\n")

def p_statement_rule19(p):
    'statement : ELSEIF COMPARE NUMBER GE VAR'
    print("else if("+str(p[3])+">="+str(p[5])+")\n{\n}\n")

def p_statement_rule20(p):
    'statement : ELSEIF COMPARE NUMBER LE VAR'
    print("else if("+str(p[3])+"<="+str(p[5])+")\n{\n}\n")

def p_statement_rule21(p):
    'statement : ELSEIF COMPARE NUMBER GT VAR'
    print("else if("+str(p[3])+">"+str(p[5])+")\n{\n}\n")

def p_statement_rule22(p):
    'statement : ELSEIF COMPARE NUMBER LT VAR'
    print("else if("+str(p[3])+"<"+str(p[5])+")\n{\n}\n")


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

