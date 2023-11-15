# Use the Python 3.8-slim-buster image as the base image
FROM python:3.8-slim-buster


ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app

# Install essential development tools (gcc solution)
# we use build essential bc it has the gcc package in it and other build tools needed
RUN apt-get update && apt-get install -y build-essential

# Copy the requirements.txt file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt




# Copy the rest of your application code to the container
COPY . .

# Specify the command to run your application
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
