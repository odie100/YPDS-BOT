import discord
from discord.ext import commands
from apikeys import *
from privateapikeys import *
import os
import asyncio

# CLIENT
client = commands.Bot(command_prefix = '?', intents=discord.Intents.all())

initial_extensions = []

# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         initial_extensions.append('cogs.'+ filename[:-3])


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load_extensions()
        await client.start(BOTTOKEN)

#================================= RUN SERVER =====================================#
# if __name__ == '__main__':
#     for extension in initial_extensions:
#         client.load_extension(extension)
asyncio.run(main())
