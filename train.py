# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 12:26:28 2017

@author: Administrator
"""

import pickle
from Preprocess import Vectorize_Data, readData

questions = []
answers = []

with open("data/init_file_path.txt",'r') as f:
    for line in f:
        file_path, file_type = line.strip().split("\t")
        temp_questions , temp_answers = readData(file_path,file_type)
        questions += temp_questions   
        answers += temp_answers
        
vectorizer, tfidf_matrix = Vectorize_Data(questions)

# Saving data in local disk
with open("saved_model/vectorizer_PickleFile","wb") as picklefileobject:
    pickle.dump(vectorizer, picklefileobject)
with open("saved_model/tfidf_matrix_PickleFile","wb") as picklefileobject:
    pickle.dump(tfidf_matrix, picklefileobject)
with open("saved_model/questions_PickleFile","wb") as picklefileobject:
    pickle.dump(questions, picklefileobject)
with open("saved_model/answers_PickleFile","wb") as picklefileobject:
    pickle.dump(answers, picklefileobject)
