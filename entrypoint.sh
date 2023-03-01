#!/bin/bash

# Run migrations and start the server 
python manage.py makemigrations
python manage.py migrate 
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000

echo Running eShop application on the local host at http://localhost:8082