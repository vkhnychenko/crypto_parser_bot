FROM python:3.9-slim

RUN apt update
RUN apt install -y gcc

WORKDIR /app
COPY . /app
RUN python3 -m pip install --no-cache-dir -r requirements.txt
