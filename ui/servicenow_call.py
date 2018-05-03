import requests
from collections import Counter
from nltk import word_tokenize
import json
import os
import nltk
user = 'admin'
pwd = 'LqEZaDk8yU8x'
i=0


def get_knowledge(shortDescription):
    str=shortDescription.strip()
    str.replace(" ","%20")
    url='https://dev22908.service-now.com/api/now/table/kb_knowledge?sysparm_query=short_description%3D'+str+'&sysparm_display_value=true&sysparm_fields=text&sysparm_limit=1'
    user= 'admin'
    pwd = 'SALESforce@2017'
	# Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}
	
	# Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers  )

	# Check for HTTP codes other than 200
    if response.status_code != 200: 
       print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
       exit()

	# Decode the JSON response into a dictionary and use the data
    data = response.json()
    list1=data['result']
    if not list1:
     print("no data found")
    else:
    # print(list1[0]['text'])
     path ='static/upload/'
     
     f = open(os.path.join(path, "KnowledgeText.html"), "w")
     
     f.write("<html><body>"+list1[0]['text']+"<body></html>")
     f.close()
     return os.path.join(path, "KnowledgeText.html")  
     
##     file.save(os.path.join(path, "KnowledgeText.html"))

	
####-----------------GET INCIDENT------------------------------------	
def get_incident(shortDescription):
    str=shortDescription.strip()
    str.replace(" ","%20")
    url = 'https://dev22908.service-now.com/api/now/table/incident?sysparm_query=short_description%3D'+str+'&sysparm_fields=number%2Csys_created_on%2Csys_created_by%2Cknowledge%2Cclosed_at%2Csys_id%2Ccategory%2Cseverity%2Cshort_description&sysparm_limit=1'
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    user = 'admin'
    pwd = 'SALESforce@2017'
	# Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers  )

	# Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

	# Decode the JSON response into a dictionary and use the data
    data = response.json()
    print(data)
    return data
	
####-----------------GET TICKET-------------------------------------------------		
def get_ticket(shortDescription):
    str=shortDescription.strip()
    str.replace(" ","%20")     
    url = 'https://dev22908.service-now.com/api/now/table/ticket?sysparm_query=short_description%3D'+str+'&sysparm_fields=short_description%2Cnumber%2Cstate%2Cactive%2Cdescription%2Csys_created_by&sysparm_limit=1'

	# Eg. User name="admin", Password="admin" for this code sample.


	# Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

	# Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers  )

	# Check for HTTP codes other than 200
    if response.status_code != 200:
        print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

	# Decode the JSON response into a dictionary and use the data
    data = response.json()
    a=data['result']
    print(a)
    return a

###### ---------GET ASSIGNEE TO THE TICKET--------------------------------
def Get_Assignee(answer):
  
  tokens = nltk.word_tokenize(answer.strip())
  for i in range(len(tokens)):
    ticketnumber = tokens[i]
    k=i+1
    url = 'https://dev22908.service-now.com/api/now/table/ticket?sysparm_query=number%3D'+ticketnumber+'&sysparm_fields=assigned_to&sysparm_limit=1'

    # Eg. User name="admin", Password="admin" for this code sample.
    user = 'admin'
    pwd = 'SALESforce@2017'

    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}

    # Do the HTTP request
    response = requests.get(url, auth=(user, pwd), headers=headers  )

    # Check for HTTP codes other than 200
    if response.status_code != 200: 
         print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
         exit()

    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    a=data['result']
    


    if len(a)!=0:
      b=a[0]
      #print(b['assigned_to']['value'])
      
      return b['assigned_to']['value']
    else:
       
        if k >= len(tokens): 
          #print('No ticket found to this ticket id')
          return 'No ticket found to this ticket id'
#####-----------------CREATE NEW TICKET------------------------------------
        
	
	
def create_new_ticket(shortDescription):
    url = 'https://dev34634.service-now.com/api/now/table/ticket'

   # Eg. User name="admin", Password="admin" for this code sample.
    user = 'admin'
    pwd = 'SALESforce@2017'
    # Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    dat={}
    dat['short_description']=shortDescription
    dat2 = json.dumps(dat)
	# Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers ,data=dat2)

	# Check for HTTP codes other than 200
    if response.status_code != 201: 
       print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
       exit()
    # Decode the JSON response into a dictionary and use the data
    data = response.json()
    a=data['result']['number']
   # print(a)
    return data
