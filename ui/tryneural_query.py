try:
 import xlrd
 from nltk import word_tokenize
 from nltk.corpus import stopwords
 from sklearn.naive_bayes import MultinomialNB
 import nltk
 from nltk.stem.lancaster import LancasterStemmer
 import os
 import json
 import datetime
 stemmer = LancasterStemmer()
 import numpy as np 
 import time
except ModuleNotFoundError:
    print("module not found error")
neuron=0
stop_words = set(stopwords.words('english'))

stop_word1 =["?",'"',"!",'!','"', '#', '$', '%', '&', "'", '(', ')', '*', '+',',','-','.', '/', ':', ';','<', '=', '>', '?','@', '[', ']', '^', '_', '`', '{', '|', '}', '~',
"1","2","4","5","6","7","8","9","0","/"]

book=None
sh=None
documents =[]
filenames=[]
try:
 book = xlrd.open_workbook("lily.xlsx")
 sh = book.sheet_by_index(0)
 neuron= sh.nrows
    
 for rx in range(1,sh.nrows):
    word_tokens = word_tokenize(sh.cell_value(rowx=rx, colx=1))
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = [w for w in filtered_sentence if not w in stop_word1]
    filtered_sentence1=[]
    for w in filtered_sentence:
        flag=False
        for a in stop_word1:
            if a in w:
                w.split(a)
                filtered_sentence1.append( w.split(a)[0])
                filtered_sentence1.append( w.split(a)[1])
                flag=True
                break
        if flag==False:
            filtered_sentence1.append(w)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence1 = [w for w in filtered_sentence1 if not len(w)==1 ]
    filtered_sentence1 = [w for w in filtered_sentence1 if not len(w)==0 ]
    filtered_sentence = [w.lower() for w in filtered_sentence1 if not w.isdigit()]
    if not sh.cell_value(rowx=rx, colx=1)=='':
        flag1=False
        for a in filenames:
            if sh.cell_value(rowx=rx, colx=1).strip() == a["class"].strip():
                
                flag1=True
                break
        if flag1==False:     
            filenames.append({"class":sh.cell_value(rowx=rx, colx=1), "sentence":filtered_sentence})            
    
 
except FileNotFoundError:
    print("cannot find file")    


words = []
classes = []
documents = []
ignore_words = ['?',':','(',')',    '+/-',';',',','#','/','+','%','>','-']
# loop through each sentence in our training data
for pattern in filenames:
    # tokenize each word in the sentence
    wa = (pattern['sentence'])
    a = [w for w in wa if any(char.isdigit() for char in w)]
    w= [w for w in wa if w not in a]
    # add to our words list
    words.extend(w)
    # add to documents in our corpus
    documents.append((w, pattern['class']))
    # add to our classes list
    if pattern['class'] not in classes:
        classes.append(pattern['class'])
words1=[]
# stem and lower each word and remove dupliOutputcates
for w in words:
    if not w.isupper():
        words1.append(stemmer.stem(w.lower()))
    else:
        words1.append(w.lower())        
                      
        
        
 
words = list(set(words1))

# remove duplicates
classes = list(set(classes))


print (len(documents), "documents")

print (len(words), "unique stemmed words")
target = open('classes.txt', 'w',encoding="UTF-8")
for classe in classes:
    target.write(classe)
    target.write("\n")
target.close()
classess=[]
file = open('classes.txt', 'r',encoding="UTF-8")
for line in file:
    line = line[:-1]
    classess.append(line)
print (len(classess), "classes")

target = open('words.txt', 'w',encoding="UTF-8")
for word in words:
    
    target.write(word)
    target.write("\n")
    
target.close()

words1=[]
file = open('words.txt', 'r',encoding="UTF-8")
for line in file:
    line = line[:-1]
    words1.append(line)
print(len(words1))


training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    words1=[]
    # stem and lower each word and remove dupliOutputcates
    for w in pattern_words:
        if not w.isupper():
            words1.append(stemmer.stem(w.lower()))
        else:
            words1.append(w.lower())        
                  
    pattern_words = words1
    # create our bag of words array
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    training.append(bag)
    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    output.append(output_row)

