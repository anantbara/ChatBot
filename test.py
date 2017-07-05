# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:46:16 2017

@author: Administrator
"""
import pickle

# Machine Learning libraries
from sklearn.metrics.pairwise import cosine_similarity

questions = []
answers = []
vectorizer = None
tfidf_matrix = None

# Loading data from local disk
with open("saved_model/vectorizer_PickleFile","rb") as picklefileobject:
    vectorizer = pickle.load(picklefileobject)
with open("saved_model/tfidf_matrix_PickleFile","rb") as picklefileobject:
    tfidf_matrix = pickle.load(picklefileobject)
with open("saved_model/questions_PickleFile","rb") as picklefileobject:
    questions = pickle.load(picklefileobject)
with open("saved_model/answers_PickleFile","rb") as picklefileobject:
    answers = pickle.load(picklefileobject)


sim_count = 1
threshold = 0.6
text = ["I am doing well, how about you?"]
tfidf = vectorizer.transform(text)
sim_result = cosine_similarity(tfidf, tfidf_matrix)[0]
sim_result_with_index = [(i, prob) for i, prob in enumerate(sim_result)]
# Sort based on 2nd index i.e. probability score
sorted_result = sorted(sim_result_with_index, reverse=True, key=lambda t:t[1])[:sim_count]
if sorted_result[0][1] >= threshold:
    index = sorted_result[0][0]
    print(answers[index],sorted_result[0][1])
else:
    print("I am sorry, but I do not understand.",sorted_result[0][1])
#transformation(questions, answers)   