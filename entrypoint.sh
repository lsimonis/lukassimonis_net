#!/bin/bash

# Prepare log files and start outputting logs to stdout
touch ./logs/gunicorn.log
touch ./logs/gunicorn-access.log
tail -n 0 -f ./logs/gunicorn*.log &

export DJANGO_SETTINGS_MODULE=lukassimonis_net.settings

exec gunicorn lukassimonis_net.wsgi \
    --name lukassimonis_net_django \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --log-level=info \
    --log-file=./logs/gunicorn.log \
    --access-logfile=./logs/gunicorn-access.log \
"$@"
