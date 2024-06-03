from flask import Flask, render_template, jsonify
# import Adafruit_DHT

app = Flask(__name__, static_url_path='/static')

is_streaming = False


@app.route('/')
def root():
    return render_template('start.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/logging')
def logging():
    return render_template('logging.html')


@app.route('/metrics')
def metrics():
    # global is_streaming
    # if is_streaming:
    #     sensor = Adafruit_DHT.DHT11
    #     pin = 4
    #     humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    #     return jsonify(temperature=temperature, humidity=humidity)
    # else:
        return jsonify(temperature=None, humidity=None)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
