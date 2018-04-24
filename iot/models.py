import datetime
from django.db import models
from django.db.models import DateField
from django.utils import timezone
from django.conf import settings
from iot.tasks import get_temp
#from django.contrib.auth import get_user_model


class Dht22(models.Model):
    location = models.CharField('Title', max_length=30)
    type_sensor = models.CharField('type_sensor', max_length=30)
    temp_value = models.FloatField()
    hum_value = models.FloatField()
    date = models.DateTimeField('Created Date', default=datetime.datetime.now())
    #date = models.DateTimeField(default=datetime.datetime.now)

    def update_data(self):  # В конструкторе инициализация лучше?
        print('update data...')
        temp, hum = get_temp()
        self.location = 'Bathroom'
        self.type_sensor = self.__class__.__name__
        self.temp_value = temp
        self.hum_value = hum
        self.date = datetime.datetime.now()
        self.save()

    @staticmethod
    def get_data():
        temp, hum = get_temp.delay()
        return temp, hum

    def __str__(self):
        return "loc: %s | temp: %s| hum: %s| date: %s" % (self.location, self.temp_value, self.hum_value, self.date)