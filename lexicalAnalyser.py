import os
import keyword

x = open("lexicalAnalyserReadfile.py",'r')
lines = x.readlines()

def cprg(statement1):
    dt=['int','float','string','tuple','list','dictionary','boolean']
    keywords = keyword.kwlist
    delimiter = [',', ';', '"', "'", '{', '}', '|', '/', ':']
    splchar = ['~', '!', '#', '$', '^', '&', '(', ')','_', '|', '`', '{', '}', '[',
                          ']', '"',  '?', ',', '.', '/']
    operators = ['+', '-', '*', '/', '%', '==', '!=', '>', '<','>=', '<=', '&&',
                 '!', '&', '|', '^', '~', '<<', '>>', '=', '+=', '-=', '*=',
                 '/=', '%=', '<<=', '>>=', '&=', '^=','//',
                 '|=', '*', '?:', '->','**','===','and','or','not']
    functions=['print','println','type','index','length','islower','lower',
               'isupper','upper','isdigit','count','sum','find','capitalize',
               'isaplha','set','clear','copy','update','add','discard','remove',
               'append','max','min','len','insert','pop','reverse','sort','key',
               'map','split','input()','dir',]

    lst1 = list(statement1.split())
    for i in range(len(lst1)):
        flag = 0
        if lst1[i] in keywords:
            print(lst1[i], ": Keyword")
            flag = 1
        if lst1[i] in  splchar:
            print(lst1[i], ": Special Character")
            flag = 1
        if lst1[i] in dt:
            print(lst1[i], ": Keyword")
        elif lst1[i] in operators:
            print(lst1[i], ": Operator")
        elif lst1[i] in functions:
            print(lst1[i], ": Function")
        elif lst1[i] in delimiter:
            print(lst1[i], ": Delimiter")
        elif lst1[i].isnumeric():
            print(lst1[i], ": Number")
        else:
            if flag == 0:
                b = list(lst1[i])
                n = len(b)
                if n == 3 and b[0] == b[n - 1] and (b[0] == '"' or b[0] == "'"):
                    print(lst1[i], ": Character Constant")
                elif b[0] == b[n - 1] and (b[0] == '"' or b[0] == "'"):
                    print(lst1[i], ": String")
                else:
                    print(lst1[i], ": Variable")

line_no = 0
for line in lines:
    line_no  += 1
    print("\n")
    print("<----Line No {}---->".format(line_no))
    print("\n")
    statement=line
    cprg(statement)
