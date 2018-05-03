import esclation
def virtual_agent_function(typeofaction,msg,bot_msg,bot_msg2):
    typeofaction=typeofaction.strip()
   
    if typeofaction=='esclation_handle':
    	
        return esclation.esclation_handle(msg,bot_msg,bot_msg2)
    elif typeofaction=='contact_person':
    	return esclation.contact_person(msg,bot_msg,bot_msg2)
    	
    elif typeofaction=='call_back':
    	return esclation.call_back(msg,bot_msg,bot_msg2)
    	
    elif typeofaction=='send_mail':
    	return esclation.send_mail(msg,bot_msg,bot_msg2)
    	
    elif typeofaction=='start_chat':
    	return esclation.start_chat(msg,bot_msg,bot_msg2)
    	
    elif typeofaction=='start_call':
    	return esclation.start_call(msg,bot_msg,bot_msg2)
    	
    elif typeofaction=='initiate_mail':
    	return esclation.initiate_mail(msg,bot_msg,bot_msg2)
        
   

def add_attach(path):
    jira_call.add_attach(path)
