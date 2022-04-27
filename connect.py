import os
import sys

import discord
from dotenv import load_dotenv
from discord.ext import commands
from command import openImage as b


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

bot = commands.Bot(command_prefix="-")

devs = [
    "dc34c9975dfef9ee6dc06f21cdb420f9",
]


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

    @bot.command()
    async def test(ctx):
        print(ctx.author.avatar)
        for dev in devs:
            if ctx.author.avatar == devs[dev]:
                await ctx.send("you are sheen")
            else:
                await ctx.send("you are not sheen")

    @bot.command()
    async def shutDown(ctx):
        await ctx.send("shutting down")
        sys.exit("shutdown via discord")

    @bot.command()
    async def openImage(ctx):
        b.findImage


bot.run(TOKEN)
