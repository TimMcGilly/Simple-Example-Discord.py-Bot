from discord.ext import commands
import discord

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.db

    # Simple command example
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong")

    @commands.command()
    async def getUsersMessages(self, ctx, member: discord.Member):
        #Fetches all rows from message table which matches
        messages = await self.db.fetch('''SELECT * FROM messages WHERE (discord_id = $1 )''', str(member.id))
        print(messages)
        for message in messages:
            print(message)
            await ctx.send(message["content"])

    @commands.command()
    async def getAuthorFromMessage(self, ctx, message: str):

        #Example of querying multiple tables in the database
        authors = await self.db.fetch('''SELECT * FROM messages, members 
                                         WHERE (content = $1) AND (members.discord_id = messages.discord_id)
                                      ''',
                                      message)
        for author in authors:
            await ctx.send(author["name"] + " wrote this message")


# Setups cog
def setup(bot):
    bot.add_cog(Commands(bot))
