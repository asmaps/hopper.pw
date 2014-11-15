# coding=utf-8

from __future__ import absolute_import

from .base import *


# ######### IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}