# sample training/output
##i = 0
##w = documents[i][0]
##print ([word.lower() for word in w])
##print (training[i])
##print (output[i])

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
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
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
def train(X, y, hidden_neurons=10, alpha=1, epochs=50000, dropout=False, dropout_percent=0.5):

    print ("Training with %s neurons, alpha:%s, dropout:%s %s" % (hidden_neurons, str(alpha), dropout, dropout_percent if dropout else '') )
    print ("Input matrix: %sx%s    Output matrix: %sx%s" % (len(X),len(X[0]),1, len(classes)) )
    np.random.seed(1)

    last_mean_error = 1
    # randomly initialize our weights with mean 0
    synapse_0 = 2*np.random.random((len(X[0]), hidden_neurons)) - 1
    synapse_1 = 2*np.random.random((hidden_neurons, len(classes))) - 1
   

    prev_synapse_0_weight_update = np.zeros_like(synapse_0)
    prev_synapse_1_weight_update = np.zeros_like(synapse_1)
    
    synapse_0_direction_count = np.zeros_like(synapse_0)
    synapse_1_direction_count = np.zeros_like(synapse_1)
       
    for j in iter(range(epochs+1)):

        # Feed forward through layers 0, 1, and 2
        layer_0 = X
        layer_1 = sigmoid(np.dot(layer_0, synapse_0))
                
        if(dropout):
            layer_1 *= np.random.binomial([np.ones((len(X),hidden_neurons))],1-dropout_percent)[0] * (1.0/(1-dropout_percent))

        layer_2 = sigmoid(np.dot(layer_1, synapse_1))

        # how much did we miss the target value?
        layer_2_error = y - layer_2

        if (j% 10000) == 0 and j > 5000:
            # if this 10k iteration's error is greater than the last iteration, break out
            if np.mean(np.abs(layer_2_error)) < last_mean_error:
                print ("delta after "+str(j)+" iterations:" + str(np.mean(np.abs(layer_2_error))) )
                last_mean_error = np.mean(np.abs(layer_2_error))
            else:
                print ("break:", np.mean(np.abs(layer_2_error)), ">", last_mean_error )
                break
                
        # in what direction is the target value?
        # were we really sure? if so, don't change too much.
        layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)

        # how much did each l1 value contribute to the l2 error (according to the weights)?
        layer_1_error = layer_2_delta.dot(synapse_1.T)

        # in what direction is the target l1?
        # were we really sure? if so, don't change too much.
        layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)
        
        synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
        synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))
        
        if(j > 0):
            synapse_0_direction_count += np.abs(((synapse_0_weight_update > 0)+0) - ((prev_synapse_0_weight_update > 0) + 0))
            synapse_1_direction_count += np.abs(((synapse_1_weight_update > 0)+0) - ((prev_synapse_1_weight_update > 0) + 0))        
        
        synapse_1 += alpha * synapse_1_weight_update
        synapse_0 += alpha * synapse_0_weight_update
        
        prev_synapse_0_weight_update = synapse_0_weight_update
        prev_synapse_1_weight_update = synapse_1_weight_update

    now = datetime.datetime.now()

    # persist synapses
    synapse = {'synapse0': synapse_0.tolist(), 'synapse1': synapse_1.tolist(),
               'datetime': now.strftime("%Y-%m-%d %H:%M"),
               'words': words,
               'classes': classes
              }
    synapse_file = "synapses.json"

    with open(synapse_file, 'w') as outfile:
        json.dump(synapse, outfile, indent=4, sort_keys=True)
    print ("saved synapses to:", synapse_file)

X = np.array(training)
y = np.array(output)

start_time = time.time()

train(X, y, hidden_neurons=40, alpha=0.01, epochs=130000, dropout=False, dropout_percent=0.2)

elapsed_time = time.time() - start_time
print ("processing time:", elapsed_time, "seconds")


# probability threshold
ERROR_THRESHOLD = 0.2
# load our calculated synapse values
synapse_file = 'synapses.json' 
with open(synapse_file) as data_file: 
    synapse = json.load(data_file) 
    synapse_0 = np.asarray(synapse['synapse0']) 
    synapse_1 = np.asarray(synapse['synapse1'])

def classify(sentence,error, show_details=False):
    results = think(sentence, show_details)

    results = [[i,r] for i,r in enumerate(results) if r>error ] 
    results.sort(key=lambda x: x[1], reverse=True) 
    return_results =[[classes[r[0]],r[1]] for r in results]
    print ("%s \n classification: %s" % (sentence, return_results))
    return return_results
