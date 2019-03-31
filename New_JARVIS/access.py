from flask import  Flask,render_template,request,Response
import flask
from nltk import pos_tag
from word2number import w2n
from subprocess import Popen,PIPE,STDOUT
import json
app = Flask(__name__)
linecountarr = []

@app.route('/')
def screen():
    return render_template('screen.html')


@app.route('/process', methods=['POST'])
def process():
    event = request.form.get('text')

    linenum = int(request.form.get('linenum'))
    if event == "space" or event==" ":
        linecountarr[linenum-1]+=1
        response = flask.jsonify({'some': " ", 'chars': linecountarr, 'linenum': linenum})
        # linecountarr.clear()
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    elif event == "open braces":
        linecountarr[linenum - 1] += 1
        response = flask.jsonify({'some': "(", 'chars': linecountarr, 'linenum': linenum})
        # linecountarr.clear()
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    elif event == "close braces":
        linecountarr[linenum - 1] += 1
        response = flask.jsonify({'some': ")", 'chars': linecountarr, 'linenum': linenum})
        # linecountarr.clear()
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    elif event=="enter":
        linecountarr.insert(linenum,1)
        response = flask.jsonify({'some': "\n", 'chars': linecountarr, 'linenum': linenum+1})
        # linecountarr.clear()
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    elif event=="semicolon":
        linecountarr[linenum - 1] += 1
        response = flask.jsonify({'some': ";", 'chars': linecountarr, 'linenum': linenum})
        # linecountarr.clear()
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    print(event)
    l1 = []
    if "\"" in event:
        l1.append("print")
        l1.append(event[6:])
    else:
        l1 = parseText(event)
    if '' in l1:
        l1.remove('')



    if 'do' in l1 and 'while' in l1:
        l1.remove('while')

    # print(l1)
    s1 = ""
    for i in l1:
        s1 += " " + str(i)

    key = retrieve_key_word(l1)
    assgn = ""
    for i in range(0,len(key)):
        if key[i] == "compare":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\if.py"
        elif key[i] == "const" or key[i]=="constant":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\const.py"
        elif  key[i] == "static":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\static.py"
        elif  key[i] == "register":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\register.py"
        elif  key[i] == "extern":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\extern.py"
        elif i != len(key) - 1 and key[i] == "else" and key[i + 1] == "if":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\elseif.py"
        elif i != len(key) - 1 and (key[i] == "signed" or key[i] == "unsigned" or key[i] == "short" or key[i] == "long"):
            if key[i + 1] == "number":
                filename = "E:\\codecompleter1\\GeneralSyntaxes\\int.py"
            elif key[i + 1] == "unsigned" or key[i + 1] == "signed" or key[i + 1] == "long" or key[i + 1] == "short":
                filename = "E:\\codecompleter1\\GeneralSyntaxes\\" + key[i + 2] + ".py"
            else:
                filename = "E:\\codecompleter1\\GeneralSyntaxes\\" + key[i + 1] + ".py"
        elif key[i]=="sum" or key[i]=="add":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\sum.py"
            s1 = s1.replace("and","")
        elif key[i]=="subtract" or key[i]=="difference":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\difference.py"
            s1 = s1.replace("and","")
        elif key[i]=="multiply" or key[i]=="product":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\multiply.py"
            s1 = s1.replace("and","")
        elif key[i]=="divide" or key[i]=="quotient":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\quotient.py"
            s1 = s1.replace("and","")
        elif key[i]=="remainder" or key[i]=="mod":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\mod.py"
            s1 = s1.replace("and","")
        elif key[i]=="minus" or key[i]=="negation" or key[i]=="negative":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\minus.py"
            s1 = s1.replace("and","")
        elif key[i] == "assign":
            k = 0
            for i in l1:
                n = []
                if i == "assign":
                    for j in range(1,len(l1)):
                        if l1[j]!="to":
                            n.append(l1[j])
                        else:
                            break
                    assgn = find(n)
                    break
            s1="assign "
            s1+=" "+str(assgn)
            s1 = s1.replace("\n","")
            k = len(n)

            for i in range(k+2,len(l1)):
                print("me")
                s1+=" "+str(l1[i])

                print(s1)
            print("assignment")
            print(k)
            print(s1)
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\assign.py"
        else:
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\" + key[i] + ".py"
        p = Popen(['python', filename], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        py_stdout = p.communicate(input=bytes(s1.encode('UTF-8')))[0]
        text = py_stdout.decode()
        print(text)
        text = text.replace("\r","")
        text = text.rstrip()
        listtext = text.split("\n")
        print(listtext)
        for i in range(0, len(listtext)):
            if 'LALR' in listtext[i]:
                del (listtext[i])
                break
        text = ""
        for i in listtext:
            text += i + "\n"
        print(text)
        # codefile = open(filename)
        # text = codefile.read()
        c = 0
        init = linenum
        for i in text:
            if i == '':
                continue
            if i != '\n':
                c = c + 1
            if i == '\n':
                if linenum != 0:
                    if init==linenum and init<=len(linecountarr):
                        if c!=0:
                            linecountarr[init-1]+=c
                            linecountarr.insert(init,1)
                            print(1)
                            linenum += 1
                    else:
                        if c!=0:
                            linecountarr.insert(linenum - 1, c+1)
                            linenum += 1
                            print(2)
                else:
                    if(c!=0):
                        linecountarr.append(c+1)
                        print(3)
                c = 0
        print("linenum")
        print(linenum)
        '''if linenum != 0:
            if init == linenum and init < len(linecountarr):
                linecountarr[init - 1] += c
                linenum += 1
                print(4)
            else:
                linecountarr.insert(linenum - 1, c)
                linenum += 1
                print(5)
        else:
            linecountarr.append(c)
            print(6)'''
        c = 0

        print(linecountarr)
        response = flask.jsonify({'some': text, 'chars': linecountarr, 'linenum': linenum})
        #linecountarr.clear()
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

def find(n):
    if len(n)==1:
        return n[0]
    s1 = ""
    for i in n:
        s1 += " " + str(i)

    key = retrieve_key_word(n)

    for i in range(0, len(key)):
        if key[i] == "compare":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\if.py"
        elif key[i] == "const" or key[i] == "constant":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\const.py"
        elif key[i] == "static":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\static.py"
        elif key[i] == "register":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\register.py"
        elif key[i] == "extern":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\extern.py"
        elif i != len(key) - 1 and key[i] == "else" and key[i + 1] == "if":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\elseif.py"
        elif i != len(key) - 1 and (
                key[i] == "signed" or key[i] == "unsigned" or key[i] == "short" or key[i] == "long"):
            if key[i + 1] == "number":
                filename = "E:\\codecompleter1\\GeneralSyntaxes\\int.py"
            elif key[i + 1] == "unsigned" or key[i + 1] == "signed" or key[i + 1] == "long" or key[i + 1] == "short":
                filename = "E:\\codecompleter1\\GeneralSyntaxes\\" + key[i + 2] + ".py"
            else:
                filename = "E:\\codecompleter1\\GeneralSyntaxes\\" + key[i + 1] + ".py"
        elif key[i] == "sum" or key[i] == "add":
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\sum.py"
            s1 = s1.replace("and", "")
        else:
            filename = "E:\\codecompleter1\\GeneralSyntaxes\\" + key[i] + ".py"
        p = Popen(['python', filename], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        py_stdout = p.communicate(input=bytes(s1.encode('UTF-8')))[0]
        text = py_stdout.decode()
        print(text)
        text = text.replace("\r", "")
        text = text.rstrip()
        listtext = text.split("\n")
        print(listtext)
        for i in range(0, len(listtext)):
            if 'LALR' in listtext[i]:
                del (listtext[i])
                break
        text = ""
        for i in listtext:
            text += i + "\n"
        print(text)
        return text
def retrieve_key_word(l1):
    keyfile = open('keywords.txt')
    keywords = keyfile.read()
    keywordsList = keywords.split('\n')
    l2 = []
    for i in l1 :
        if i in keywordsList:
            l2.append(i)
    return l2

def parseText(str):
   # print(w2n.word_to_num(str))
    #print(w2n.number_formation(['999']))
    words = str.split()
    posTagList = pos_tag(words)
    print(posTagList)
    ignoreWordFile = open('ignorewords.txt')
    ignorewords = ignoreWordFile.read()
    ignorewordsList = ignorewords.split('\n')
    print(ignorewordsList)
    ignoreWordFile.close()
    newList = []
    for i in range(0,len(posTagList)):
        if posTagList[i][1]!='CD':
            if posTagList[i][0]=='eleven' or posTagList[i][0]=='twelve' or posTagList[i][0]=='thirteen' or posTagList[i][0]=='fourteen' or posTagList[i][0]=='fifteen' or posTagList[i][0]=='sixteen' or posTagList[i][0]=='seventeen' or posTagList[i][0]=='eighteen' or posTagList[i][0]=='nineteen' or posTagList[i][0]=='ten' or posTagList[i][0]=='twenty' or posTagList[i][0]=='thirty' or posTagList[i][0]=='forty' or posTagList[i][0]=='fifty' or posTagList[i][0]=='sixty' or posTagList[i][0]=='seventy' or posTagList[i][0]=='eighty' or posTagList[i][0]=='ninety'or posTagList[i][0]=='thousand'or posTagList[i][0]=='hundred'or posTagList[i][0]=='million'or posTagList[i][0]=='billion'or posTagList[i][0]=='one'or posTagList[i][0]=='two'or posTagList[i][0]=='three'or posTagList[i][0]=='four'or posTagList[i][0]=='five'or posTagList[i][0]=='six'or posTagList[i][0]=='seven'or posTagList[i][0]=='eight'or posTagList[i][0]=='nine':
                posTagList[i] = list(posTagList[i])
                posTagList[i][1]='CD'


    print(posTagList)
    i = 0
    while i <len(posTagList):
        print(i)
        if(posTagList[i][0]=='='):
            newList.append(posTagList[i][0])
            del(posTagList[i])
        #print(newList)
       # if posTagList[i][0] in stopWordList:
        #    continue
        #if posTagList[i][1] == 'CD' or posTagList[i][1] == 'NNS' or posTagList == 'NN' :
        if posTagList[i][1] == 'CD':
           
            l1 = []
            j = i
            while(j!=len(posTagList)and posTagList[j][1]=='CD' ):
                if(posTagList[j][0].isdigit()):
                    newList.append(posTagList[j][0])
                #    print(newList)
               #     print(1)
                    break
                l1.append(posTagList[j][0])

                j=j+1
            i = j

            s = ""
            for k in l1:
                s = s+k+" "

            if s!="" and not s.find("."):
                newList.append(w2n.word_to_num(s))
            else:
                newList.append(s)
             #   print(newList)
              #  print(2)
            #newList.append(w2n.number_formation(l1))
        #if posTagList[i][1]=='CD':
         #   print(w2n.word_to_num(posTagList[i][0]))
        #if(posTagList[i][0]=='eleven' or posTagList[i][0]=='twelve' or posTagList[i][0]=='thirteen' or posTagList[i][0]=='fourteen' or posTagList[i][0]=='fifteen' or posTagList[i][0]=='sixteen' or posTagList[i][0]=='seventeen' or posTagList[i][0]=='eighteen' or posTagList[i][0]=='nineteen' or posTagList[i][0]=='ten' or posTagList[i][0]=='twenty' or posTagList[i][0]=='thirty' or posTagList[i][0]=='forty' or posTagList[i][0]=='fifty' or posTagList[i][0]=='sixty' or posTagList[i][0]=='seventy' or posTagList[i][0]=='eighty' or posTagList[i][0]=='ninety'):
        #    posTagList[i][1]='CD'
        if(i==len(posTagList)):
            break
        if posTagList[i][0] == 'if':
            newList.append(posTagList[i][0])
            #print(newList)
            #print(3)
        if posTagList[i][0] in ignorewordsList and posTagList[i+1][0]=='loop':
            newList.append(posTagList[i][0])
            #print(newList)
            #print(4)
        elif i != len(posTagList) - 1 and posTagList[i][0] == 'for' and posTagList[i + 1][1] == 'NNP':
            newList.append('for')
        elif i ==0 and posTagList[i][0] == 'for' :
            newList.append('for')

            #print(newList)
            #print(5)
        elif posTagList[i][0]=='a':
            if i+1 == len(posTagList):
                newList.append(posTagList[i][0])
                #print(newList)
               # print(6)
            elif posTagList[i-1][1]=='NN'or posTagList[i-1][1]=='NNS':
                newList.append(posTagList[i][0])
               # print(newList)
              #  print(7)
            elif posTagList[i+1][1] =='CC' or posTagList[i+1][1]=='TO':
                newList.append(posTagList[i][0])
             #   print(newList)
            #    print(8)

        elif (posTagList[i][1]=="TO"and posTagList[0][0]=="assign")or posTagList[i][0]=="plus" or(len(posTagList)==1 and posTagList[i][1]=='CC')or(posTagList[i][1]=='CC' and posTagList[i-1][1] == 'NN' and posTagList[i+1][1] == 'NN')or(posTagList[i][1]=='CC' and posTagList[i-1][1] == 'NN' and posTagList[i+1][1] == 'CD')or(posTagList[i][1]=='CC' and posTagList[i-1][1] == 'CD' and posTagList[i+1][1] == 'NN') or(posTagList[i][1]=='CC' and posTagList[i-1][1] == 'CD' and posTagList[i+1][1] == 'CD')or posTagList[i][1] == 'NN'   or posTagList[i][1]=='NNS' or posTagList[i][1]=='JJ' or posTagList[i][1]=='JJR'or posTagList[i][1]=='NNP' or posTagList[i][1]=='VBG' or posTagList[i][1] == 'VBZ' or posTagList[i][1]== 'VBD' or posTagList[i][1]=='VBP'or posTagList[i][1]=='VBN'or (posTagList[i][1]=='VB' and posTagList[i][0]!="create" and posTagList[i][0]!='iterate') or (posTagList[i][1]=='RB' and (posTagList[i][0]=='not'or posTagList[i][0]=='else')):
            newList.append(posTagList[i][0])
           # print(newList)
           #print(9)
        i=i+1
    print("list with needed feature ")
    print(newList)
    if '' in newList:
        newList.remove('')
    return newList

if __name__== '__main__':
    f = open("E:\\codecompleter1\\SymbolTable.txt","w")
    f.close()
    f = open("E:\\codecompleter1\\ST.txt", "w")
    f.close()
    app.debug = True
    app.run()


