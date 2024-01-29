FROM python:3.10
LABEL authors="Isko"

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /CHATFORM

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y supervisor && \
    rm -rf /var/lib/apt/lists/*

COPY . /CHATFORM
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
