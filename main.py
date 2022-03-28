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
isConnected = False

@bot.event
async def on_ready():
    print('[INFO] Logged in as ' + bot.user.name + ' #' + str(bot.user.id))

    # get channels
    voice_channel = await bot.fetch_channel(voice_channel_id)
    debug_channel = await bot.fetch_channel(text_channel_id)
    if not voice_channel:
        print("[WARN] No voice channel " + voice_channel_id + " found!")
    if not debug_channel:
        print("[WARN] No text channel " + text_channel_id + " found!")

    await debug_channel.send('] ready.')

@bot.event
async def on_message(message):
    # don't respond to ourselves
    if message.author == bot.user:
        return

    if not str(message.channel.id) == text_channel_id:
        return

    print('<' + message.author.nick + '> ' + message.content)

    if message.content == '!version':
        await message.channel.send('] radiobot ' + bot_version + ' - python ' + os.environ['PYTHON_VERSION'] + ' - https://github.com/deflax/radiobot :purple_heart:')

@bot.event
async def on_voice_state_update(member, before, after):
    """
    Starts events when a user changes their voice state.
    Such as connecting, disconnecting and moving between channels.
    :type member: discord.Member
    :type before: discord.VoiceState
    :type after: discord.VoiceState
    :param member: The member that changed their voice state.
    :param before: The member as they were before the change.
    :param after: The member as they are after the change.
    :return:
    """
    global isConnected
    FFMPEG_OPTS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if member.bot:
        #print("[INFO] self event detection")
        return
    
    voice_channel = await bot.fetch_channel(voice_channel_id)
    debug_channel = await bot.fetch_channel(text_channel_id)

    member_ids = len(voice_channel.voice_states.keys())

    #await debug_channel.send('] voice #' + voice_channel_id + ' member count: ' + str(member_ids))

    if member_ids == 1 and isConnected == False:
        isConnected = True
        await debug_channel.send('] connecting to #' + voice_channel_id)
        voice_client = await voice_channel.connect()
        player = voice_client.play(discord.FFmpegPCMAudio(os.environ['url'], **FFMPEG_OPTS))
        return

    if member_ids == 1 and isConnected == True:
        isConnected = False
        await debug_channel.send('] disconnecting from #' + voice_channel_id)
        for voice_client in bot.voice_clients:
            await voice_client.disconnect()
        return

# Start the bot with multiprocess compatiblity
if __name__ == "__main__":
    try:
        bot.loop.run_until_complete(bot.start(login_token))
    finally:
        bot.loop.close()
