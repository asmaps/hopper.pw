#!/bin/bash

python manage.py migrate --noinput
if [ "$1" = 'worker' ]; then
    celery -n hopperpw.%h -A hopperpw worker -B --loglevel=info
else
    python manage.py collectstatic --noinput
    gunicorn hopperpw.wsgi:application --log-level=info -b "0.0.0.0:8000"
fi
