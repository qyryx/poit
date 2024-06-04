# import Adafruit_DHT
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import time
import random
import threading

app = Flask(__name__, static_url_path='/static')

is_streaming = True

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


def background_task():
    while True:
        temperature = random.uniform(0, 40)
        humidity = random.uniform(0, 100)
        data = {'temperature': round(temperature, 1), 'humidity': round(humidity, 1)}
        socketio.emit('data_update', data, namespace='/data')
        time.sleep(1)


@app.route('/')
def root():
    return render_template('start.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/gauge')
def logging():
    return render_template('gauge.html')


@app.route('/graph')
def graph():
    return render_template('graph.html')


@app.route('/start', methods=['POST'])
def start_stream():
    global is_streaming
    is_streaming = True
    return jsonify({"status": "started"})


@app.route('/stop', methods=['POST'])
def stop_stream():
    global is_streaming
    is_streaming = False
    return jsonify({"status": "stopped"})


@app.route('/metrics')
def metrics():
    global is_streaming
    if is_streaming:
        temperature = random.uniform(10, 30)
        humidity = random.uniform(10, 100)
        return jsonify(temperature=temperature, humidity=humidity)
    # global is_streaming
    # if is_streaming:
    #     sensor = Adafruit_DHT.DHT11
    #     pin = 4
    #     humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    #     return jsonify(temperature=temperature, humidity=humidity)
    # else:
    #     return jsonify(temperature=None, humidity=None)


@socketio.on('connect', namespace='/data')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect', namespace='/data')
def handle_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    bg_thread = threading.Thread(target=background_task)
    bg_thread.daemon = True
    bg_thread.start()
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
