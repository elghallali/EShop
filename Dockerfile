# Use the official Python image as the base image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the required files to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the rest of the project files to the working directory (Copy application code)
COPY . .


# Set environment variables (Define build arguments)

# Set up database and run migrations
RUN python manage.py makemigrations && \
    python manage.py migrate

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the default Django server port
EXPOSE 8000

# Run the command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]