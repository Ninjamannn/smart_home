from datetime import datetime
from django.db import models
from django.db.models import DateField
from django.utils import timezone
from django.conf import settings
from iot.tasks import bathroom_data
#from django.contrib.auth import get_user_model


class Dht22Bathroom(models.Model):
    location = models.CharField('Location', max_length=30)
    type_sensor = models.CharField('Type_sensor', max_length=30)
    temp_value = models.FloatField()
    hum_value = models.FloatField()
    #date = models.DateTimeField('Created Date', default=timezone.localtime(timezone.now()))
    #date = models.DateTimeField('Created Date', auto_now=True, editable=True) не отоюражает в админ
    datetime = models.DateTimeField('Created Date')

    def update_data(self):  # В конструкторе инициализацию нельзя!
        print('Model<Dht22Bathroom>: update data...')
        temp, hum = bathroom_data()
        self.location = 'Bathroom'
        self.type_sensor = 'Dht22 (HTTP method)'
        self.temp_value = temp
        self.hum_value = hum
        #self.datetime = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        self.datetime = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")
        self.save()
        print('Model<Dht22Bathroom>: update OK')

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
    temp_value = models.CharField('DATA', max_length=30)

    datetime = models.DateTimeField('Created Date')

    def update_data(self, a):
        print('Model<{}>: update data...'.format(self.__class__.__name__))
        self.location = 'Liveroom'
        self.type_sensor = 'Dht11 + DS18B20 (MQQT method)'
        self.temp_value = a

        self.datetime = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")
        self.save()
        print('Model<{}>: update OK'.format(self.__class__.__name__))

    def __str__(self):
        return "loc: %s | temp: %s | date: %s" % (self.location, self.temp_value, self.datetime)
