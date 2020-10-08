FROM python:3.7-slim

LABEL maintainer="jie8357ioii@gmail.com"

ENV DOCKER=true

RUN pip install --no-cache-dir --upgrade pip

WORKDIR /app/
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

EXPOSE 8000