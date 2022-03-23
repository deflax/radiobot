# Radiobot

Radio Bot based on codecat/reddit-radio


## Features

* Live radio re-streaming to voice channels (using multiple bot users), automatically turned on/off when someone joins/leaves the bound channel.
* Other cool things.


## Modules
A module is a class in the `modules` folder. It accepts the following methods:

* `constructor(config, client, bot)` where `config` is the object directly from the config file, `client` is the Discord client, and `bot` is the `RedditRadio` object.
* `onCmdXxxx(msg, ...)` where `Xxxx` is a command name like `.xxxx`.
* `onTick()` is called every second.
* `onMessage(msg)` is called whenever a message is sent in any channel. Return `false` if the message can pass through to other commands and handlers, or `true` to stop that from happening.


## Running using Docker from the repo
1. Clone this repo
    `git clone https://github.com/codecat/reddit-radio.git`
2. Install dependancies `sudo apt install docker-compose`
3. Create a folder called `config` or similiar to keep your configuration in
4. Make a copy of `config.example.toml` called `config.toml` and place it in your `config` folder
5. Edit the config file
6. Build and execute using docker-compose: `docker-compose up -d --build --remove-orphans`
7. Monitor execution with `docker-compose logs --follow --tail 100`

