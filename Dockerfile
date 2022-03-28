FROM python:3-bullseye

RUN apt-get update
RUN apt-get -yq install ffmpeg build-essential

RUN pip --no-cache-dir install \
    discord.py[voice] \
    pynacl \
    httplib2 \
    urllib3

WORKDIR /app

COPY . /app
