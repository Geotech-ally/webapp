# Docker Flask Web App

A small Flask web application that runs in Docker. Its home page identifies
the container host and operating system.

## Requirements

- Python 3.9 or later
- Docker (for container deployment)

## Run locally

Create a virtual environment and install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open <http://localhost:5000>.

## Run with Docker

Build the image:

```bash
docker build -t docker-flask-app .
```

Start the container:

```bash
docker run --rm -p 5000:5000 docker-flask-app
```

Open <http://localhost:5000>.

## Endpoint

| Route | Method | Description |
| --- | --- | --- |
| `/` | `GET` | Returns the application greeting, container hostname, and system name. |