####----------CREATE NEW INCIDENT--------------------------------------------
	
	
def create_new_incident(shortDescription):
	# Set the request parameters
    url = 'https://dev22908.service-now.com/api/now/table/incident'

  # Eg. User name="admin", Password="admin" for this code sample.
    user = 'admin'
    pwd = 'LqEZaDk8yU8x'# Set proper headers
    headers = {"Content-Type":"application/json","Accept":"application/json"}
    dat={}
    dat['short_description']=shortDescription
    dat2 = json.dumps(dat)
	# Do the HTTP request
    response = requests.post(url, auth=(user, pwd), headers=headers ,data=dat2)

	# Check for HTTP codes other than 200
    if response.status_code != 201: 
       print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
       exit()

    data = response.json()
    a=data['result']['number']
   # print(a)
    return data	
	
####-----------------GET 5 TIKCETS------------------------------------		
def get_last5_tickets():
	# Set the request parameters
	url = 'https://dev22908.service-now.com/api/now/table/ticket?sysparm_query=&sysparm_fields=short_description%2Cnumber%2Cstate%2Cactive%2Cdescription%2Csys_created_by&sysparm_limit=1000'
	user = 'admin'
	pwd = 'SALESforce@2017'
	# Set proper headers
	headers = {"Content-Type":"application/json","Accept":"application/json"}

	# Do the HTTP request
	response = requests.get(url, auth=(user, pwd), headers=headers  )

	# Check for HTTP codes other than 200
	if response.status_code != 200: 
		print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
		exit()

	# Decode the JSON response into a dictionary and use the data
	data = response.json()
	a=data['result']
	return a
###--------------------------------------------------------------------###   
        
    
def ticket_assignee_check_servicenow(answer,bot_msg,bot_msg2):
    issue_id = Get_Assignee(answer)
    if issue_id!=0:
        return 'Your ticket assignee is -'+issue_id
    else:
        str1="I am sorry, Your Issue id is not valid. Please check."
        if bot_msg2 ==str1:
            return "Sorry, please try again with correct information."
        else:
            return "I am sorry, Your Issue id is not valid. Please check."



def ticket_log_check_servicenow(answer,bot_msg,bot_msg2):
    a = get_last5_tickets()
    if i==2 and 'yes'.lower() in answer.lower() or 'ya' in answer.lower() or'yaa' in answer.lower() or'yo' in answer.lower() or 'yoo' in answer.lower() or'yup' in answer.lower() or 'yeah' in answer.lower() or 'right' in answer.lower() or 'totally' in answer.lower():
        print('Your last 5 logged issues are -')
        a = get_last5_tickets()
        s='Your last 5 logged issues are -'
        for b in range(len(a)-5,len(a)):
          issue_id=a[b]['number']
          s+=str('<br>'+issue_id)
          #print(issue_id)
         # i-=1
        return s
    elif 'na'.lower() in answer.lower() or 'no' in answer.lower() or'nops' in answer.lower():
        return "Sorry,then please ask again, with more information"
    else:
        return "Sorry Did not understand. Please clearify your query"
    



def issue_create_servicenow(answer,bot_msg,bot_msg2):
    data = create_new_ticket(answer)
    
    if data:
        flag=("Your Ticket is logged with given information <br>Ticket id=("+str(data['result']['number'])+")-"+str('Acitve= '+data['result']['active'])+"<br>"+str('Short Description= '+data['result']['short_description']))
   
       # print('Ticket id= '+data['result']['number'])
        #print('Acitve= '+data['result']['active'])
       # print('Short Description= '+data['result']['short_description'])
        return flag
    else:
        str1="I am sorry, Your Issue is not valid. Please check."
        if messages[len(messages)-3] ==str1 and messages[len(messages)-2] ==str1:
            return "Sorry, please try again with correct information."
        else:
            return "I am sorry, Your Issue is not valid. Please check."

def incident_create_servicenow(answer,bot_msg,bot_msg2):
    data = create_new_incident(answer)
    if  data:
        flag=("Your Incident is logged with given information <br>Incident id=("+str(data['result']['number'])+")-"+str('Acitve= '+data['result']['active'])+"<br>"+str('Short Description= '+data['result']['short_description'])+"<br> Or please contact Carl Haste at haste_carl@lilly.com<mailto:haste_carl@lilly.com")
       # print('Incident id= '+data['result']['number'])
       # print('Acitve= '+data['result']['active'])
       #print('Short Description= '+data['result']['short_description'])
        return flag
    else:
        str1="I am sorry, Your Issue is not valid. Please check."
        if messages[len(messages)-3] ==str1 and messages[len(messages)-2] ==str1:
            return "Sorry, please try again with correct information."
        else:
            return "I am sorry, Your Issue is not valid. Please check."       

def get_knowledge_servicenow(shortDescription,botmsg,botmsg2):
    data = get_knowledge(shortDescription)
    return 'Please visit the link for Details<br><a target="_blank" href="'+data+'"><font color="FF00CC">'+data+'</font></a>'

    
    


