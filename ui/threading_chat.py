class Room(object):

    def __init__(self):
        self.users = set()
        self.messages = ['fg','dg','dc']

    def backlog(self, size=25):
        return self.messages[-size:]

   
    def add(self, message):
        
        self.messages.append(message)

rooms = {
    'admin': Room(),
    'surbhi': Room(),
}
users = {}

messages=['fg','dg','dc']


