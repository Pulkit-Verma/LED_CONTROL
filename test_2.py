from flask import Flask, render_template, request
#import paho.mqtt.client as mqtt
import mqtt_test 
data= "global"
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('LED_test.html')

@app.route('/', methods=['POST','GET'])
def read_data():
    global data
    if request.method == 'POST':
        data = request.form['led']
        if data=="1":
            print("LED is",data)
            mqtt_test.read_data(data)
            return "LED ON!!"
        elif data=="0":
            print("LED is",data)
            mqtt_test.read_data(data)
            return "LED OFF!!"

