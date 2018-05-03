import xlrd
import chatterbot_call
import classify_query
import classify_Virtualaction
import action
import psycopg2
conversation = [
"Hello",
"Hello there! How may I help you?",
"Hi",
"Hello there! How may I help you?",
"Hello Alan",
"Hello there! How may I help you?",
"Hi Alan",
"Hello there! How may I help you?",
"Hey Alan",
"How are you doing?, How may I help you?",
"How are you doing?",
"I'm doing great. How may I help you?",
"Thank you",
"You're welcome, Always at your service.",
"Bye",
"Okay, see you soon. Have a great day!",
"I am doing good",
"Glad to hear! How may I help you?",
"I am doing great",
"Glad to hear! How may I help you?",
"okay",
"Is there anything else that I can help you with today?",
"ok",
"Is there anything else that I can help you with today?",
"okk",
"Is there anything else that I can help you with today?",
"ok then",
"Is there anything else that I can help you with today?",
"thanks",
"You're welcome, Always at your service.",
"thanks for help",
"You're welcome, Always at your service.",
"thankyou",
"You're welcome, Always at your service.",
"Hallo",
"Hallo! Wie geht es Ihnen?",
"Mir geht es gut",
"Froh zu hören! Wie kann ich dir helfen?",
"Vielen Dank",
"Sie sind herzlich willkommen und bitte sagen Sie mir, wenn Sie jederzeit helfen können. Immer für Sie da",
"こんにちは","こんにちは！ どのように私はあなたを助けることができる？",
"こんにちは"," こんにちは！ どのように私はあなたを助けることができる？",
"お元気ですか？","私は素晴らしいことをしています。どうすればあなたを助けることができますか？",
"ありがとうございました","あなたは歓迎です、いつもあなたのサービスで。",
"さよなら","さて、お会いしましょう。素晴らしい一日を！",
]
mapping=[]

Question=[]

conn = psycopg2.connect(database = "que_ans", user = "postgres", password = "mohitsain97", host = "127.0.0.1", port = "5432")
cur = conn.cursor()
cur.execute("select * from qna")
rows = cur.fetchall()

#book1 = xlrd.open_workbook("chat.xlsx")
#sh1= book1.sheet_by_index(0)


for rx in range(len(rows)):
    if rx!=0:
        if not rows[rx][1] =='':
            Question.append({"ques":rows[rx][0], "answer":rows[rx][1]})
        if not rows[rx][1]=='':
            if rows[rx+1][1]=='':
                if rows[rx+2][1]=='':
                    mapping.append({"Answer":rows[rx][1],"Level1":[rows[rx][2],rows[rx+1][2],rows[rx+2][2]],"Level2":[rows[rx][3],rows[rx+1][3],rows[rx+2][3]],"Level3":[rows[rx][4],rows[rx+1][4],rows[rx+2][4]]})
                else:
                    mapping.append({"Answer":rows[rx][1],"Level1":[rows[rx][2],rows[rx+1][2]],"Level2":[rows[rx][3],rows[rx+1][3]],"Level3":[rows[rx][4],rows[rx+1][4]]})
            else:
                mapping.append({"Answer":rows[rx][1],"Level1":rows[rx][2],"Level2":rows[rx][3],"Level3":rows[rx][4]})




def check_chatterbot(msg):
    a=0
    for w in conversation:
        if msg.lower() in w.lower():
            a=1
    if a==1:
        return str(chatterbot_call.chatbot_response(msg))
    else:
        return False

def add_attach(path):
    action.add_attach(path)
    


def classify_query_(msg):
    threshold_for_answer=0.95
    threshold=0.90
    x1=classify_query.classify(msg,0.006)
    
    if not x1:
        return False
            
    else:
        sa1=x1[0][0]
        if sa1=='':
            return False
        else :
            x2=x1[0][1]>threshold
            if x2>threshold or len(x1)==1:
                if x2>threshold_for_answer:
                    return check_yes_or_no("yes",sa1)
                else :
                    return sa1
            else:
                
                sa=[]
                for index in range(len(x1)):
                    if index<3:
                        sa.append(x1[index][0])
                                   
                
            return sa
                
                
def classify_action(msg,bot_msg,bot_msg2):
    if isinstance(bot_msg, list):
        return False
    else :
        x1=classify_Virtualaction.classify(bot_msg,0.98)
        if not x1:
            return False
            
        else:
            sa1=x1[0][0]
            if sa1=='':
                return False
            else :
                return action.virtual_agent_function(sa1,msg,bot_msg,bot_msg2)


def yes_or_no(answer,reply):
    if 'yes'.lower() in answer.lower() or 'ya' in answer.lower() or'yaa' in answer.lower()  or'yo' in answer.lower() or 'yoo' in answer.lower() or'yup' in answer.lower() or 'yeah' in answer.lower() or 'right' in answer.lower() or 'totally' in answer.lower():
        return reply
    elif 'na'.lower() in answer.lower() or 'no' in answer.lower() or'nops' in answer.lower():
        return "Sorry,then please ask again, with more information"
    else:
        return "Sorry Did not understand. Please clearify your query"




                    
def check_yes_or_no(answer,bot_msg):
    print("check msg yes or no method")
    flag = False
    if isinstance(bot_msg, list):
        flag = False
    else :
        
        for a in Question:
            if bot_msg == a['ques'] and type(answer)!=int:
                flag = yes_or_no(answer,a['answer'])
                break
    return flag

def check_yes_or_no_in_option(answer,bot_msg):
    print("answer in yes or no"+answer)
   
    flag = False
    if isinstance(bot_msg, list) and answer.isdigit():
        for a in Question:
            if bot_msg[int(answer)] == a['ques']:
                print("ture")
                flag = a['answer']
                break
    return flag





def multiple_option(answer,list_of_responses):
    no_of_responses=len(list_of_responses)
    a=0
    response=''
    print(list_of_responses)
    

    for i in range(no_of_responses):
        
        if(answer==str(i+1)):
            print("vas")
            
            a=1
            response= list_of_responses[i]
            break

    if a==0:
        response= "Please choose correct response,again ask your query"
    return response




def check_multiple_option(answer,bot_msg):
    print("check in multiple option")
    flag = False
    if isinstance(bot_msg, list):
        flag = False
    else:
        for i in mapping:
            if bot_msg ==i['Answer']:
                print("check in multiple option inside")
                if isinstance(i['Level1'], list):
                    flag = multiple_option(answer,i['Level1'])
                    break
            elif bot_msg ==i['Level1']:
                if isinstance(i['Level2'], list):
                    flag = multiple_option(answer,i['Level2'])
                    break
            
    return flag   
                
def message_handle(msg):
    if isinstance(bot_msg, list):
        flag = False
    else:
        for i in mapping:
            if bot_msg ==i['Answer']:
                print("check in multiple option inside")
                if isinstance(i['Level1'], list):
                    flag = multiple_option(answer,i['Level1'])
                    break
            elif bot_msg ==i['Level1']:
                if isinstance(i['Level2'], list):
                    flag = multiple_option(answer,i['Level2'])
                    break
            
    return flag  




    

