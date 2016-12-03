from flask import *
from flask_socketio import SocketIO
import things
import time

app = Flask(__name__)
socketio = SocketIO(app)
pi_things = things.PiThings()

@app.route("/")
def hello():
      button = pi_things.read_button()
      return render_template('index.html', button=button)


@socketio.on('change_led')
def change_led(led):
    if led == 'on':
        pi_things.set_led(True)
    elif led == 'off':
        pi_things.set_led(False)

def button_change(button):
    socketio.emit('button_change', { 'button': button })


if __name__ == "__main__":
    pi_things.on_button_change(button_change)
    socketio.run(app, host='0.0.0.0', debug=True, port=80)
