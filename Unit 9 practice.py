import re

#put whatever file name here
nameOfFile = "Untitled spreadsheet - PoetryFoundationData.csv"

#breaks down the file given to the n gram data
def decomposeByN(fileName,letterBag,n):
    with open(fileName,encoding='utf8') as f:
        lineByLine = f.readlines()
        for line in lineByLine:
            line = clean(line)
            while(len(line) > n-1):
                frag = line[:n]
                if(not(letterBag.get(frag)==None)):
                    inta = letterBag.get(frag)#inta is intaga (integer) the current count of the word
                    inta = inta+1
                    letterBag.update({frag:inta})
                else:
                    letterBag.update({frag:1})
                line = line[1:]
                
        #for i in range(2469):
        f.close()
    return(letterBag)
    
    
    
#removes all but letters and spaces from the documents
def clean(line):
    line = "".join(re.findall("[a-zA-Z ]",line))  # capture the inner number only
    return line

#the n grams for 1, 2, and 3
oneLB = {}
twoLB = {}
threeLB = {}

file = nameOfFile

try:
    decomposeByN(file,oneLB,1)
    print("1-Gram done.")
    decomposeByN(file,twoLB,2)
    print("2-Gram done.")
    decomposeByN(file,threeLB,3)
    print("3-Gram done.")
        
except FileNotFoundError:
    dummyVar = 2#does nothing

print(str(oneLB))
print(str(twoLB))
print(str(threeLB))



