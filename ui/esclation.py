import mail_attach


def esclation_handle(msg,bot_msg,bot_msg2):
	answer = ['want to send mail to access financial','want to speak our person now','want us to give you a call back']
	return answer
	
	
def send_mail(msg,bot_msg,bot_msg2):
	return 'please provide your name, contact and email, so I can send mail to Access Financial.'
	

def contact_person(msg,bot_msg,bot_msg2):
	return 'Please provide your name , I will take you to the live person.'
	
def call_back(msg,bot_msg,bot_msg2):
	return 'please provide your name, contact and email,so our person can call you'
	
def initiate_mail(msg,bot_msg,bot_msg2):

	response = mail_attach.mailsend('meon.co.in',str(msg),"enquiry")
	
	return response 
	

def start_chat(msg,bot_msg,bot_msg2):

	return 'This is Rahul from access financial, How can i help you today?'


def start_call(msg,bot_msg,bot_msg2):
	
	response = mail_attach.mailsend('meon.co.in',str(msg),"enquiry")
	
	return response


