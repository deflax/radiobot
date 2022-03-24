import os
import discord
from discord.ext import commands
import asyncio
from subprocess import Popen

bot_version = os.environ['version']
print('radiobot ' + bot_version + ' starting')

login_token = os.environ['token']
voice_channel_id = os.environ['channel_voice']
text_channel_id = os.environ['channel_text']

# Configure the bot
description = '''Radiobot'''
bot = commands.Bot(command_prefix='!', description=description)

# Initialize opus
#if not discord.opus.is_loaded():
#    discord.opus.load_opus('opus')

# Initialize some global variables
voice_client = None
text_channel = None
isPlaying = False

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    # get channels
    voice_channel = bot.get_channel(voice_channel_id)
    text_channel = bot.get_channel(text_channel_id)
    if not voice_channel:
        print("No voice channel " + voice_channel_id + " found!")
    if not text_channel:
        print("No text channel " + text_channel_id + " found!")
    #voice_client = await bot.join_voice_channel(v_channel)

@bot.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == bot.user:
        return

    if not str(message.channel.id) == text_channel_id:
        return

    print('<' + message.author.nick + '> ' + message.content)

    if message.content == '!version':
        await message.channel.send('] radiobot ' + bot_version + ' - python ' + os.environ['PYTHON_VERSION'])

@bot.event
async def on_voice_state_update(member, before, after):
    print("User connected to " + str(after.channel.id))
    if after.channel.id == [voice_channel_id]:
        clients_before = len(before.channel.members)

        # If nobody in the channel based on before, invoke join the channel
        if clients_before == 0:
            print("Connecting to voice channel " + voice_channel_id)
            voiceChannel = await after.channel.connect()

        # if channel members > 0, leave the channel
        if clients_before == 1:
            print("Disconnecting from voice channel " + voice_channel_id)
            await voiceChannel.disconnect()

# Start the bot with multiprocess compatiblity
if __name__ == "__main__":
    try:
        bot.loop.run_until_complete(bot.start(login_token))
    finally:
        bot.loop.close()

