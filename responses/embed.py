import discord

def generate_embed(title, desc, color, auth, thumb, fields, footer):
    embed = discord.Embed(title=title, description=desc, color=color)
    embed.set_thumbnail(url=thumb)
    embed.set_author(name=auth)
    for field in fields:
        embed.add_field(name=field['title'], value=field['content'])
    embed.set_footer(text=footer)
    return embed
