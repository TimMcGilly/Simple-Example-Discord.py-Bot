import asyncio
import logging

from discord.ext import commands

import config

logger = logging.getLogger('discord')

# sets up discord.py logging in chat
logging.basicConfig(level=logging.INFO)

# sets up logging to file
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=self.get_prefix, description="Simple example discord.py command bot")

    async def get_prefix(self, message):
        return "!"

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        await self.process_commands(message)

    async def load_extensions(self, names):
        for name in names:
            self.load_extension(name)


async def run():
    bot = Bot()
    # write general bot commands here
    await bot.load_extensions(["cogs.commands"])

    try:
        await bot.start(config.token)
    except KeyboardInterrupt:
        await bot.logout()


if __name__ == "__main__":
    # Starts async run function in event loop
    asyncio.get_event_loop().run_until_complete(run())
