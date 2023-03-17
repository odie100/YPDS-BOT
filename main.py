import discord
from discord.ext import commands
from apikeys import *
import sys

# CLIENT
client = commands.Bot(command_prefix = '?>', intents=discord.Intents.all())

#================================== EVENTS ==========================================#
### On ready
@client.event
async def on_ready():
    print('The bot is ready for use!')
    print('-------------------------')

@client.event
async def on_connect():
    channel = client.get_channel(CH_ASK_BOT)
    await channel.send("BOT connected!")

### On disconnect
@client.event
async def on_disconnect():
    print('Disconnected successfully')
    channel = client.get_channel(CH_ASK_BOT)
    await channel.send("BOT disconnected")

### On member join join server
@client.event
async def on_member_join(member):
    print("New member: " + member)
    channel = client.get_channel(CH_PRESENT_YOURSELF)
    await channel.send("Hello "+ member.mention +"! Welcome to the server, Thanks for join us!")
    await channel.send("We want to know you, (your name, your level in python, your level in data science, your target...)")

### On member leave server
@client.event
async def on_member_remove(member):
    channel = client.get_channel(CH_PRESENT_YOURSELF)
    print("A member leave: " + member)
    await channel.send(member.mention +" leave the server!")

### On a message recived
@client.event
async def on_message(message):
    channel = client.get_channel(CH_ASK_BOT)
    channel_message = message.channel
    auth = message.author
    if (channel == channel_message and not auth.bot) or client.user.mentioned_in(message):
        await message.reply("Sorry "+ auth.mention +"! For the moment, I can't generate answers for you!")

### On update member
@client.event
async def on_member_update(before, after):
    if before.top_role != after.top_role:
        channel = client.get_channel(CH_LEVEL)
        await channel.send("Congratulation "+ after.mention +"! You just passed the test!")
        embed = discord.Embed(title="CONGRATULATION", description="Level up!", color=0x4dff4d)
        embed.set_author(name=after.display_name)
        embed.set_thumbnail(url="https://images.emojiterra.com/google/noto-emoji/v2.034/512px/1f3c6.png")
        embed.add_field(name="Previous Level", value=before.top_role.mention, inline=True)
        embed.add_field(name="New Level", value=after.top_role.mention, inline=True)
        embed.add_field(name="Target Level", value=after.guild.roles[len(after.roles)+1].mention, inline=False)
        message = f"Good for you {after.display_name}! Your are now classified as a {after.top_role.name}!"
        embed.set_footer(text=message)
        await channel.send(embed=embed)
        await channel.send("If you agree that we share your progress on YPDS facebook official page, Please mention your name on Facebook!")

#================================= COMMANDS ======================================#
@client.command()
async def welcome(ctx):
    await ctx.send('Thanks! I am YPDS-BOT and I am here to help you')

@client.command()
async def goodbye(ctx):
    await ctx.send('Goodbey! Hope you have a good rest of the day')

#================================= RUN SERVER =====================================#
client.run(BOTTOKEN)
