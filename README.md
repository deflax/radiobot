# Radiobot

## Features

* Live radio re-streaming to voice channels.
* Automatically turned on/off when someone joins/leaves the bound channel.
* Shows ICY StreamTITLE
* Other cool things.

## Running using Docker from the repo

1. `sudo apt install docker-compose`
2. `cp radiobot.env.dist radiobot.env ; cp relay.env.dist relay.env`
3. `vim .env`
4. `docker-compose up -d --build --remove-orphans`
5. `docker-compose logs --follow --tail 100 --timestamps`
