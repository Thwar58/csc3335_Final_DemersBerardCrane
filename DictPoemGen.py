import json
import random

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

print(genSen(random.randint(20,30)))