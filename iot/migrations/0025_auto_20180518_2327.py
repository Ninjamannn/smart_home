# Generated by Django 2.0.4 on 2018-05-18 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0024_auto_20180518_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dht22bathroom',
            name='datetime',
            field=models.DateTimeField(verbose_name='Created Date'),
        ),
    ]