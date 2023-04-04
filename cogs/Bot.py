import discord
from discord.ext import commands
from apikeys import CH_ASK_BOT

from responses.commands import generate_reply

class Bot(commands.Cog):
    def __init__(self, client):
        self.client = client
    ### On ready
    @commands.Cog.listener()
    async def on_ready():
        print('The bot is ready for use!')
        print('-------------------------')
        channel = client.get_channel(CH_ASK_BOT)
        await channel.send("BOT connected!")

    ### On disconnect
    @commands.Cog.listener()
    async def on_disconnect():
        print('Disconnected')
        channel = client.get_channel(CH_ASK_BOT)
        await channel.send("BOT disconnected")

async def setup(client):
    await client.add_cog(Bot(client))