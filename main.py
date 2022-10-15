import threading
import asyncio
import discord
import os
from discord.ext import commands

import config

def toz(token):
    asyncio.set_event_loop(asyncio.new_event_loop())
    client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)
    @client.event
    async def on_ready():
        #print(f'Logged in as {client.user} ({client.user.id})')

        vc = discord.utils.get(client.get_guild(token.guild_id).channels, id=token.channel_id)
        await vc.guild.change_voice_state(channel=vc,
                                        self_mute=token.self_mute,
                                        self_deaf=token.self_deaf)
    
        print(f"Logged in as {client.user} ({client.user.id}). Successfully joined {vc.name} ({vc.id})")
    client.run(token.token)


tokens = config.get_tokens()

clients = []

for i, token in enumerate(tokens):
    # print(f'I: {i}, K: {token}')
    clients.append(threading.Thread(target=toz, args=(token,)))
    clients[i].start()

while True:
    if input() == 'exit':
        os.kill(os.getpid(), 9)