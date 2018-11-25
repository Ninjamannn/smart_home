from paho.mqtt import client
import iot.models
import json
from smart_home.celery import app
from decouple import config


MQTT_USER = config('MQTT_USER', cast=str)
MQTT_PASS = config('MQTT_PASS', cast=str)
MQTT_HOST = config('MQTT_HOST', cast=str)
MQTT_PORT = config('MQTT_PORT', cast=int)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code: %s" % rc)
    client.subscribe("liveroom")


def on_message(client, userdata, msg):
    print("%s: %s" % (msg.topic, msg.payload.decode('utf-8')))
    data = msg.payload.decode('utf-8')
    update_liveroom_data(json.loads(data))


@app.task
def mqtt_start():
    '''
    запускать отдельным процессом mqtt_start.delay()
    '''
    subscriber = client.Client(client_id="ESP8266_liveroom44")  # TODO: change id for prod.
    subscriber.on_connect = on_connect
    subscriber.on_message = on_message
    subscriber.username_pw_set(MQTT_USER, password=MQTT_PASS)
    subscriber.connect_async(MQTT_HOST, MQTT_PORT)
    subscriber.loop_start()
    print('mqtt started')


def update_liveroom_data(data):
    print('@app.task <update_liveroom_data>: starting update...')
    task = iot.models.Liveroom()
    task.update_data(data)
