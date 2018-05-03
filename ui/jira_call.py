from jira import JIRA
from nltk import word_tokenize
##jira_server = "https://jiratcs.atlassian.net"
##jira_user = "nik.y@tcs.com"
##jira_password = "Tcs@12345"
##
##jira_server = {'server': jira_server}
jira = None
issues= None
issues_list= None
JIRA_CONNECTED = False
returnstate ="JIRA is not connected.Please check instance is running"

#---try catch  to handle exception when not able to connect to jira---#
try:
    jira = JIRA("https://jiratcs2.atlassian.net", basic_auth=("jiratcs2@tcs.com", "Tcs@1234"))
    issues = jira.search_issues('project=L1Support')
    issues_list =[]
    for issue1 in issues:
      issues_list.append(str(issue1))
    JIRA_CONNECTED = True
    
except:
    print("could not connect to jira")

    
def if_issue_inlist(issue2):
  if JIRA_CONNECTED: 
    flag=0
    issue3 =word_tokenize(issue2)
    for issue4 in issue3:
        if(issue4 in issues_list):
            for issue5 in issues:
                if issue4==str(issue5):
                    flag =str(issue5.fields.status)
                    
           

    return flag
  else:
      return returnstate  

def GET_ASSIGNE(issue2):
  if JIRA_CONNECTED:    
    
    flag=0
    issue3 =word_tokenize(issue2)
    for issue4 in issue3:
        if(issue4 in issues_list):
            for issue5 in issues:
                if issue4==str(issue5):
                    flag =str(issue5.fields.assignee)
    return flag
  else:
      return returnstate
        
def GET_top_5_issues(issue2):
    if JIRA_CONNECTED:
     flag=''
     i=1
     for issue in jira.search_issues('reporter = currentUser() order by created desc', maxResults=5):
         flag=flag+("<br>"+str(i)+". Ticket("+str(issue)+")-"+str(issue.fields.summary)+"<br> Status-"+str(issue.fields.status)+"<br>Assignee- "+str(issue.fields.assignee)+"<br>")
         i+= 1
     if(flag==''):
         flag ="No issues logged"
     return flag
    else:
        return returnstate

def logg_issue(issue2):
  if JIRA_CONNECTED:  
    flag=''
    issue = jira.create_issue(project='LSUP', summary=issue2,description='', issuetype={'name': 'Service Request'})
    
    flag=("Your issue is logged with given information <br>Ticket("+str(issue)+")-"+str(issue.fields.summary)+"<br>Status-"+str(issue.fields.status)+"<br>Assignee- "+str(issue.fields.assignee)+"<br>")
    return flag
  else:
      return returnstate
def add_attach(attachment):
  if JIRA_CONNECTED:  
    for issue in jira.search_issues('reporter = currentUser() order by created desc', maxResults=1):
        jira.add_attachment(issue, attachment) 
  else:
      return returnstate

##jira.add_attachment(issue=new_issue, attachment='static/res/spain.jpg')


    
#---method to get status of ticket----##
def ticket_status_check_jira(answer,bot_msg,bot_msg2):
  if JIRA_CONNECTED:
    
    issue_id = if_issue_inlist(answer)
    if issue_id!=0:
        return 'Your ticket status is -'+issue_id
    else:
        str1="I am sorry, Your Issue id is not valid. Please check."
        if bot_msg2 ==str1:
            return "Sorry, please try again with correct information."
        else:
            return "I am sorry, Your Issue id is not valid. Please check."
  else:
      return returnstate
    
#----method to get assignee to ticket----##    
def ticket_assignee_check_jira(answer,bot_msg,bot_msg2):
  if JIRA_CONNECTED:  
    issue_id =GET_ASSIGNE(answer)
    if issue_id!=0:
        return 'Your ticket assignee is -'+issue_id
    else:
        str1="I am sorry, Your Issue id is not valid. Please check."
        if bot_msg2 ==str1:
            return "Sorry, please try again with correct information."
        else:
            return "I am sorry, Your Issue id is not valid. Please check."
  else:
       return returnstate 

#-----method to get last n number of tickets----##
def ticket_log_check_jira(answer,bot_msg,bot_msg2):

  if JIRA_CONNECTED:  
    issue_id = GET_top_5_issues(answer)
    if 'yes'.lower() in answer.lower() or 'ya' in answer.lower() or'yaa' in answer.lower() or'yo' in answer.lower() or 'yoo' in answer.lower() or'yup' in answer.lower() or 'yeah' in answer.lower() or 'right' in answer.lower() or 'totally' in answer.lower():
        return 'Your last 5 logged issues are -'+issue_id
    elif 'na'.lower() in answer.lower() or 'no' in answer.lower() or'nops' in answer.lower():
        return "Sorry,then please ask again, with more information"
    else:
        return "Sorry Did not understand. Please clearify your query"
  else:
      return returnstate


#-----method to raise new ticket------##
def ticket_raise_jira(answer,bot_msg,bot_msg2):
  if JIRA_CONNECTED:  
    issue_id = logg_issue(answer)
    if issue_id!=0:
        return issue_id+'you can also add any attachment to this if you want?'
    else:
        str1="I am sorry, Your Issue is not valid. Please check."
        if bot_msg2 ==str1:
            return "Sorry, please try again with correct information."
        else:
            return "I am sorry, Your Issue is not valid. Please check."
  else:
      return returnstate
