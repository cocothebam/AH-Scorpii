import os

import discord
from dotenv import load_dotenv
from commands import CommandsBot
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

bot = commands.Bot(command_prefix="-")


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")
    CommandsBot()


bot.run(TOKEN)
