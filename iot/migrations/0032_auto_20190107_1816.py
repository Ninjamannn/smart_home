# Generated by Django 2.0.8 on 2019-01-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0031_auto_20180626_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoilerRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default=None, max_length=20, verbose_name='BoilerRoom')),
                ('type_sensor', models.CharField(default=None, max_length=10, verbose_name='Type_sensor')),
                ('value', models.FloatField(default=None, verbose_name='Value')),
                ('type_value', models.CharField(default=None, max_length=10, verbose_name='Type_value')),
                ('datetime', models.DateTimeField(default='2019-01-07 18:16', verbose_name='Created Date')),
            ],
        ),
        migrations.RemoveField(
            model_name='liveroom',
            name='hum_value',
        ),
        migrations.RemoveField(
            model_name='liveroom',
            name='temp_value',
        ),
        migrations.AddField(
            model_name='liveroom',
            name='type_value',
            field=models.CharField(max_length=10, null=True, verbose_name='Type_value'),
        ),
        migrations.AddField(
            model_name='liveroom',
            name='value',
            field=models.FloatField(null=True, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='bathroom',
            name='datetime',
            field=models.DateTimeField(default='2019-01-07 18:16', verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='bathroom',
            name='hum_value',
            field=models.FloatField(default=None, verbose_name='hum_value'),
        ),
        migrations.AlterField(
            model_name='bathroom',
            name='location',
            field=models.CharField(default=None, max_length=30, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='bathroom',
            name='temp_value',
            field=models.FloatField(default=None, verbose_name='temp_value'),
        ),
        migrations.AlterField(
            model_name='bathroom',
            name='type_sensor',
            field=models.CharField(default=None, max_length=30, verbose_name='Type_sensor'),
        ),
        migrations.AlterField(
            model_name='liveroom',
            name='datetime',
            field=models.DateTimeField(default='2019-01-07 18:16', verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='liveroom',
            name='location',
            field=models.CharField(max_length=20, null=True, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='liveroom',
            name='type_sensor',
            field=models.CharField(max_length=10, null=True, verbose_name='Type_sensor'),
        ),
    ]
