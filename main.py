from http import client
import threading
import asyncio
import discord
import os
from discord.ext import commands

GUILD_ID = Guild Id
CHANNEL_ID = Channel ID

def toz(token):
    asyncio.set_event_loop(asyncio.new_event_loop())
    client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)
    @client.event
    async def on_ready():
        #print(f'Logged in as {client.user} ({client.user.id})')
        vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id=CHANNEL_ID)
        await vc.guild.change_voice_state(channel=vc,
                                        self_mute=True, #True or False
                                        self_deaf=True) #True or False
    
        print(f"Logged in as {client.user} ({client.user.id}). Successfully joined {vc.name} ({vc.id}")
    client.run(token)

with open("token.txt", "r") as f:
    accounts = list()
    for line in f:
        if "#" in line:
            continue
        data = line.split()
        accounts.append(data[0])

tokens = (accounts)

clients = []

for i, token in enumerate(tokens):
    # print(f'I: {i}, K: {token}')
    clients.append(threading.Thread(target=toz, args=(token,)))
    clients[i].start()


while True:
    if input() == 'exit':
        os.kill(os.getpid(), 9)