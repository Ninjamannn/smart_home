from paho.mqtt import client
import json
from decouple import config
import logging
from iot.models import Liveroom, BoilerRoom

# create logger
log = logging.getLogger('mqtt_application')
log.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create file handler which logs even debug messages
fh = logging.FileHandler('mqtt.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
log.addHandler(fh)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
log.addHandler(ch)


# rooms = {
#     'boiler_room': {'topic': 'boiler_room/sensors/ds18b20', 'model': None},
#     'living_room': {'topic': 'boiler_room/sensors/dht22/#', 'model': Liveroom}
# }

rooms = {
    'boiler_room': {'ds18b20': BoilerRoom, 'dht22': Liveroom},
}

MQTT_USER = config('MQTT_USER', cast=str)
MQTT_PASS = config('MQTT_PASS', cast=str)
MQTT_HOST = config('MQTT_HOST', cast=str)
MQTT_PORT = config('MQTT_PORT', cast=int)


def on_connect(client, userdata, flags, rc):
    log.info(f'Connected with result code: {rc}')
    client.subscribe([('boiler_room/sensors/ds18b20', 0), ('boiler_room/sensors/dht22/#', 0)])


def on_message(client, userdata, msg):
    log.info(f"{msg.topic}: {msg.payload.decode('utf-8')}")
    data = msg.payload.decode('utf-8')
    save_room_data(data, msg.topic)


def on_disconnect(client, userdata, rc):
    """
    loop_stop for resolve extra connections
    """
    if rc != 0:
        log.info(f"Unexpected MQTT disconnection ERROR - {rc}")
        log.info(f"stop extra connections...")
        client.loop_stop()


def mqtt_start():
    subscriber = client.Client(client_id="testing_mode")  # TODO: change id for prod.
    subscriber.username_pw_set(MQTT_USER, password=MQTT_PASS)
    subscriber.on_connect = on_connect
    subscriber.on_message = on_message
    subscriber.on_disconnect = on_disconnect
    subscriber.connect_async(MQTT_HOST, MQTT_PORT)
    subscriber.loop_start()
    #subscriber.loop_forever()
    log.info('mqtt service started')


def save_room_data(data, topic):
    if data == 'nan':
        log.error(f'inconsistent data from mqtt: topic - {topic}, data - {data}')
        return None
    room = topic.split('/')[0]
    type_sensor = topic.split('/')[2]
    try:
        model = rooms[room][type_sensor]
    except KeyError as error:
        log.error(f'{error}, required model not found! data from mqtt not save!')
        return None
    task = model()
    task.save_data(data, topic)
