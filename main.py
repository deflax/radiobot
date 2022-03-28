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
    print('Logged in as ' + bot.user.name + ' #' + str(bot.user.id))

    # get channels
    #voice_channel = bot.get_channel(voice_channel_id)
    #text_channel = bot.get_channel(text_channel_id)
    #if not voice_channel:
    #    print("No voice channel " + voice_channel_id + " found!")
    #if not text_channel:
    #    print("No text channel " + text_channel_id + " found!")

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
    #print('before: ' + str(before))
    #print('after: ' + str(after))
    #return
    
    if member.bot:
        print("self event detection")
        return
    
    debug_channel = bot.get_channel(text_channel_id)
    voice_channel = bot.get_channel(voice_channel_id)
    member_ids = voice_channel.voice_states.keys()
    
    await debug_channel.send('voice activity')
    return    

    if str(after.channel.id) == voice_channel_id:
            print("Connecting to voice channel " + voice_channel_id)
            voiceChannel = await voice_channel.connect()
   
        print("Disconnecting from voice channel " + voice_channel_id)
        voiceChannel = await after.channel.connect()
        await voiceChannel.disconnect()

# Start the bot with multiprocess compatiblity
if __name__ == "__main__":
    try:
        bot.loop.run_until_complete(bot.start(login_token))
    finally:
        bot.loop.close()
