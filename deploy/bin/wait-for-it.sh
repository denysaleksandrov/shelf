#!/bin/bash

host="$1"
shift
cmd="$@"

until psql -h "$host" -U "postgres" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing commands"
python3 /usr/src/app/manage.py migrate 
python3 /usr/src/app/manage.py collectstatic --noinput
echo "User.objects.create_superuser('admin', 'admin@example.com', 'Poclab123')" | python3 /usr/src/app/manage.py shell_plus

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn shelf.wsgi:application \
        --bind :8010 \
        --workers 3
