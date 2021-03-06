# Generated by Django 2.0.4 on 2018-04-18 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dht22',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30, verbose_name='Title')),
                ('type_sensor', models.CharField(max_length=30, verbose_name='type_sensor')),
                ('temp_value', models.FloatField()),
                ('hum_value', models.FloatField()),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 4, 18, 17, 45, 55, 390013), verbose_name='Created Date')),
            ],
        ),
    ]
