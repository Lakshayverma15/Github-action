# Use a lightweight official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY leap_year.py .

# Configure the container to run your script by default
ENTRYPOINT ["python", "leap_year.py"]
