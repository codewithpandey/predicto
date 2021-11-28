import nltk
import csv
import re
from textblob import TextBlob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import tensorflow
# from tensorflow.python.keras import models, layers, optimizers
# from tensorflow.keras.preprocessing import Tokenizer, text_to_word_sequence
# from tensorflow.preprocessing.sequence import pad_sequence
# from sklearn.metrics import f1_score, roc_auc_score, accuracy_score


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

print(train_labels[0])
print(train_texts[0])

# pre-processing the text
non_alphanum = re.compile(r'[\W]')
non_ascii = re.compile(r'[^a-z0-1]\s')
def process_texts(texts):
  normal_texts = []
  for text in texts:
    lower = text.lower()
    no_punctn = non_alphanum.sub(r' ', lower)
    no_non_ascii = non_ascii.sub(r'', no_punctn)
    normal_texts.append(no_non_ascii)
  return normal_texts

train_texts = process_texts(train_texts)
test_texts = process_texts(test_texts)

print(train_texts[0])

# convert the data in countable vector form
