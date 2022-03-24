import os
import discord
from discord.ext.commands import Bot

bot_version = os.environ['version']
print('radiobot ' + bot_version + ' starting')

bot_token = os.environ['token']

client = Bot(command_prefix="!")

isPlaying = False
class Radio(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        print ('<' + message.author.nick + '> ' + message.content)

        if message.content == '!version':
            await message.channel.send('] radiobot ' + bot_version)

    @client.event
    async def on_voice_state_update(self, member, before, after):
        clients_before = len(before.channel.members)

        # If nobody in the channel based on before, invoke join the channel
        if clients_before == 0:
            self.voiceChannel = await after.channel.connect()

        # if after join channel members > 0, join the channel
        if clients_before == 1:
            print("gg")
            await self.voiceChannel.disconnect()

client = Radio()
client.run(bot_token) # Get tokeun for this shit
