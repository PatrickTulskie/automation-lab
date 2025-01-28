# Use an official lightweight Python image
FROM python:3.10-slim

# Set a working directory
WORKDIR /app

# Copy the application code into the container
COPY app.py /app/app.py

# Install dependencies
RUN pip install --no-cache-dir flask html2text

# Expose the application port
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]
