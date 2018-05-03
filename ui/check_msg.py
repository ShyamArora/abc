import xlrd
import chatterbot_call
import classify_query
import classify_Virtualaction
import action

mapping=[]

Question=[]

book1 = xlrd.open_workbook("lily.xlsx")
sh1= book1.sheet_by_index(0)


for rx in range(sh1.nrows):
    if rx!=0:
        if not sh1.cell_value(rowx=rx, colx=1) =='':
            Question.append({"ques":sh1.cell_value(rowx=rx, colx=1), "answer":sh1.cell_value(rowx=rx, colx=2)})
        if not sh1.cell_value(rowx=rx, colx=2)=='':
            if sh1.cell_value(rowx=rx+1, colx=2)=='':
                if sh1.cell_value(rowx=rx+2, colx=2)=='':
                    mapping.append({"Answer":sh1.cell_value(rowx=rx, colx=2),"Level1":[sh1.cell_value(rowx=rx, colx=3),sh1.cell_value(rowx=rx+1, colx=3),sh1.cell_value(rowx=rx+2, colx=3)],"Level2":[sh1.cell_value(rowx=rx, colx=4),sh1.cell_value(rowx=rx+1, colx=4),sh1.cell_value(rowx=rx+2, colx=4)],"Level3":[sh1.cell_value(rowx=rx, colx=5),sh1.cell_value(rowx=rx+1, colx=5),sh1.cell_value(rowx=rx+2, colx=5)]})
                else:
                    mapping.append({"Answer":sh1.cell_value(rowx=rx, colx=2),"Level1":[sh1.cell_value(rowx=rx, colx=3),sh1.cell_value(rowx=rx+1, colx=3)],"Level2":[sh1.cell_value(rowx=rx, colx=4),sh1.cell_value(rowx=rx+1, colx=4)],"Level3":[sh1.cell_value(rowx=rx, colx=5),sh1.cell_value(rowx=rx+1, colx=5)]})
            else:
                mapping.append({"Answer":sh1.cell_value(rowx=rx, colx=2),"Level1":sh1.cell_value(rowx=rx, colx=3),"Level2":sh1.cell_value(rowx=rx, colx=4),"Level3":sh1.cell_value(rowx=rx, colx=5)})




def check_chatterbot(msg):
    
    a=chatterbot_call.chatbot_response_conf(msg)
    
    if not a==False:
        return a
    else:
        return False

def add_attach(path):
    action.add_attach(path)
    

def checkmsglen(msg):
    msg_lenth=''
    msg=classify_query.clean_up_sentence(msg)
    print(msg)
    for a in msg:
        msg_lenth=msg_lenth+a
    return len(msg_lenth)    
def classify_query_(msg):
    threshold_for_answer=0.95
    threshold=0.90
    x1=[]
    if checkmsglen(msg)<10:
        
        x1=classify_query.classify(msg,0.6)
    else :
        x1=classify_query.classify(msg,0.08)
            
   
        
    
    if not x1:
        
        return False
            
    else:
        sa1=x1[0][0]
        if sa1=='':
            
            return False
        else :
            x2=x1[0][1]>threshold
            if x2>threshold:
                if x2>threshold_for_answer:
                    
                    return check_yes_or_no("yes",sa1)
                else :
                    return sa1
            else:
                
                sa=[]
                for index in range(len(x1)):
                    if index<3:
                        sa.append(x1[index][0])
                sa.append("If you did not mean any of above Please click me, I will help you")                    
                
            return sa
                
                
def classify_action(msg,bot_msg,bot_msg2):
    
    x1=classify_Virtualaction.classify(msg,0.9945)
    x2=classify_Virtualaction.classify(str(bot_msg),0.9945)
    flag=False
    
    
    if not x1==[]:
        if not x2==[]:
            if x1[0][1]<x2[0][1]:
                sa1=x2[0][0]
               
                if sa1=='':
                    flag= False
                else :
                   
                    flag = action.virtual_agent_function(sa1,msg,bot_msg,bot_msg2)
            else :
                sa1=x1[0][0]
               
                if sa1=='':
                    flag= False
                else :
                    flag = action.virtual_agent_function(sa1,msg,bot_msg,bot_msg2)
   
        else:
          
            sa1=x1[0][0]
            if sa1=='':
                flag= False
            else :
                flag = action.virtual_agent_function(sa1,msg,bot_msg,bot_msg2)

            
    else:
        
        if not x2==[]:
          
            sa1=x2[0][0]
            print(sa1)
            if sa1=='':
            	
            	flag= False
            else :
                flag = action.virtual_agent_function(sa1,msg,bot_msg,bot_msg2)

    
    return flag     


            
def yes_or_no(answer,reply):
    if 'yes'.lower() in answer.lower() or 'ya' in answer.lower() or'yaa' in answer.lower()  or'yo' in answer.lower() or 'yoo' in answer.lower() or'yup' in answer.lower() or 'yeah' in answer.lower() or 'right' in answer.lower() or 'totally' in answer.lower():
        return reply
    elif 'na'.lower() in answer.lower() or 'no' in answer.lower() or'nops' in answer.lower():
        return "Sorry,then please ask again, with more information"
    else:
        return "Sorry Did not understand. Please clearify your query"




                    
def check_yes_or_no(answer,bot_msg):
    #print("check msg yes or no method")
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
    #print("answer in yes or no"+answer)
    flag = False
    for a in Question:
        if answer.strip() == a['ques'].strip() :
            flag = a['answer']
            break
    return flag





def multiple_option(answer,list_of_responses):
    no_of_responses=len(list_of_responses)
    a=0
    response=''
    #print(list_of_responses)
    

    for i in range(no_of_responses):
        
        if(answer==str(i+1)):
            #print("vas")
            
            a=1
            response= list_of_responses[i]
            break

    if a==0:
        response= "Please choose correct response,again ask your query"
    return response




def check_multiple_option(answer,bot_msg):
    #print("check in multiple option")
    flag = False
    if isinstance(bot_msg, list):
        flag = False
    else:
        for i in mapping:
            if bot_msg ==i['Answer']:
                #print("check in multiple option inside")
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
                #print("check in multiple option inside")
                if isinstance(i['Level1'], list):
                    flag = multiple_option(answer,i['Level1'])
                    break
            elif bot_msg ==i['Level1']:
                if isinstance(i['Level2'], list):
                    flag = multiple_option(answer,i['Level2'])
                    break
            
    return flag  




    

