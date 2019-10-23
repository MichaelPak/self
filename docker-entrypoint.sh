#!/bin/sh
sleep 10  # wait postgres
python manage.py migrate
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers 3