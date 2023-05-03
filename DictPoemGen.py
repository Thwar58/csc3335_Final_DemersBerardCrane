import json
import random
import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import WordGenerator

gram = {}
try:
    with open("dictGram.txt", encoding='utf8') as file:
        data = file.read()
        gram = json.loads(data)
        file.close()
except FileNotFoundError:
    WordGenerator.makeDict()
    with open("dictGram.txt", encoding='utf8') as file:
        data = file.read()
        gram = json.loads(data)
        file.close()
    
def genSen(sz, seed):
    words = []
    if(seed == None):
        nextWord = random.choice(list(gram.keys()))
    else:
        nextWord = seed
    words.append(random.choice(gram[nextWord]))
    while len(words) < sz:
        nextWord = random.choice(gram[nextWord])
        words.append(nextWord)
    return " ".join(words)

def genCleanSen(seed):
    #generates the sentence
    if(seed == None):
        sentence = genSen(random.randint(10,15),None)
    else:
        sentence = genSen(random.randint(10,15),seed)

    #tokenizes the sentence
    taggedWords = nltk.pos_tag(word_tokenize(sentence), lang='eng')

    #list of legal parts of speech
    legalPos = ["NN","NNS", "VB", "VBZ", "JJ", "JJR", "JJS", "RB", "PRP"]

    #checks for the last word being nouns or adj or verb
    isLegal = False
    while(not isLegal):
        for pos in legalPos:
            if (taggedWords[-1][1]==pos):
                isLegal = True
        if not(isLegal):
            taggedWords = taggedWords[:len(taggedWords)-1]
            
    poem = ""
    for word in taggedWords:
        poem = poem + " " + word[0]
    poem = poem +"\n"
    return poem

def genPoem(sz):
    poem = ""
    poem = poem + genCleanSen(None)
    for i in range(sz-1):
        poem = poem + genCleanSen(word_tokenize(poem)[-1])
    return poem

def replaceNouns(poem, nouns):
    print(nouns)
    splitPoem = poem.split("\n")
    output = ""
    #the posision so only replace every other noun
    posCnt = 0;
    #the position of the pointer in the noun list
    nounCnt = 0;

    for line in splitPoem:
        #breaks up and labels the poem
        segmentedLine = word_tokenize(line)
        labeledData = nltk.pos_tag(segmentedLine, lang='eng')
        #counter of how many nousn there are
        cnt = 0
        #tup is tuple of word w POS
        for i in range(len(labeledData)):
            if(labeledData[i][1]=="NN" or labeledData[i][1]=="NNS"):
                cnt = cnt+1
        #cnt now has the count of the total number of nouns
        cnt = int(cnt/2)
        
        for i in range(len(labeledData)):
            if(labeledData[i][1]=="NN"):
                if(posCnt % 2==0):
                    labeledData[i] = (nouns[nounCnt],"NN")
                    nounCnt = (nounCnt + 1) % len(nouns)
                posCnt = (posCnt + 1)
                
                
            if(labeledData[i][1]=="NNS"):
                if(posCnt % 2==0):
                    labeledData[i] = (nouns[nounCnt] + "s","NN")
                    nounCnt = (nounCnt + 1) % len(nouns)
                posCnt = (posCnt + 1)
        for word in labeledData:
            output = output + " " + word[0]
        output = output +"\n"
    return output
    
    
    
def replaceVerbs(poem, verbs):
    print(verbs)
    splitPoem = poem.split("\n")
    output = ""
    #the posision so only replace every other noun
    posCnt = 0;
    #the position of the pointer in the noun list
    nounCnt = 0;
    for line in splitPoem:
        #breaks up and labels the poem
        segmentedLine = word_tokenize(line)
        labeledData = nltk.pos_tag(segmentedLine, lang='eng')
        #counter of how many nousn there are
        cnt = 0
        #tup is tuple of word w POS
        for i in range(len(labeledData)):
            if(labeledData[i][1]=="VBZ" or labeledData[i][1]=="VBG"or labeledData[i][1]=="VBP"or labeledData[i][1]=="VBN"or labeledData[i][1]=="VB"or labeledData[i][1]=="VBD"):
                cnt = cnt+1
        #cnt now has the count of the total number of nouns
        cnt = int(cnt/2)
        
        for i in range(len(labeledData)):
            if(labeledData[i][1]=="VBZ" or labeledData[i][1]=="VBP"or labeledData[i][1]=="VBN"or labeledData[i][1]=="VB"or labeledData[i][1]=="VBD"):
                if(posCnt % 2==0):
                    labeledData[i] = (verbs[nounCnt],"VB")
                    nounCnt = (nounCnt + 1) % len(verbs)
                posCnt = (posCnt + 1)
                
            if(labeledData[i][1]=="VBG"):
                if(posCnt % 2==0):
                    labeledData[i] = (verbs[nounCnt] + "ing","VBG")
                    nounCnt = (nounCnt + 1) % len(verbs)
                posCnt = (posCnt + 1)
        for word in labeledData:
            output = output + " " + word[0]
        output = output +"\n"
    return output
    
    



