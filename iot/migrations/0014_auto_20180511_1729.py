# Generated by Django 2.0.4 on 2018-05-11 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0013_auto_20180510_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dht22',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='dht22',
            name='location',
            field=models.CharField(max_length=30, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='dht22',
            name='type_sensor',
            field=models.CharField(max_length=30, verbose_name='Type_sensor'),
        ),
    ]