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

def getLabelsAndTexts(file):
  tsv_data = pd.read_csv(file, delimiter='\t', error_bad_lines=False)
  # print(tsv_data['star_rating'])
  labels = []
  texts = []
  for rating in tsv_data['star_rating']:
    labels.append(int(rating))
  for review in tsv_data['review_body']:
    texts.append(review)
  return np.array(labels), texts

train_labels, train_texts = getLabelsAndTexts("amazon_reviews_us_Watches_v1_00.tsv")
test_labels, test_texts = getLabelsAndTexts("amazon_reviews_us_Watches_v1_00.tsv")

print(train_labels[0])
print(train_texts[0])