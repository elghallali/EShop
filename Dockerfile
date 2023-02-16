# Use the official Python image as the base image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the required files to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files to the working directory
COPY . .

# Expose the default Django server port
EXPOSE 8000

# Set the environment variables for Django

# Run the command to start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]