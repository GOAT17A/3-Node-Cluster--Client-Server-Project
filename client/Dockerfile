# Use a base image with Python
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the application code and dependencies
COPY client.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application
CMD ["python", "client.py"]