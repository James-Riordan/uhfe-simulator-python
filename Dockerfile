FROM python:3.13.5-slim

# Set environment variables for GUI backend
ENV DEBIAN_FRONTEND=noninteractive
ENV MPLBACKEND=TkAgg

RUN apt-get update && apt-get install -y \
    python3-tk \
    libgl1-mesa-glx \
    libglib2.0-0 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy Pipenv files and install dependencies
COPY Pipfile Pipfile.lock* ./
RUN pip install pipenv && pipenv install --system --deploy

COPY . .

CMD ["python", "main.py"]
