import discord
from discord.ext import commands
from apikeys import CH_ASK_BOT
from responses.commands import generate_reply

class Message(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    ### On a message recived
    @commands.Cog.listener()
    async def on_message(message):
        channel = client.get_channel(CH_ASK_BOT)
        channel_message = message.channel
        auth = message.author
        if (channel == channel_message and not auth.bot) or client.user.mentioned_in(message):
            com = message.content
            if com[0] == '!':
                text = generate_reply(auth, com)
            else:
                text = "Sorry "+ auth.mention +"! For the moment, I can't generate answers for you!"
            await message.reply(embed=text)

async def setup(client):
    await client.add_cog(Message(client))