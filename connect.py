import os

import discord
from dotenv import load_dotenv
from commands import CommandsBot

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()


@client.event
async def on_ready():
    CommandsBot()


client.run(TOKEN)
