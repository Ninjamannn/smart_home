# Generated by Django 2.0.4 on 2018-05-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0005_auto_20180510_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dht22',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Created Date'),
        ),
    ]
