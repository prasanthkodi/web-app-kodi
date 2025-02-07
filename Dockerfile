# Use the official lightweight Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Heroku provides
ENV PORT=5000
EXPOSE $PORT

# Start the application with Gunicorn
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT run:app
