from flask import Flask, render_template, request, jsonify
import insta.fakefriends as ff
from pprint import pprint as pp
import numpy as np
from operator import itemgetter

from flask_socketio import SocketIO, emit, send
app = Flask(__name__)  # original
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('/index.html')


# socket.io
@socketio.on('my event', namespace='/test')
def test_message(message):
    print("my-event")
    clientID = request.sid
    print(socketio)
    print("socket sdi: {}".format(clientID))

    zeroLikes = ff.fakeFriends(message['username'])

    emit('zeroLikes', zeroLikes, room=clientID)


@socketio.on('status update', namespace='/test')
def statusUpdate(message):
    print("Update Status{}".format(socketio))
    emit('statusUpdate', {'data': message})


@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})
    print('Client connected')


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
