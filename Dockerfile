# Use an official Python runtime as a parent image
FROM python:3.9

# Update and upgrade the package manager
RUN apt-get update && apt-get upgrade -y

# Upgrade pip
RUN pip install --upgrade pip

# Start the MySQL service
#CMD ["mysqld"]

# Set the working directory to /var/www
WORKDIR /var/www

# Copy the requirements file into the container at /var/www
#COPY requirements.txt /var/www

# Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /var/www
COPY . /var/www

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Add the entrypoint script and set the execute permissions
COPY migrations_runserver.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/migrations_runserver.sh

# Set the entrypoint script
ENTRYPOINT ["migrations_runserver.sh"]

# Run the command to start the Django app
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
