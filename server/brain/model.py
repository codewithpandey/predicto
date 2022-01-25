import csv
import re
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
from sklearn.preprocessing import OneHotEncoder


class Model:

    # getting the testing and traning datasets
    def getLabelsAndTexts(self, file):
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

    def process_texts(self, texts):
        # pre-processing the text
        non_alphanum = re.compile(r'[\W]')
        non_ascii = re.compile(r'[^a-z0-1]\s')
        normal_texts = []
        count = 0
        for text in texts:
            # print(f"Text{count}", text)
            lower = text.lower()
            no_punctn = non_alphanum.sub(r' ', lower)
            no_non_ascii = non_ascii.sub(r' ', no_punctn)
            normal_texts.append(no_non_ascii)
            count += 1  
        return normal_texts

    def train(self):

        train_labels, train_texts = self.getLabelsAndTexts("amazon_reviews_us_Watches_v1_00.tsv")
        test_labels, test_texts = self.getLabelsAndTexts("amazon_reviews_us_Watches_v1_00.tsv")

        # print(train_labels[0])
        # print(train_texts[0])

        train_labels = train_labels[0:500]
        train_texts = train_texts[0:500]

        
        train_texts = self.process_texts(train_texts)
        test_texts = self.process_texts(test_texts)

        # print(train_texts[0])

        # convert the data in countable vector form

        cvec = CountVectorizer(binary=True)
        cvec.fit(train_texts)
        X = cvec.transform(train_texts)
        X_test = cvec.transform(test_texts)
        # print("X_test: ", X_test)

        # splitting the training and testing values

        X_train, X_val, Y_train, Y_val = train_test_split(X, train_labels, train_size = 0.75)
        # training the data using LogisticRegression
        for c in [0.01, 0.05, 0.25, 0.5, 1]:
            model = LogisticRegression(C=c)
            model.fit(X_train, Y_train)
            print("Accuracy for C=%s: %s" % (c, accuracy_score(Y_val, model.predict(X_val))))
            pickle.dump(model, open('predicto.model', 'wb'))

    def predict(self, review):
        
        train_labels, train_texts = self.getLabelsAndTexts("amazon_reviews_us_Watches_v1_00.tsv")
        # test_labels, test_texts = self.getLabelsAndTexts("amazon_reviews_us_Watches_v1_00.tsv")

        # print(train_labels[0])
        # print(train_texts[0])

        # train_labels = train_labels[0:500]
        train_texts = train_texts[0:500]

        
        train_texts = self.process_texts(train_texts)
        review = self.process_texts(review)

        # print(train_texts[0])

        # convert the data in countable vector form

        cvec = CountVectorizer(binary=True)
        cvec.fit(train_texts)
        print(review[0])
        X = cvec.transform(review)
        print(X[0])
        
        # loading the model
        model = pickle.load(open('predicto.model', 'rb'))
        result = model.predict(X[0])
        print(result)
        return result