import json
import random
import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

gram = {}

with open("dictGram.txt", encoding='utf8') as file:
    data = file.read()
    gram = json.loads(data)
    file.close()
    
def genSen(sz):
    words = []
    nextWord = random.choice(list(gram.keys()))
    words.append(nextWord)
    while len(words) < sz:
        nextWord = random.choice(gram[nextWord])
        words.append(nextWord)
    return " ".join(words)

#generates the sentence
sentence = genSen(random.randint(10,15))

#tokenizes the sentence
taggedWords = nltk.pos_tag(word_tokenize(sentence), lang='eng')

#list of legal parts of speech
legalPos = ["NN","NNS", "VB", "VBZ", "JJ", "JJR", "JJS", "RB", "PRP"]

#checks for the last word being nouns or adj or verb
print(taggedWords)
isLegal = False
while(not isLegal):
    for pos in legalPos:
        if (taggedWords[-1][1]==pos):
            isLegal = True
    if not(isLegal):
        print(taggedWords[len(taggedWords)-1])
        taggedWords = taggedWords[:len(taggedWords)-1]
        

print(sentence)






