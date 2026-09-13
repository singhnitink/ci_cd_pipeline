# 1. Start with a lightweight, official Python Linux base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements first to leverage Docker layer caching
COPY requirements.txt .

# 4. Install dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy our application code into the container
COPY main.py .

# 6. Inform Docker that the app listens on port 8000
EXPOSE 8000

# 7. The command to run when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
