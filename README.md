# Radiobot

## Features

* Live radio re-streaming to voice channels (using multiple bot users), automatically turned on/off when someone joins/leaves the bound channel.
* Other cool things.

## Running using Docker from the repo

2. Install dependancies `sudo apt install docker-compose`
3. Create a folder called `config` or similiar to keep your configuration in
4. Make a copy of `config.example.ini` called `config.ini` and place it in your `config` folder
5. Edit the config file
6. Build and execute using docker-compose: `docker-compose up -d --build --remove-orphans`
7. Monitor execution with `docker-compose logs --follow --tail 100`
