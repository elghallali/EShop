# Use the official Python image as the base image
FROM python:3.11-alpine

# Add Mysql
RUN apk update && \
    apk add --no-cache mariadb-connector-c-dev build-base && \
    apk add --no-cache mysql-client && \
    ln -s /usr/bin/mysql_config /usr/local/bin/mysql_config


# Set the working directory inside the container
WORKDIR /app

# Copy the required files to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the project files to the working directory (Copy application code)
COPY . .


# Set environment variables (Define build arguments)
ENV DB_NAME=eshop \
    DB_USER=root \
    DB_HOST=localhost \
    DB_PORT=3306


ENTRYPOINT ["/bin/bash","entrypoint.sh"]