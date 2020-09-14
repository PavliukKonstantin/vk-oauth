#!/bin/sh

if [ "$POSTGRES_DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      sleep 0.2
    done

    echo "PostgreSQL started"
fi

python manage.py migrate --noinput

exec "$@"
