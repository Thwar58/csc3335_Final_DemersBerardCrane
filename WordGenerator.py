import re

#put whatever file name here
nameOfFile = "Untitled spreadsheet - PoetryFoundationData.csv"
numWords = 0

#breaks down the file given to the n gram data
def decomposeByN(fileName,letterBag,n):
    global numWords
    with open(fileName,encoding='utf8') as f:
        lineByLine = f.readlines()
        for line in lineByLine:
            line = line.lower()
            words = clean(line)
            while(len(words) > 0):
                word = words[0]
                if(word==""):
                    break
                if(not(letterBag.get(word)==None)):
                    inta = letterBag.get(word)#inta is intaga (integer) the current count of the word
                    inta = inta+1
                    letterBag.update({word:inta})
                else:
                    letterBag.update({word:1})
                numWords = numWords + 1
                words = words[1:]
                
        #for i in range(2469):
        f.close()
    
    #change all the occurances to percentages by dividing by numWords
    keys = list(letterBag.keys())
    for key in keys:
        letterBag.update({key:letterBag.get(key)/numWords})
    
    return(letterBag)
    
    
    
#removes all but letters and spaces from the documents
def clean(line):
    cleanStrings = "".join(re.findall("[a-z ]",line))  # capture the inner number only
    rtrn = re.split(" ", cleanStrings)
    return rtrn

#the n grams for 1, 2, and 3
oneLB = {}

file = nameOfFile

try:
    decomposeByN(file,oneLB,1)
        
except FileNotFoundError:
    print("File not found when reading in.")
print("There are "+str(numWords)+" words.")
print(str(oneLB))




