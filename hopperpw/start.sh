#!/bin/bash

cd hopperpw
python3 manage.py migrate --noinput
if [ "$1" = 'worker' ]; then
    celery -n hopperpw.%h -A project worker -B --loglevel=info
else
    python3 manage.py collectstatic --noinput
    gunicorn hopperpw.wsgi:application --log-level=info -b "0.0.0.0:8000"
fi
