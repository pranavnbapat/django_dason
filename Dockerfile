# Use an official Python runtime as a parent image
FROM python:3.9

# Update and upgrade the package manager
RUN apt-get update && apt-get upgrade -y

# Upgrade pip
RUN pip install --upgrade pip

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# Install Yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y yarn

# Install Gulp
RUN npm install -g gulp-cli

# Start the MySQL service
CMD ["mysqld"]

# Set the working directory to /var/www
WORKDIR /var/www

# Copy the requirements file into the container at /var/www
COPY requirements.txt /var/www

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at /var/www
COPY . /var/www

# Expose port 8000 for the Django app
#EXPOSE 8080

# Run the command to start the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
