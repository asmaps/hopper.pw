# coding=utf-8
import os
from os.path import dirname, abspath
from sys import path

SITE_ROOT = dirname(dirname(abspath(__file__)))
path.append(SITE_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hopperpw.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
