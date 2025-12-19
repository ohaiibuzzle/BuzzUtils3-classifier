# Use official Python image as base
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
	&& rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY src/ ./src/
COPY models/ ./models/

# Set environment variables (optional)
ENV PYTHONUNBUFFERED=1

# Set entrypoint (adjust if needed)
CMD ["python", "-m", "fastapi", "run", "src/main.py"]
