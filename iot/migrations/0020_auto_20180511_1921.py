# Generated by Django 2.0.4 on 2018-05-11 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0019_remove_dht22_local_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dht22',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Created Date'),
        ),
    ]