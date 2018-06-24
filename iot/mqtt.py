from paho.mqtt import client
import paho.mqtt.subscribe as subscribe

import iot.models

from threading import Timer
from smart_home.celery import app

MQTT_USER = "bzxuzryj"
MQTT_PASS = "NK7BEO4cSB7k"
MQTT_HOST = "m23.cloudmqtt.com"
MQTT_PORT = 16547


def on_connect(client, userdata, flags, rc):
    print("Connected with result code: %s" % rc)
    # print(client, userdata, flags)
    client.subscribe("liveroom")


def on_message(client, userdata, msg):
    print("%s: %s" % (msg.topic, msg.payload.decode('utf-8')))
    update_liveroom_data(msg.payload.decode('utf-8'))


@app.task
def mqtt_start():
    '''
    запускать отдельным процессом mqtt_start.delay()
    '''
    subscriber = client.Client(client_id="ESP8266_liveroom")
    subscriber.on_connect = on_connect
    subscriber.on_message = on_message
    subscriber.username_pw_set(MQTT_USER, password=MQTT_PASS)
    subscriber.connect_async(MQTT_HOST, MQTT_PORT)
    subscriber.loop_start()
    print('mqtt started')


def update_liveroom_data(a):
    print('@app.task <update_liveroom_data>: starting update...')
    task = iot.models.Liveroom()
    task.update_data(a)


"""
a = mqtt_start()
print(a)

for x in range(1000):
    a = x**1000000
    print("----------------------")
    #print(a)
"""
"""
t = Timer(10, mqtt_start)
t.start()
ненужные коннекты!
"""
