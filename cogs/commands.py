from discord.ext import commands
import main

class Commands:
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.db

    #Simple command example
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")

    @commands.command()
    async def getUsersMessages(self, ctx, userId):
        messages = await self.db.fetch('''SELECT * FROM messages WHERE (discord_id = $1 )''', str(userId))
        print(messages)
        for message in messages:
            print(message)
            await ctx.send(message["content"])



#Setups cog
def setup(bot):
    bot.add_cog(Commands(bot))