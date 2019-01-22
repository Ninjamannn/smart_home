from datetime import datetime
from django.db import models
from iot.tasks import bathroom_data


class Bathroom(models.Model):
    location = models.CharField('Location', max_length=30)
    type_sensor = models.CharField('Type_sensor', max_length=30)
    temp_value = models.FloatField()
    hum_value = models.FloatField()
    datetime = models.DateTimeField('Created Date')

    def update_data(self):
        print('Model<Bathroom>: update data...')
        temp, hum = bathroom_data()
        self.location = 'Bathroom'
        self.type_sensor = 'Dht22 (HTTP method)'
        self.temp_value = temp
        self.hum_value = hum
        self.datetime = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")
        self.save()
        print('Model<Bathroom>: update OK')

    @staticmethod
    def get_data():
        result = bathroom_data.delay()
        temp, hum = result.get()
        return temp, hum

    def __str__(self):
        return "loc: %s | temp: %s | hum: %s | date: %s" % (self.location, self.temp_value,
                                                            self.hum_value, self.datetime)


class Liveroom(models.Model):
    """
    use MQTT method
    broker - www.cloudmqtt.com
    """
    location = models.CharField('Location', max_length=20, null=True)
    type_sensor = models.CharField('Type_sensor', max_length=10, null=True)
    value = models.FloatField('Value', null=True)
    type_value = models.CharField('Type_value', max_length=10, null=True)
    datetime = models.DateTimeField('Created Date', default=datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M"))

    def save_data(self, data, topic):
        print('Model <{}>: update data...'.format(self.__class__.__name__))
        self.location = 'Liveroom'
        self.type_sensor = topic.split('/')[2]
        self.type_value = topic.split('/')[-1]
        self.value = round(float(data), 1)
        self.datetime = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")
        self.save()
        print('Model <{}>: save data'.format(self.__class__.__name__))

    def __str__(self):
        return "location: %s | value: %s | type_value: %s | date: %s" % (self.location, self.value,
                                                                         self.type_value, self.datetime)


class BoilerRoom(models.Model):
    """
    use MQTT method
    broker - www.cloudmqtt.com
    """
    location = models.CharField('BoilerRoom', max_length=20, default=None)
    type_sensor = models.CharField('Type_sensor', max_length=10, default=None)
    value = models.FloatField('Value', default=None)
    type_value = models.CharField('Type_value', max_length=10, default=None)
    datetime = models.DateTimeField('Created Date', default=datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M"))

    def save_data(self, data, topic):
        print('Model <{}>: update data...'.format(self.__class__.__name__))
        self.location = 'Boiler_room'
        self.type_value = 'temp'
        self.type_sensor = topic.split('/')[2]
        self.value = round(float(data), 1)
        self.datetime = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")
        self.save()
        print('Model <{}>: save data'.format(self.__class__.__name__))

    def __str__(self):
        return "loc: %s | temp: %s | hum: %s | date: %s" % (self.location, self.value,
                                                            self.type_sensor, self.datetime)
