#!/bin/bash

python manage.py makemigrations

python manage.py migrate


if [ "$APP_NAME" = "django" ]; then
    
    python manage.py tsetmctask
    
    python manage.py runserver 0.0.0.0:8000

elif [ "$APP_NAME" = "celery-worker" ]; then
    
    celery -A maskanib_test worker --loglevel=info

elif [ "$APP_NAME" = "celery-beat" ]; then

    celery -A maskanib_test beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler

else
    echo "Invalid APP_NAME specified."
fi

