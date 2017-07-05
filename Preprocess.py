# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:25:52 2017

@author: Administrator
"""

#from nltk.corpus import stopwords
#from nltk.stem import WordNetLemmatizer
#from collections import Counter
#from sklearn.feature_extraction.text import TfidfVectorizer

import os
from xlrd import open_workbook
import json

# Machine Learning libraries
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

features = []
result_count = -9999

def getBasePath():
    projectPath = os.path.dirname(os.path.realpath('__file__'))
#        print(projectPath)
    basePath = os.path.join(projectPath,"")
    return basePath
            
def readData(file_path, file_type):
    questions = []
    answers = []
    if file_type == "xlsx":
        try:
            wb = open_workbook(file_path)
        #        questions = []
        #        answers = []
            for sheet in wb.sheets():
                number_of_rows = sheet.nrows
                for row in range(1, number_of_rows):
                    question = sheet.cell(row,0).value
                    questions.append(question)
                    answer = sheet.cell(row,1).value
                    answers.append(answer)
        except Exception as ex:
            print("Error in read_data() method")
            print(ex)
            
    elif file_type == "json":   
        # Reading data from JSON data
        with open(file_path,'r') as data_file:
            data = json.load(data_file)
            conversation = data['conversations']
            for each_list in conversation:
                for i in range(len(each_list)-1):
                    questions.append(each_list[i])
                    answers.append(each_list[i+1])
    return questions, answers
    
# Function defination to clean the raw data
def clean_data(raw_data):
    # for each line
    for line in raw_data:
        # remove junk characters like #,$,_ etc.
        # You can add any nonsense character to this list
        junk_characters = ['#','_','$']
        # for each junk_character
        for ch in junk_characters:
            # replace junc_character with 1 space
            line = line.replace(ch, ' ')
        
# Function defination to integrate data from multiple files/source
def integrate_data(file_path_1, file_path_2):
    with open("Merged_file.txt", "a") as fw:
        # Reading 1st file
        with open(file_path_1, "r") as f1:
            for line in f1:
                fw.write(line)
        # Reading 2nd file        
        with open(file_path_1, "r") as f1:
            for line in f1:
                fw.write(line)
                
def Vectorize_Data(data):
    vectorizer = None
    tfidf_matrix = []
    # prepare Whitelist and stop word list
#    whitelist_words = ["what", "when", "why", "whom", "who", "where", 
#    "Should", "is", "are", "do", "does", "did", "how", "can", "will"]
    stop = set(stopwords.words('english'))
    symbols = ["\\","/",":",",",";","++","--","$",".","+","-","#","?"]
    numbers = [str(i) for i in range(0,101)]
    symbols = symbols + numbers
    for s in symbols:
        stop.add(s)

    # calculate TF-IDF 
    vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1,1), 
        min_df = 1, stop_words = stop, sublinear_tf=True)
    tfidf_matrix = vectorizer.fit_transform(data)
    
    return vectorizer, tfidf_matrix

