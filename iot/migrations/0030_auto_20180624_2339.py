# Generated by Django 2.0.4 on 2018-06-24 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0029_auto_20180621_1835'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dht22Bathroom',
            new_name='Bathroom',
        ),
    ]