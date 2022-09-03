# Build
FROM python:3.10-buster AS build-env

ENV PYTHONUNBUFFERED=1\
    PYTHONDONTWRITEBYTECODE=1\
    PYTHONFAULTHANDLER=1\
    POETRY_VERSION=1.1.14\
    POETRY_VIRTUALENVS_IN_PROJECT=1\
    POETRY_NO_INTERACTION=1

WORKDIR /app
COPY . .

RUN pip install poetry==${POETRY_VERSION}\
    && poetry install --no-dev --no-root\
    && poetry build -f wheel\
    && .venv/bin/pip install dist/*.whl

# Distroless container
FROM python:3.10-alpine

WORKDIR /app

RUN apk add libgcc

ENV PYTHONPATH=/app/site-packages
COPY --from=build-env /app/.venv/lib/python3.10/site-packages /app/site-packages

COPY scripts.py .

ENTRYPOINT ["python", "scripts.py", "start"]
