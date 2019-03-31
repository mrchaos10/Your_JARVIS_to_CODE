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
# keyoard event
    event = request.form.get('text')
    linenum=int(request.form.get('linenum'))
    print(event)
    l1 = parseText(event)


    if 'do' in l1 and 'while' in l1:
        l1.remove('while')

    #print(l1)
    s1 = ""
    for i in l1:
        s1+=" "+str(i)

    key = retrieve_key_word(l1)


    for i in key:
        filename ="E:\\codecompleter1\\GeneralSyntaxes\\"+i + ".py"
        p = Popen(['python',filename],stdout=PIPE,stdin=PIPE,stderr=STDOUT)
        py_stdout = p.communicate(input=bytes(s1.encode('UTF-8')))[0]
        text=py_stdout.decode()
        print(text)
        listtext = text.split("\n")
        print(listtext)
        for i in range(0,len(listtext)):
            if 'LALR' in listtext[i]:
                del(listtext[i])
                break
        text=""
        for i in listtext:
            text+=i+"\n"
        #codefile = open(filename)
        #text = codefile.read()
        c = 0
        for i in text:
            if i!='\n':
                c=c+1
            if i == '\n':
                if linenum!=0:
                    linecountarr.insert(linenum-1,c)
                    linenum+=1
                else:
                    linecountarr.append(c)
                c= 0

        if linenum != 0:
            linecountarr.insert(linenum-1, c)
            linenum+=1
        else:
            linecountarr.append(c)
        c=0

        print(linecountarr)
        response = flask.jsonify({'some': text,'chars':linecountarr,'linenum':linenum})
        #linecountarr.clear()
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

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
            newList.append(posTagList[i])
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

            if s!="":
                newList.append(w2n.word_to_num(s))
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

        elif posTagList[i][1] == 'NN'   or posTagList[i][1]=='NNS' or posTagList[i][1]=='JJ' or posTagList[i][1]=='JJR'or posTagList[i][1]=='NNP':
            newList.append(posTagList[i][0])
           # print(newList)
           #print(9)
        i=i+1
    print("list with needed feature ")
    print(newList)
    return newList

if __name__== '__main__':
    app.debug = True
    app.run()


