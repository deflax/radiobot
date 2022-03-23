FROM python:3-bullseye

RUN apt update
RUN apt install ffmpeg build-essential

RUN pip --no-cache-dir install \
    discord.py \
    pynacl

WORKDIR /app

ENV CONFIG_FILE="./config/config.ini"

COPY . /app