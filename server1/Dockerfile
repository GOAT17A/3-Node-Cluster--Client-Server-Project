# Use a base image with Python or any other preferred language
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY server1.py .

# Install dependencies
RUN pip install flask

# Command to run the server
CMD ["python", "server1.py"]

