# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY req.txt /app/
RUN pip install -r req.txt
COPY . .