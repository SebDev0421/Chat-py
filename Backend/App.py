from flask import Flask, render_template
from flask_socketio import SocketIO, send

 
 
message = "Thank you"
 
# setup the parameters of the message
password = "pia0421"

 
app = Flask(__name__)
app.config['SECRET_KEY']='secret'





socketio = SocketIO(app, cors_allowed_origins="*")
@socketio.on('Connect')
def handle_message(msg):
    print(msg)
    socketio.emit('Connect client',msg)

@socketio.on('typing')
def typing_msg(usr):
    print('usr typing: ',usr)


@socketio.on('new message')
def new_message(data):
    print(data)
    socketio.emit('new message client',data)

@socketio.on('send email')
def send_email(email):
    print(email)
   
    

if __name__ == '__main__':
    socketio.run(app)