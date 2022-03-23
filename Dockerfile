FROM python:3-alpine

RUN apk add --no-cache ffmpeg \
    && apk add --no-cache --virtual .build-deps \
        g++ \
        gcc \
        libgcc \
        make \
        autoconf \
        libtool \
        automake \
        python3 \
    && apk del .build-deps

RUN pip --no-cache-dir install \
    discord.py \
    pynacl

WORKDIR /app

ENV CONFIG_FILE="./config/config.ini"

COPY . /app