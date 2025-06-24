FROM python:3.10.8-slim-buster
LABEL maintainer = '** Equipe de Desenvolvimento Mindbe <equipe at mindbe.com.br> **'

ARG CS_TAG
ENV CS_TAG=${CS_TAG}
ARG CS_GIT_ACCESS_TOKEN
ARG CS_SERVICE_NAME
ENV CS_SERVICE_NAME=${CS_SERVICE_NAME}

RUN apt-get update && apt-get install git python3-dev gcc make vim -y && git config --global url."https://${CS_GIT_ACCESS_TOKEN}@github.com".insteadOf "ssh://git@github.com"
RUN mkdir -p /app/${CS_SERVICE_NAME}

WORKDIR /app
COPY requirements.txt /app
COPY ${CS_SERVICE_NAME} /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app