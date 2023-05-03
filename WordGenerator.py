import re
import json

#put whatever file name here
nameOfFile = "CleanedPoetry.txt"
numWords = 0

#breaks down the file given to the n gram data
def decomposeByN(fileName,letterBag,n):
    global numWords
    with open(fileName,encoding='utf8') as f:
        lineByLine = f.readlines()
        for line in lineByLine:
            #makes all words in line lower case for ease of camparison
            line = line.lower()
            #cleans the lines 
            words = clean(line)
            while(len(words) > n-1):
                #chops off the first n words and then concats them together
                word = words[:n]
                convertingToString = ""
                for i in range(len(word)-1):
                    convertingToString = convertingToString + word[i]+" "
                #this next line is outside the loop to not have a space at the end
                convertingToString = convertingToString + word[len(word)-1]
                word = convertingToString
                #ignores empty lines
                if(word==""):
                    break
                #adds a new entry if one does not exists, else add one to it
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
        
def nGramDict(fileName,gram,n):
    global numWords
    allWords = []
    with open(fileName,encoding='utf8') as f:
        lineByLine = f.readlines()
        for line in lineByLine:
            #makes all words in line lower case for ease of camparison
            line = line.lower()
            #cleans the lines 
            words = clean(line)
            for word in words:
                if(word==""):
                    continue
                allWords.append(word)
               
        f.close()
        
    # got the code below from a youtube video
    # "Generating Sentences with n-grams using Python"
    # by Douglas Starnes
    for i in range(len(allWords)-1):
        try:
            gram[allWords[i]].append(allWords[i+1])
        except KeyError as _:
            gram[allWords[i]] = []
            gram[allWords[i]].append(allWords[i+1])
    
    return(gram)
    
    
    
#removes all but letters and spaces from the documents
def clean(line):
    cleanStrings = "".join(re.findall("[a-z ]",line)) 
    rtrn = re.split(" ", cleanStrings)
    return rtrn

def makeDict():
    #the n grams for 1, 2, and 3
    oneLB = {}
    nGram = {}

    file = nameOfFile

    try:
        ans = nGramDict(file,nGram,1)
            
    except FileNotFoundError:
        print("File not found when reading in.")
    # print("There are "+str(numWords)+" words.")

    with open("dictGram.txt" , 'w') as file:
        json_object = json.dumps(ans, indent = 4)
        file.write(json_object)
        file.close()
    print("Made dictGram.txt")




