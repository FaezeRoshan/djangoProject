
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

app = Celery('djangoProject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('reza')

app.conf.beat_schedule = {
    'add-news-every-2-minutes': {
        'task': 'news.collectnews.addnews',
        'schedule': crontab(minute='*/2'),

    },
}