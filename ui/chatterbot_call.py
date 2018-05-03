from chatterbot import ChatBot

bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./database.sqlite3'
)

def chatbot_response_conf(msg):
  read_only=True
  response = bot.get_response(msg)
  if (response.confidence>0.8):
                b = str(response)
                
                return b
  else:
                return False


##def chatbot_response(msg):
##    return chatbot.get_response(msg)
##



def chatbot_response_conf_check(msg):
  response = bot.get_response(msg)
  if (response.confidence>0.92):
    return True
  else:
    return False
