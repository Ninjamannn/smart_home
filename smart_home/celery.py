from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_home.settings')

app = Celery('smart_home')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'iot.tasks.update_dht22_bathroom',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0, '*/5')` if you want it to run daily at midnight
    },
}