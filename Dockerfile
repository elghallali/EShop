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
ENV DB_HOST=localhost
ENV DB_PORT=3306
ENV DB_NAME=data
ENV DB_USER=root
ENV DB_PASSWORD=


# Set up database and run migrations
RUN python manage.py makemigrations && \
    python manage.py migrate

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the default Django server port
EXPOSE 8000

# Run the command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]