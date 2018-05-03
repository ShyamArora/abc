import xlrd
import math
book =None
sh=None
userdata=[]
GILEAD_CONNECTED=False
gilead_msg= "Oops! something went wrong"
try:
 book = xlrd.open_workbook("user_data_gilead.xlsx")
 sh=book.sheet_by_index(0)
 for rx in range(sh.nrows):
      if rx!=0:
         userdata.append({"name_rep":sh.cell_value(rowx=rx, colx=0), "access":sh.cell_value(rowx=rx, colx=1),"name_app":sh.cell_value(rowx=rx, colx=2),"location":sh.cell_value(rowx=rx, colx=3)})
 GILEAD_CONNECTED=True
 print(userdata)
except FileNotFoundError:
    print("cannot find file")
    



def gilead_access_svn(answer,bot_msg,bot_msg2):
    flag = False
    if GILEAD_CONNECTED:
        if(answer.count(",")>0):
            print('sadf')
            for x in userdata:
                print(x['name_rep'].lower()+x['access'].lower()+answer.lower())
                if x['name_rep'].lower() in answer.lower() and x['access'].lower() in answer.lower() :
                    flag=True
                    print('sasxadf')
                    break 

            if flag==True:
                return 'I will open a predefined list of SVN repositories and look for Admin entry against repository entered by you and will send a customised mail to all Admins requesting for their approval to provide access to the you.'
               
            else :
                str1="I am sorry, Your information are not valid. Please check."
                if bot_msg ==str1:
                    return "Sorry, please try again with correct information."
                else:
                    return "I am sorry, Your information are not valid. Please check."
        else:
            str1="Please provide information in commas,ex:iRep,Read"
            if bot_msg ==str1:
                return "Sorry, please try again with correct information."
            else:
                return "Please provide information in commas,ex:iRep,Read"

    else:
        return gilead_msg

      
def gilead_access_sandimas(answer,bot_msg,bot_msg2):
    flag = False
    if GILEAD_CONNECTED:
          for x in userdata:
              if x['location'].lower() in answer.lower() :
                  flag=True
                  break
          if flag==True:
                return 'I have send a customized mail to David C. Johnson encapsulating all the information.'               
          else :
              str1="'You are not allowed to access the applications"
              if bot_msg ==str1:
                  return "Sorry, please try again with correct information."
              else:
                  return "'You are not allowed to access the applications"
    else:
        return gilead_msg

    
    
      

def gilead_access_application(answer,bot_msg,bot_msg2):
    flag = False
    if GILEAD_CONNECTED:
        for x in userdata:
            if x['name_app'].lower() in answer.lower():
                flag=True
                break
        if flag==True:
                return 'I will look for the Admin of the application from the predefined list against the Name given by the you and sends a customized mail to Admins asking for their approval.'
          
        else :
            str1="I am sorry, Your information are not valid. Please check."
            if bot_msg ==str1:
                return "Sorry, please try again with correct information."
            else:
                return "I am sorry, Your information are not valid. Please check."
    else:
        return gilead_msg




def gilead_mobile_stipend(answer,bot_msg,bot_msg2):
  if GILEAD_CONNECTED:  
    if 'yes'.lower() in answer.lower() or 'ya' in answer.lower() or'yaa' in answer.lower() or'yo' in answer.lower() or 'yoo' in answer.lower() or'yup' in answer.lower() or 'yeah' in answer.lower() or 'right' in answer.lower() or 'totally' in answer.lower():
        return 'I have generated a ticket and your ticket number is Tick'+str(random.randint(1111,9999))
    elif 'na'.lower() in answer.lower() or 'no' in answer.lower() or'nops' in answer.lower():
        return "Sorry,then please ask again, with more information"
    else:
        return "Sorry Did not understand. Please clearify your query"
  else:
      return gilead_msg
