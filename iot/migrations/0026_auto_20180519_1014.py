# Generated by Django 2.0.4 on 2018-05-19 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0025_auto_20180518_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dht22bathroom',
            name='datetime',
            field=models.DateTimeField(default='2018-05-19 10:14:53', verbose_name='Created Date'),
        ),
    ]
