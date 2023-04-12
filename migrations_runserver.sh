#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

# Generate fake data
echo "Generating fake data..."
python3 generate_faker_data.py &

# Execute SQL files
echo "Executing SQL files..."
mysql -u $MYSQL_USER -p$MYSQL_PASS -h $MYSQL_HOST -P $MYSQL_PORT $MYSQL_DB < /var/www/docker_scripts/1_admin_menu_master.sql
mysql -u $MYSQL_USER -p$MYSQL_PASS -h $MYSQL_HOST -P $MYSQL_PORT $MYSQL_DB < /var/www/docker_scripts/2_countries_master.sql

# Rebuild Elasticsearch search index
echo "Rebuilding Elasticsearch search index..."
python3 manage.py search_index --rebuild &

# Start the Django app
echo "Starting Django server..."
exec python3 manage.py runserver 0.0.0.0:8080
