import xlrd
from nltk import word_tokenize
import codecs
from nltk.stem.lancaster import LancasterStemmer
import os
import nltk
import json
import datetime
stemmer = LancasterStemmer()
import numpy as np
import time
words=[]
file = None
try:
 file = open('words_action.txt', 'r',encoding='latin1')
 for line in file:
    line = line[:-1]
    words.append(line)
 print(words) 
except UnicodeDecodeError:
    print("Unicode decode error")
classes =[]
file = open('classes_action.txt', 'r',encoding="UTF-8")
for line in file:
    line = line[:-1]
    classes.append(line)
print(classes) 

def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)
 
def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [word.lower() for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

def think(sentence, show_details=False):
    x = bow(sentence.lower(), words, show_details)
    if show_details:
        print ("sentence:", sentence, "\n bow:", x)
    # input layer is our bag of words
    l0 = x
    # matrix multiplication of input and hidden layer
    l1 = sigmoid(np.dot(l0, synapse_0))
    # output layer
    l2 = sigmoid(np.dot(l1, synapse_1))
    return l2




ERROR_THRESHOLD = 0.2
# load our calculated synapse values
synapse_file = 'synapses_action.json' 
with open(synapse_file) as data_file: 
    synapse = json.load(data_file) 
    synapse_0 = np.asarray(synapse['synapse0']) 
    synapse_1 = np.asarray(synapse['synapse1'])

def classify(sentence,error, show_details=False):
    results = think(sentence, show_details)

    results = [[i,r] for i,r in enumerate(results) if r>error ] 
    results.sort(key=lambda x: x[1], reverse=True) 
    return_results =[[classes[r[0]],r[1]] for r in results]
    #print ("%s \n classification: %s" % (sentence, return_results))
    return return_results



