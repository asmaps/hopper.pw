# coding=utf-8

from __future__ import absolute_import

from django.conf import ImproperlyConfigured

from .base import *


# ######### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
# ######### END DEBUG CONFIGURATION

# ######### EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# ######### END EMAIL CONFIGURATION

# ######### CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# ######### END CACHE CONFIGURATION

# ######### TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
)
# ######### END TOOLBAR CONFIGURATION

try:
    from .local_settings import *
except ImportError as e:
    raise ImproperlyConfigured(
        'Please add a local_setting.py in the settings folder for your local untracked settings.'
    )

# ######### DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
if not DATABASES:
    raise ImproperlyConfigured(
        '''
        Please add DATABASES setting to your local_settings.py.
        See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
        Example:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'cinderella',
                'USER': 'cinderella',
                'PASSWORD': 'secret',
                'HOST': 'localhost',
                'PORT': '',
            }
        }
        ''')
# ######### END DATABASE CONFIGURATION

SECRET_KEY = 'ohsoverysecret'