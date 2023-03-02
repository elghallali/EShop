# Use the official Python image as the base image
FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /eShop

# Copy the required files to the working directory
COPY requirements.txt requirements.txt

# Install the required packages
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
