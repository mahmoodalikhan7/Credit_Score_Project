# Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Copy the application code
COPY app.py /app/

# Copy the model file to the container
COPY credit_score_model.pkl /app/

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use the $PORT environment variable for binding the server
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]
