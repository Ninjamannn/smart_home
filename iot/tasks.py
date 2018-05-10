import time

import iot.models
import json
import urllib.request
from smart_home.celery import app


@app.task
def get_temp():
    print('@app.task <get_temp>: starting request api.thingspeak...')
    response = urllib.request.urlopen('https://api.thingspeak.com/channels/120869/feeds.json?results=1')
    data = response.read()
    encoding = response.info().get_content_charset()
    JSON_object = json.loads(data.decode(encoding))

    temp = float(JSON_object['feeds'][0]['field1'])
    humidity = float(JSON_object['feeds'][0]['field2'])
    print('@app.task <get_temp>: data received!')
    return temp, humidity


# celery worker -A smart_home --loglevel=debug --pool=eventlet [--concurrency=2] win
# celery worker -A smart_home --loglevel=debug --concurrency=2    linux
# celery -A smart_home beat


@app.task
def update_dht22():
    print('@app.task <update_dht22>: starting update dht22...')
    dht22 = iot.models.Dht22()
    dht22.update_data()
    print('@app.task <update_dht22>: data has been updated from %s' % dht22.location)
