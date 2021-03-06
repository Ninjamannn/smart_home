# Generated by Django 2.0.4 on 2018-06-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0027_auto_20180519_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liveroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30, verbose_name='Location')),
                ('type_sensor', models.CharField(max_length=30, verbose_name='Type_sensor')),
                ('temp_value', models.FloatField()),
                ('datetime', models.DateTimeField(verbose_name='Created Date')),
            ],
        ),
    ]
