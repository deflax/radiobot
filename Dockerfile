FROM python:3-bullseye

RUN apt-get update
RUN apt-get -yq install ffmpeg build-essential

RUN pip --no-cache-dir install \
    discord.py \
    pynacl

WORKDIR /app

ENV CONFIG_FILE="./config/config.ini"

COPY . /app