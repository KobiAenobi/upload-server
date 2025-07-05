FROM python:3.10-slim

# working directory
WORKDIR /app

# Copy app code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Exposing the port Railway will use
EXPOSE 8000

# Running Flask app using the correct PORT
CMD ["python", "app.py"]
