# Use an official Python runtime as a parent image
FROM python:3.9

# Update and upgrade the package manager
RUN apt-get update && \
    apt-get install -y \
    sudo \
    vim \
    nano \
    curl \
    wget \
    unzip \
    git \
    iputils-ping \
    net-tools \
    dnsutils \
    build-essential \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory to /var/www
WORKDIR /var/www

# Copy the current directory contents into the container at /var/www
COPY . /var/www

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Add the entrypoint script and set the execute permissions
COPY migrations_runserver.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/migrations_runserver.sh

# Set the entrypoint script
ENTRYPOINT ["migrations_runserver.sh"]

