import time
import json
import urllib.request
import iot.models
from smart_home.celery import app

#from iot.mqtt import mqtt_start


@app.task
def bathroom_data():
    """
    :return: текущая температура и влажность ванной комнаты
    """
    print('@app.task <bathroom_data>: starting request api.thingspeak...')
    response = urllib.request.urlopen('https://api.thingspeak.com/channels/120869/feeds.json?results=1')
    data = response.read()
    encoding = response.info().get_content_charset()
    JSON_object = json.loads(data.decode(encoding))

    temp = float(JSON_object['feeds'][0]['field1'])
    humidity = float(JSON_object['feeds'][0]['field2'])
    print('@app.task <bathroom_data>: data received!')
    return temp, humidity


# celery worker -A smart_home --loglevel=debug --pool=eventlet [--concurrency=2] win
# celery worker -A smart_home --loglevel=debug --concurrency=2    linux
# celery -A smart_home beat
# pkill -9 -f 'celery worker'


@app.task
def update_dht22_bathroom():
    """
    app.conf.beat_schedule - crontab()
    """
    print('@app.task <update_dht22Bathroom>: starting update dht22...')
    dht22 = iot.models.Bathroom()
    dht22.update_data()
    print('@app.task <update_dht22Bathroom>: data has been updated from %s' % dht22.location)
