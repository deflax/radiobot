# Radiobot

## Features

* Live radio re-streaming to voice channels (using multiple bot users), automatically turned on/off when someone joins/leaves the bound channel.
* Other cool things.

## Running using Docker from the repo

1. `sudo apt install docker-compose`
2. `cp .env.dist .env`
3. `vim .env`
4. `docker-compose up -d --build --remove-orphans`
5. `docker-compose logs --follow --tail 100`
