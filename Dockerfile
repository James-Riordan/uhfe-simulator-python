FROM python:3.10.3-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV MPLBACKEND=TkAgg
ENV DOCKER=true

RUN apt-get update && apt-get install -y \
    python3-tk \
    libgl1-mesa-glx \
    libglib2.0-0 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only Pipfile first to leverage Docker cache
COPY Pipfile ./

# Install pipenv
RUN pip install pipenv

# Generate Pipfile.lock *inside* the container
RUN pipenv lock

# Install dependencies from the lock file
RUN pipenv install --system --deploy

# Copy the rest of the code
COPY . .

CMD ["python", "main.py"]
