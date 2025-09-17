FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# System deps (psycopg2 build, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Requirements first (for layer caching)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# App code
COPY . .

# Run as non-root
RUN useradd -m appuser
USER appuser

EXPOSE 8000
CMD ["bash", "-lc", "gunicorn -w ${BACKEND_WORKERS:-2} -b 0.0.0.0:8000 -k gthread --threads 4 --log-level ${BACKEND_LOG_LEVEL:-info} app:app"]
