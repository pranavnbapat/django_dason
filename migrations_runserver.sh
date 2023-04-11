#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Rebuild Elasticsearch search index
echo "Rebuilding Elasticsearch search index..."
python manage.py search_index --rebuild

# Start the Django app
echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8080
