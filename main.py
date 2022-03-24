import os
import discord
from discord.ext import commands
import asyncio
from subprocess import Popen

bot_version = os.environ['version']
print('radiobot ' + bot_version + ' starting')

login_token = os.environ['token']
voice_channel_id = os.environ['channel_voice']
text_channel_id = config['channel_test']

# Configure the bot
description = '''Radiobot.'''
bot = commands.Bot(command_prefix='!', description=description)

# Initialize opus
if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

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
    if not v_channel:
        print("No voice channel with that ID found!")
    if not text_channel:
        print("No text channel with that ID found!")
    #voice_client = await bot.join_voice_channel(v_channel)

@bot.event
async def on_message(ctx):
    # don't respond to ourselves
    if ctx.message.author == ctx.user:
        return

    print ('<' + ctx.message.author.nick + '> ' + ctx.message.content)

    if ctx.message.content == '!version':
        await ctx.message.channel.send('] radiobot ' + bot_version + ' - python: ' + os.environ['PYTHON_VERSION'])

@bot.event
async def on_voice_state_update(member, before, after):
    clients_before = len(ctx.before.channel.members)

    # If nobody in the channel based on before, invoke join the channel
    if clients_before == 0:
        voiceChannel = await after.channel.connect()

    # if after join channel members > 0, join the channel
    if clients_before == 1:
        print("gg")
        await voiceChannel.disconnect()

bot.run(bot_token) # Get token for this shit

