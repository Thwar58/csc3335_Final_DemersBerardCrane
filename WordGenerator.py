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
    
    #change all the occurances to percentages by dividing by numWords
#     keys = list(letterBag.keys())
#     for key in keys:
#         letterBag.update({key:letterBag.get(key)/numWords})
    
    return(letterBag)
    
    
    
#removes all but letters and spaces from the documents
def clean(line):
    cleanStrings = "".join(re.findall("[a-z ]",line)) 
    rtrn = re.split(" ", cleanStrings)
    return rtrn

#the n grams for 1, 2, and 3
oneLB = {}

file = nameOfFile

# try:
#     decomposeByN(file,oneLB,1)
        
# except FileNotFoundError:
#     print("File not found when reading in.")
# print("There are "+str(numWords)+" words.")
# print(str(oneLB))




