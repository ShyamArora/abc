from nltk import word_tokenize
import sys
from simple_salesforce import Salesforce
sf= None
SF_CONNECTED = False
sf_msg ="oops! cannot cannect to salesforce please check credentials and token are correct"
try:
   sf = Salesforce(username='sfdctraning@tcs.com', password='Surbhi@1234', security_token='HBUU2ckVCtHchEHv2WIPjI8ia')
   SF_CONNECTED= True
except:    
    print("invalid login credentials/token")

def contact_create(name):
   if SF_CONNECTED: 
      sf.Contact.create({'LastName':name})
   else:
       return sf_msg


##sf.Account.create({'Name':'sample'})
#print(sf.query_all("SELECT Id, Email FROM Contact WHERE LastName = 'Shyam'"))


def contact_create_salesforce(answer,bot_msg,bot_msg2):
   if SF_CONNECTED:
     contact_create(answer)
     return 'Your Contact is created with name - '+answer
   else:
       return sf_msg
def CHANGE_PASSWORD(username,password):
    dat={}
    dat["Username"]=username
    dat["pwd"]=password
    #dat2 = json.dumps(dat)
    result = sf.apexecute('ResetPassword', method='POST', data=dat)
    return result




def reset_password_salesforce(answer,bot_msg,bot_msg2):
    RESET_PASSWORD(username,password)
    return 'Your Contact is created with name - '+answer


def password_reset_salesforce(answer,bot_msg,bot_msg2):
    #credential =word_tokenize(answer)
   if SF_CONNECTED: 
     credential = answer.split(",")  
     username=credential[0]
     password=credential[1]
     try:
         issue_id=CHANGE_PASSWORD(username,password)
         if issue_id!=0:
            return 'Password has been changed successfully,please check your mail for new TOKEN '
         else:
            str1="I am sorry, Your Issue is not valid. Please check."
            if bot_msg2 ==str1:
              return "Sorry, please try again with correct information."
            else:
              return "I am sorry, Your Issue is not valid. Please check."
     except:
         return "Oops! something went wrong <br> please check your entered username and password"
   else:
      return sf_msg
       
