from nltk.corpus import stopwords
from nltk import word_tokenize
stop_words = set(stopwords.words('english'))
import random
import nltk
words=[]
stop_word1 =["?",'"',"!",'!','"', '#', '$', '%', '&', "'", '(', ')', '*', '+',',','-','.', '/', ':', ';','<', '=', '>', '?','@', '[', ']', '^', '_', '`', '{', '|', '}', '~',
"1","2","4","5","6","7","8","9","0","/"]

stat=["Sorry this seems to be irrevelent know. Can you be more specific what you want to know.",
"Hmmm Something isn't working .Let's try something different",
"Hmmm , I have never heard that before",
"Oops ! I didn't get that",
"My apologies  didn't understand the question"]

 

def message_handle(msg):
    filtered_sentence = word_tokenize(msg)
    
    
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
    filtered_sentence1 = [w.lower() for w in filtered_sentence1 if not w.lower() in stop_words]
    filtered_sentence1 = [w for w in filtered_sentence1 if not len(w)==1 ]
    filtered_sentence1 = [w for w in filtered_sentence1 if not len(w)==0 ]
    filtered_sentence = [w.lower() for w in filtered_sentence1 if not w.isdigit()]
    from nltk.tag import pos_tag
    tagged_sent = pos_tag(filtered_sentence)
    #print(tagged_sent)
    nouns = [word for word,pos in tagged_sent if pos == 'NN' or pos == 'NNS'or pos == 'NNPS']
    if not nouns==[]:
        term=''
        for a in nouns:
            term= term+" "+a
        
        flag=["I understand you taking about "+term+".please give me some more information or i can also help you with these below options"]
        answer = ['want to send mail to access financial','want to speak our person now','want us to give you a call back']
        flag.extend(answer)
    else:
    	 
    	rand = random.randint(0,4) 
    	flag=stat[rand]
   
            
    return flag
                    

  

