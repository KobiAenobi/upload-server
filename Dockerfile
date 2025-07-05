# Use a small Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy your app code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Railway will use
EXPOSE 8000

# Run your Flask app using the correct PORT
CMD ["python", "app.py"]
