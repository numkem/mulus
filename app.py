from flask import Flask, json, render_template
from flask.ext.socketio import SocketIO, emit
from flask.ext.bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
import datetime


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '870FKAJE@h41lk1408f09j#%!@'
socketio = SocketIO(app)
Bootstrap(app)
toolbar = DebugToolbarExtension(app)

users = []

def sendMessage(event, message, user='Bot', broadcast=False):
    emit(event, {
        'date': datetime.datetime.now(),
        'message': message,
        'username': user,
    }, broadcast=broadcast)

@app.route('/')
def index():
    return render_template('index.html')

def send_motd():
    sendMessage('motd', 'Hello, welcome to this makeshift chat server!')

def send_userList():
    sendMessage('users', {'users': users})

@socketio.on('connect', namespace='/chat')
def connect():
    send_motd()
    send_userList()

@socketio.on('setUser', namespace='/chat')
def set_user(message):
    if message['username'] not in users:
        users.append(message['username'])
    send_userList()

@socketio.on('disconnect', namespace='/chat')
def bye():
    sendMessage('bye', 'Bye bye!')

@socketio.on('msg-in', namespace='/chat')
def message(message):
    sendMessage('msg-out', message['message'], user=message['username'], broadcast=True)


if __name__ == '__main__':
    socketio.run(app, '0.0.0.0', 5000)