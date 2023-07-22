# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Run database migrations
RUN python manage.py migrate

RUN chmod +x docker-entrypoint.sh

# Expose any necessary ports
EXPOSE 8000

# Define the command to run the application
CMD ["./docker-entrypoint.sh"]