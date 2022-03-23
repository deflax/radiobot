FROM node:16-alpine

WORKDIR /app

COPY ./package.json /app/package.json

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

ENV CONFIG_FILE="./config/config.toml"

COPY . /app

CMD ["node", "index.js"]