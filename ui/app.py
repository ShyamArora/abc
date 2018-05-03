# Micro gevent chatroom.
# ----------------------
# Make things as simple as possible, but not simpler.

from flask import Flask, render_template, request, json, redirect, url_for,session,escape
from flask_restful import Resource, Api
from flask import jsonify
from gevent import queue
from gevent.pywsgi import WSGIServer
import prof_check
import app1
#import speech_to_text
import datetime
app = Flask(__name__)
app.debug = True
api = Api(app)
##conn = psycopg2.connect(database = "chatroom", user = "postgres", password = "mohitsain97", host = "127.0.0.1", port = "5432")
##cur = conn.cursor()
##
##'''
##@app.route('/speech', methods=['POST'])
##def speech_():
##    msg=speech_to_text.speech_to_text_()
##    print("cd"+msg)
##    return jsonify( { 'text': msg } )'''
##    
##class Room(object):
##
##    def __init__(self):
##        self.users = set()
##        self.messages = []
##
##    def backlog(self, size=5000):
##        return self.messages[-size:]
##
##    def subscribe(self, user):
##        self.users.add(user)
##
##    def add(self, message):
##        for user in self.users:
##            
##            user.queue.put_nowait(message)
##        self.messages.append(message)
##
##class User(object):
##
##    def __init__(self):
##        self.queue = queue.Queue()
##
##rooms = {
##    'Room-1': Room(),
##    'Room-2': Room(),
##}
##
##users = {}
##@app.route('/', methods = ['GET', 'POST'])
##def choose_name():
##    
##    error = None
##    if request.method == 'POST':
##        
##        if not request.form['username'] == "" :
##            print(request.form['username'])
##            
##            return redirect(url_for('main',uid=request.form['username']))
##        else:
##            error = "The user name you entered isn't correct. Try entering it again."
##    return render_template('login.html', error=error)
##
##
##"Tagging user"
##@app.route('/<uid>')
##def main(uid):
##    return render_template('main.html',
##        uid=uid,
##        rooms=rooms.keys()
##    )
##
##"Tagging room to user"
##@app.route('/<room>/<uid>')
##def join(room, uid):
##    user = users.get(uid, None)
##    if not user:
##        users[uid] = user = User()
##    
##    active_room = rooms[room]
##    active_room.subscribe(user)
##    messages = active_room.backlog()
##    print(users)
##    return render_template('room.html',
##        room=room, uid=uid, messages=messages,data="This is a fantain chatroom, you can talk here.")
##
##
##"For msg pushing in the room"
##@app.route("/put/<room>/<uid>", methods=["POST"])
##def put(room, uid):
##    user = users[uid]
##    room = rooms[room]
##    
##    message = request.form['message']
##    print(message)
##    room.add(':'.join([uid, message]))
##
##    return ''
##"For msg giving back in the chatroom"
##@app.route("/poll/<uid>", methods=["POST"])
##def poll(uid):
##    try:
##        msg = users[uid].queue.get(timeout=1000)
##    except queue.Empty:
##        msg = []
##    print(msg)
##   
##    user=''
##    message=''
##    if not msg==[]:
##        user=msg.split(":")[0]
##        message=msg.split(":")[1]
##    if prof_check.check_prof(message)==False:
##        message="It seems to be a false language. Please avoid using these terms here."
##        check="false"
##    else:
##        check="true"
##    return jsonify({'user':user,'msg':message,'check':check})
##    
def abc(msg):
    return app1.reply(msg)
    


    
"rest api's"
class CreateRoom(Resource):
    def get(self,room):
        
        
##        cur.execute("INSERT INTO room VALUES ('"+str(room)+"')")
##        conn.commit
        a=abc(room)
        return a
##        
##    
api.add_resource(CreateRoom, '/message/<string:room>')      
## 
##class TagUserToRoom(Resource):
##    def get(self,user,room):
##        rooms[room].subscribe(user)
##        cur.execute("INSERT INTO room_user VALUES ('"+str(user)+"','"+str(room)+"')")
##        conn.commit
##        return "Tag to room success"
##        
##api.add_resource(TagUserToRoom, '/<string:user>/tagtoroom/<string:room>') 
##
##class DeleteRoom(Resource):
##    def get(self,room):
##        cur.execute("delete from room where roomid= %s",(room,))
##        conn.commit
##        del rooms[room]
##        
##        return ("delete room sucess")
##api.add_resource(DeleteRoom, '/Delete/room/<string:room>')  
##
##class MsgToRoom(Resource):
##    def put(self,room,uid):
##        user = users[uid]
##        room = rooms[room]
##        message = request.form['message']
##        cur.execute("INSERT INTO messages VALUES ('"+message+"','"+uid+"','"+room+"')")
##        conn.commit
##    
##        newmessage= ':'.join([uid, message])
##        room.add(newmessage)
##        msg = newmessage
##        user=''
##        message=''
##        if not msg==[]:
##            user=msg.split(":")[0]
##            message=msg.split(":")[1]
##        if prof_check.check_prof(message)==False:
##            message="It seems to be a false language. Please avoid using these terms here."
##            check="false"
##        else:
##            check="true"
##        return jsonify({'user':user,'msg':message,'check':check})
##        
##         
## 
##        
##        
##api.add_resource(MsgToRoom, '/message/to/room/    /<string:uid>')
##
##    
##            
        

if __name__ == "__main__":
    http = WSGIServer(('0.0.0.0', 5039), app)
    http.serve_forever()
    conn.close()
