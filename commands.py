class CommandsBot:
    from discord.ext import commands

    bot = commands.Bot(command_prefix="-")

    @bot.command()
    async def test(ctx):
        await ctx.send("no")
