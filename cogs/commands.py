from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Simple command example
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")

    @commands.command()
    async def say(self, ctx, message: str):
        print(message)
        await ctx.send(message)


# Setups cog
def setup(bot):
    bot.add_cog(Commands(bot))
