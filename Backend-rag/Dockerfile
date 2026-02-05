# Use python-slim to start with a tiny base (~120MB instead of ~900MB)
FROM python:3.13-slim

WORKDIR /app

# Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install only essential build tools, then clean up the apt cache immediately
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Update pip to the latest version
RUN pip install --no-cache-dir --upgrade pip

# --- THE CRITICAL FIX ---
# Install the CPU-only version of Torch. 
# This version is ~200MB, whereas the default (with GPU drivers) is ~2.5GB.
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Install your other dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app code
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8000

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]