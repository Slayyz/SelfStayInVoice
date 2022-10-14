from email.policy import default
import threading
import asyncio
import discord
import os
from discord.ext import commands

import config

defaults = config.get_default()
(GUILD_ID, CHANNEL_ID) = (defaults.guild_id, defaults.channel_id)

def toz(token):
    asyncio.set_event_loop(asyncio.new_event_loop())
    client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)
    @client.event
    async def on_ready():
        #print(f'Logged in as {client.user} ({client.user.id})')
        vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id=CHANNEL_ID)
        await vc.guild.change_voice_state(channel=vc,
                                        self_mute=defaults.self_mute,
                                        self_deaf=defaults.self_deaf)
    
        print(f"Logged in as {client.user} ({client.user.id}). Successfully joined {vc.name} ({vc.id}")
    client.run(token)

tok = config.get_tokens()
tokens = (tok.token)

clients = []

for i, token in enumerate(tokens):
    # print(f'I: {i}, K: {token}')
    clients.append(threading.Thread(target=toz, args=(token,)))
    clients[i].start()

while True:
    if input() == 'exit':
        os.kill(os.getpid(), 9)