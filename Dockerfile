FROM python:3

RUN pip --no-cache-dir install \
    discord.py
    pynacl

WORKDIR /app

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
    && npm install \
    && apk del .build-deps

ENV CONFIG_FILE="./config/config.ini"

COPY . /app

CMD ["node", "index.js"]
