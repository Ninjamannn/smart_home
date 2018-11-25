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
    location = models.CharField('Location', max_length=30)
    type_sensor = models.CharField('Type_sensor', max_length=30)
    temp_value = models.FloatField()
    hum_value = models.FloatField()
    datetime = models.DateTimeField('Created Date')

    def update_data(self, data):
        print('Model<{}>: update data...'.format(self.__class__.__name__))
        self.location = 'Liveroom'
        self.type_sensor = 'Dht11 + DS18B20 (MQQT method)'
        self.temp_value = round(data["ds18b20"], 1)
        self.hum_value = data["dht"]["hum"]
        self.datetime = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")
        self.save()
        print('Model<{}>: update OK'.format(self.__class__.__name__))

    def __str__(self):
        return "loc: %s | temp: %s | hum: %s | date: %s" % (self.location, self.temp_value,
                                                            self.hum_value, self.datetime)
