# import Adafruit_DHT
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import time
import random
import threading
import redis

app = Flask(__name__, static_url_path='/static')

is_streaming = True

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
stop_event = threading.Event()
bg_thread = None

data_log_file = 'data.log'
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


def write_to_data_log(data):
    with open(data_log_file, 'a') as file:
        file.write(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')} Temperature: {data['temperature']}°C Humidity: {data['humidity']}%\n")


def write_to_db(data):
    log_message = f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')} Temperature: {data['temperature']}°C Humidity: {data['humidity']}%"
    redis_client.rpush('data_log', log_message)


def background_task():
    while not stop_event.is_set():
        temperature = random.uniform(15, 25)
        humidity = random.uniform(40, 50)
        data = {'temperature': round(temperature, 1), 'humidity': round(humidity, 1)}
        write_to_data_log(data)
        write_to_db(data)
        socketio.emit('data_update', data, namespace='/data')
        for _ in range(10):
            if stop_event.is_set():
                break
            time.sleep(0.1)
        #     sensor = Adafruit_DHT.DHT11
        #     pin = 4
        #     humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        #     return jsonify(temperature=temperature, humidity=humidity)


@app.route('/')
def root():
    return render_template('start.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/gauge')
def gauge():
    return render_template('gauge.html')


@app.route('/graph')
def graph():
    return render_template('graph.html')


@app.route('/file')
def file():
    return render_template('file.html')


@app.route('/db')
def db():
    return render_template('db.html')


def read_data_log():
    data_list = []
    with open(data_log_file, 'r') as file:
        for line in file:
            data_list.append(line.strip())
    return data_list


@app.route('/from-file')
def get_data():
    data_list = read_data_log()
    return jsonify(data_list)


@app.route('/database')
def database():
    data_logs = redis_client.lrange('data_log', 0, -1)
    return jsonify([log.decode('utf-8') for log in data_logs])


@app.route('/start', methods=['POST'])
def start_stream():
    global bg_thread
    if bg_thread is None or not bg_thread.is_alive():
        stop_event.clear()
        bg_thread = threading.Thread(target=background_task)
        bg_thread.daemon = True
        bg_thread.start()
        return jsonify({"status": "started"})
    else:
        return jsonify({"status": "already running"})


@app.route('/stop', methods=['POST'])
def stop_stream():
    stop_event.set()
    if bg_thread is not None:
        bg_thread.join()
    return jsonify({"status": "stopped"})


@socketio.on('connect', namespace='/data')
def handle_connect():
    print("Client connected")


@socketio.on('disconnect', namespace='/data')
def handle_disconnect():
    print("Client disconnected")


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
