import xlrd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))

book1 = xlrd.open_workbook("chat.xlsx")
sh1= book1.sheet_by_index(0)

stop_word1 =["?",'"',"!",'!',"'", '#', '$', '%', '&', "'", '(', ')', '*', '+',',','-','.', '/', ':', ';','<', '=', '>', '?','@', '[', ']', '^', '_', '`', '{', '|', '}', '~',
"1","2","4","5","6","7","8","9","0",]
for rx in range(sh1.nrows):
    word_tokens = word_tokenize(sh1.cell_value(rowx=rx, colx=1))
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
    filtered_sentence1 = [w.lower() for w in filtered_sentence1 if not w.isdigit()]
    #print(filtered_sentence1)
    
