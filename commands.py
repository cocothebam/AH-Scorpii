from discord.ext import commands

class CommandsBot:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(ctx):
        await ctx.send("no")
