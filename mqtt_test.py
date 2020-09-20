import paho.mqtt.client as mqtt 

def read_data(data):
    #print(data)
    myClient = mqtt.Client("led_publisher")       # setting up a client with a client_ID
    myClient.connect("localhost", 1883)
    myClient.publish("house/led_control",data)
