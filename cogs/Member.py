import discord
from discord.ext import commands
from apikeys import CH_PRESENT_YOURSELF, CH_LEVEL

class Member(commands.Cog):
    def __init__(self, client):
        self.client = client

    ### On member join join server
    @commands.Cog.listener()
    async def on_member_join(member):
        print("New member: " + member)
        channel = client.get_channel(CH_PRESENT_YOURSELF)
        await channel.send("Hello "+ member.mention +"! Welcome to the server, Thanks for join us!")
        await channel.send("We want to know you, (your name, your level in python, your level in data science, your target...)")

    ### On member leave server
    @commands.Cog.listener()
    async def on_member_remove(member):
        channel = client.get_channel(CH_PRESENT_YOURSELF)
        print("A member leave: " + member)
        await channel.send(member.mention +" leave the server!")

    ### On update member info
    @commands.Cog.listener()
    async def on_member_update(before, after):
        if before.top_role != after.top_role:
            channel = client.get_channel(CH_LEVEL)
            embed = discord.Embed(title="CONGRATULATION", description="Level up!", color=0x4dff4d)
            embed.set_author(name=after.display_name)
            embed.set_thumbnail(url="https://images.emojiterra.com/google/noto-emoji/v2.034/512px/1f3c6.png")
            if (len(before.roles) == 1):
                await channel.send("Welcome "+ after.mention +"!")
                embed.add_field(name="Previous Level", value="Ivited", inline=True)
            else:
                await channel.send("Congratulation "+ after.mention +"! You just passed the test!")
                embed.add_field(name="Previous Level", value=before.top_role.mention, inline=True)
            embed.add_field(name="New Level", value=after.top_role.mention, inline=True)
            try:
                embed.add_field(name="Target Level", value=after.guild.roles[len(after.roles)+1].mention, inline=False)
            except:
                embed.add_field(name="Target Level", value="That all!", inline=False)
            message = f"Good for you {after.display_name}! Your are now classified as a {after.top_role.name}!"
            embed.set_footer(text=message)
            await channel.send(embed=embed)
            await channel.send("If you agree that we share your progress on YPDS facebook official page, Please mention your name on Facebook!")

async def setup(client):
    await client.add_cog(Member(client))