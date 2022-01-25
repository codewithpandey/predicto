import nltk
import csv
import re
from textblob import TextBlob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
# import tensorflow
# from tensorflow.python.keras import models, layers, optimizers
# from tensorflow.keras.preprocessing import Tokenizer, text_to_word_sequence
# from tensorflow.preprocessing.sequence import pad_sequence
from sklearn.metrics import f1_score, roc_auc_score, accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# nltk.download('punkt')

# getting the testing and traning datasets
def getLabelsAndTexts(file):
  tsv_data = pd.read_csv(file, delimiter='\t', error_bad_lines=False)
  labels = []
  texts = []
  for rating in tsv_data['star_rating']:
    labels.append(int(rating))
  for review in tsv_data['review_body']:
    texts.append(review)
  
  # removing texts which are not strings
  count = 0
  for text in texts:
    if type(text) != str:
      del texts[count]
      del labels[count]
    count += 1
    
  return np.array(labels), texts

train_labels, train_texts = getLabelsAndTexts("amazon_reviews_us_Watches_v1_00.tsv")
test_labels, test_texts = getLabelsAndTexts("amazon_reviews_us_Watches_v1_00.tsv")

# print(train_labels[0])
# print(train_texts[0])

train_labels = train_labels[0:500]
train_texts = train_texts[0:500]

# pre-processing the text
non_alphanum = re.compile(r'[\W]')
non_ascii = re.compile(r'[^a-z0-1]\s')
def process_texts(texts):
  normal_texts = []
  for text in texts:
    lower = text.lower()
    no_punctn = non_alphanum.sub(r' ', lower)
    no_non_ascii = non_ascii.sub(r' ', no_punctn)
    normal_texts.append(no_non_ascii)
  return normal_texts

train_texts = process_texts(train_texts)
test_texts = process_texts(test_texts)

print(test_texts[0])

# convert the data in countable vector form

cvec = CountVectorizer(binary=True)
cvec.fit(train_texts)
X = cvec.transform(train_texts)
X_test = cvec.transform(test_texts)

print(X_test[0])

# splitting the training and testing values

X_train, X_val, Y_train, Y_val = train_test_split(X, train_labels, train_size = 0.75)

# training the data using LogisticRegression (Will use Neural Networks Later)

for c in [0.01, 0.05, 0.25, 0.5, 1]:
  model = LogisticRegression(C=c)
  model.fit(X_train, Y_train)
  print("Accuracy for C=%s: %s" % (c, accuracy_score(Y_val, model.predict(X_val))))
  pickle.dump(model, open('predicto1.model', 'wb'))

# load the model from disk
model = pickle.load(open('predicto1.model', 'rb'))
print(X_test[0])
result = model.predict(X_test[0])
print(result)
# print(LR.predict(X_test[1]))