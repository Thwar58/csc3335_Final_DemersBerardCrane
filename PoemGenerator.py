import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow.keras.utils as ku
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import regularizers
from tensorflow.keras.models import load_model
# Sources:
# https://www.geeksforgeeks.org/lstm-based-poetry-generation-using-nlp-in-python/#
# https://kgptalkie.medium.com/poetry-generation-using-tensorflow-keras-and-lstm-75c4e4b7f07e

# cleans data and outputs to .txt file
def cleanAndTxt():
    with open("CleanPoetryData.csv", encoding='utf8') as f, open('CleanedPoetry.txt', 'w') as f_out:
        output = f.read()
        output = "".join(re.findall("[a-zA-Z ,.'\n]", output))
        output = re.sub(',,+', ' ', output).strip()
        output = re.sub('  +', '\n', output)
        output = re.sub('\n+', '\n', output)
        output = re.sub("[,.]", ' ', output)
        output = re.sub('  +', ' ', output)
        output = re.sub('\n +', '\n', output)
        output = re.sub('\n+', '\n', output).strip()
        f_out.write(output.lower())

# cleanAndTxt()

# Generating the corpus by splitting the text into lines
data = open('CleanedPoetry.txt', encoding="utf8").read()
corpus = data.split("\n")
for line in corpus:
    # remove the line if it is too long
    if(len(line) > 60):
        corpus.remove(line)

# Fitting the Tokenizer on the Corpus
token = Tokenizer()
token.fit_on_texts(corpus[:1000])

# Encoding the tokenized words
encoded_text = token.texts_to_sequences(corpus)
# vocabulary size should be + 1
vocab_size = len(token.word_counts) + 1

# Preparing the training data
datalist = []
for d in encoded_text:
  if len(d) > 1:
    for i in range(2, len(d)):
      datalist.append(d[:i])

# Padding so sequences all have the same length
max_length = 20
sequences = pad_sequences(datalist, maxlen=max_length, padding='pre')
X = sequences[:, :-1]
y = sequences[:, -1]
y = to_categorical(y, num_classes=vocab_size)
seq_length = X.shape[1]

# LSTM model
model = Sequential()
model.add(Embedding(vocab_size, 50, input_length=seq_length))
model.add(LSTM(100, return_sequences=True))
model.add(LSTM(100))
model.add(Dense(100, activation='relu'))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# Model training
model.fit(X, y, batch_size=32, epochs=50)

# Save the model
model.save("model.h5")
print("Saved model to disk")

poetry_length = 10
def generate_poetry(seed_text, n_lines):
  for i in range(n_lines):
    text = []
    for _ in range(poetry_length):
      encoded = token.texts_to_sequences([seed_text])
      encoded = pad_sequences(encoded, maxlen=seq_length, padding='pre')

      y_pred = np.argmax(model.predict(encoded), axis=-1)

      predicted_word = ""
      for word, index in token.word_index.items():
        if index == y_pred:
          predicted_word = word
          break

      seed_text = seed_text + ' ' + predicted_word
      text.append(predicted_word)

    seed_text = text[-1]
    text = ' '.join(text)
    print(text)


seed_text = 'i love you'
generate_poetry(seed_text, 5)




# # Fitting the Tokenizer on the Corpus
# tokenizer = Tokenizer()
# tokenizer.fit_on_texts(corpus[:100]) #number of lines to use

# # Vocabulary count of the corpus
# total_words = len(tokenizer.word_index)

# print("Total Words:", total_words)

# # Converting the text into embeddings
# input_sequences = []
# for line in corpus:
#     token_list = tokenizer.texts_to_sequences([line])[0]

#     for i in range(1, len(token_list)):
#         n_gram_sequence = token_list[:i+1]
#         input_sequences.append(n_gram_sequence)

# max_sequence_len = max([len(x) for x in input_sequences])
# # input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
# # predictors, label = input_sequences[:, :-1], input_sequences[:, -1]
# # label = ku.to_categorical(label, num_classes=total_words+1)

# # # Building a Bi-Directional LSTM Model
# # model = Sequential()
# # model.add(Embedding(total_words+1, 25, input_length=max_sequence_len-1))
# # model.add(Bidirectional(LSTM(40, return_sequences=True)))
# # model.add(Dropout(0.2))
# # model.add(LSTM(25))
# # model.add(Dense(total_words+1/2, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
# # model.add(Dense(total_words+1, activation='softmax'))
# # model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# # print(model.summary())

# # history = model.fit(predictors, label, epochs=1, verbose=1)

# # # Save the model
# # model.save("model.h5")
# # print("Saved model to disk")

# # Load the model
# model = load_model('model.h5')

# seed_text = "The sun is"
# next_words = 25
# ouptut_text = ""

# for _ in range(next_words):
#     token_list = tokenizer.texts_to_sequences([seed_text])[0]
#     token_list = pad_sequences( [token_list], maxlen=max_sequence_len-1, padding='pre')
#     predicted = np.argmax(model.predict(token_list, verbose=0), axis=-1)
#     output_word = ""

#     for word, index in tokenizer.word_index.items():
#         if index == predicted:
#             output_word = word
#             break

#     seed_text += " " + output_word

# print(seed_text)
