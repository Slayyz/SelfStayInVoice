import threading
import asyncio
import discord
import random
import os
from discord.ext import commands

import config

def toz(token):
    asyncio.set_event_loop(asyncio.new_event_loop())
    client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)
    @client.event
    async def on_ready():
        
        vc = discord.utils.get(client.get_guild(token.guild_id).channels, id=token.channel_id)
        await vc.guild.change_voice_state(channel=vc,
                                        self_mute=token.self_mute,
                                        self_deaf=token.self_deaf)                          

        games = random.choice(["Minecraft", "Fortnite", "osu!", "League of Legends",])

        if token.status == "Random":
            status = random.choice(["online", "dnd", "idle"])
        if token.status == "Online":
            status = "online"
        if token.status == "Dnd":
            status = "dnd"
        if token.status == "Idle":
            status = "idle"

        if token.game == "None":
            await client.change_presence(status=discord.Status(status))
        elif token.game == "Random":
            if random.randint(1,2) == 1:
                await client.change_presence(status=discord.Status(status), activity=discord.Game(name=games))
        else:
            await client.change_presence(status=discord.Status(status), activity=discord.Game(name=token.game))

        print(f"As {client.user} ({client.user.id}). Joined {vc.name} ({vc.id}). Set {status}. Played {token.game}")
    client.run(token.token)

tokens = config.get_tokens()

clients = []

for i, token in enumerate(tokens):
    clients.append(threading.Thread(target=toz, args=(token,)))
    clients[i].start()

while True:
    if input() == 'exit':
        os.kill(os.getpid(), 9)