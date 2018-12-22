import asyncio

from discord.ext import commands

import config
import logging
import asyncpg
from db import create_tables

logger = logging.getLogger('discord')

# sets up discord.py logging in chat
logging.basicConfig(level=logging.INFO)

# sets up logging to file
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class Bot(commands.Bot):
    def __init__(self, db):
        """

        :type pool: asyncpg.pool
        """
        super().__init__(command_prefix=self.get_prefix, description="Simple example discord.py command bot")
        self.db = db

    async def get_prefix(self, message):
        return "!"

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        try:
            await self.db.execute('''INSERT INTO members(discord_id, name, dob) VALUES($1, $2, $3)''',
                              str(message.author.id), message.author.name, message.created_at)
        except asyncpg.exceptions.UniqueViolationError:
            _ = 1

        await self.db.execute('''INSERT INTO messages(discord_id, content, dob) VALUES ($1, $2, $3)''',
                              str(message.author.id), message.content, message.created_at)

        await self.process_commands(message)

    async def load_extensions(self, names):
        for name in names:
            self.load_extension(name)


async def run():
    # Creates postrgesql connection pool
    db = await asyncpg.create_pool(**config.postgresqlCredentials)

    await create_tables(db)

    bot = Bot(db)
    # write general bot commands here
    await bot.load_extensions(["cogs.commands"])

    try:
        await bot.start(config.token)
    except KeyboardInterrupt:
        await db.close()
        await bot.logout()


if __name__ == "__main__":
    # Starts async run function in event loop
    asyncio.get_event_loop().run_until_complete(run())
