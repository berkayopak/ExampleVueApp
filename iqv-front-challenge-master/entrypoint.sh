#!/usr/bin/env sh

WEB_COMMAND='gunicorn --bind 0.0.0.0:5000 challenge.web -k uvicorn.workers.UvicornWorker'

echo "First arg: $1"

if [ -t 1 ]; then
  standout="\e[1m"
  standin="\e[0m"
fi

case $1 in
    web)
        echo -e "Running $standout$WEB_COMMAND$standin"
        exec $WEB_COMMAND
        ;;
esac