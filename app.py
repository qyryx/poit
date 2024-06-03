from flask import Flask, render_template, jsonify
import Adafruit_DHT

app = Flask(__name__, static_url_path='/static')

is_streaming = False


@app.route('/')
def root():
    return render_template('start.html')


@app.route('/index')
def index():
    return render_template('index.html')



