import os
import sys
charClass = -1
lexeme=[]
nextChar = ''
lexLen = 0
token = 0
nextToken = 0

LETTER = 0
DIGIT = 1
UNKNOWN = 99
EOF = 999

INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MUL_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
seekval = 0

def addChar():
    global lexeme
    global count
    if len(lexeme)<=98:
        lexeme.append(nextChar)
    else:
        print ("Error: lexeme is too long.")
        sys.exit(0)
    return 0

def getChar():
    global seekval
    global charClass
    global nextChar
    f=open("C:\Eclipse Workspace\450\front.txt", "r")
    f.seek(seekval)
    nextChar = f.read(1)
    seekval+=1
    if nextChar:
        if nextChar.isalpha():
            charClass = LETTER;
        elif nextChar.isdigit():
            charClass = DIGIT
        else:
            charClass = UNKNOWN
    else:
        charClass = EOF
    f.close()        

def getNonBlank():
    global nextChar
    while nextChar.isspace():
        getChar()

def lex():
    global nextToken
    lexLen = 0
    getNonBlank()
    
    if charClass == LETTER:
        addChar()
        getChar()
        while (charClass == LETTER or charClass == DIGIT):
            addChar()
            getChar()
            nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
            nextToken = IDENT
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    elif charClass == EOF:
        nextToken = EOF
        lexeme[0] = 'E'
        lexeme[1] = 'O'
        lexeme[2] = 'F'
        lexeme[3] = 0
        
    print ("Next token is : "+str(nextToken)+",Next lexeme is :  "+str("".join(lexeme)))
    del lexeme[:]
    return nextToken
    
    
def lookup(ch):
    global nextToken
    if ch=='(':
        addChar()
        nextToken = LEFT_PAREN
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN
    elif ch == '+':
        addChar()
        nextToken = ADD_OP
    elif ch == '-':
        addChar()
        nextToken = SUB_OP
    elif ch == '*':
        addChar()
        nextToken = MUL_OP
    elif ch == '/':
        addChar()
        nextToken = DIV_OP
    else:
        addChar()
        nextToken = EOF
    return nextToken


def Program():
    global EOF
    global nextToken
    if open(' C:\Eclipse Workspace\450\front.txt','r'):
        getChar()
        while True:
            lex()
            if nextToken == EOF:
                break
Program()
