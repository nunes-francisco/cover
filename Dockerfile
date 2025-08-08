FROM python:3.10.8-slim-buster
LABEL maintainer = '** Equipe de Desenvolvimento Mindbe <equipe at mindbe.com.br> **'

ARG TAG
ENV TAG=${TAG}
ARG GIT_ACCESS_TOKEN
ARG SERVICE_NAME
ENV SERVICE_NAME=${SERVICE_NAME}

RUN apt-get update && apt-get install git python3-dev gcc make vim -y && git config --global url."https://${GIT_ACCESS_TOKEN}@github.com".insteadOf "ssh://git@github.com"
RUN mkdir -p /app/${SERVICE_NAME}

WORKDIR /app
COPY requirements.txt /app
COPY ${SERVICE_NAME} /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app