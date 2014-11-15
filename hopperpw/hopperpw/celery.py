# coding=utf-8
from __future__ import absolute_import

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hopperpw.settings.dev')

print '==========================', os.environ['DJANGO_SETTINGS_MODULE']

from celery import Celery
from django.conf import settings

app = Celery('hopperpw')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)