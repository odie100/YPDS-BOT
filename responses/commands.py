from responses.embed import generate_embed

HELP = [{
    "title" : "!help",
    "content" :"Show this message"
    },{
    "title": "!level",
    "content": "Show your current level"
    },{
    "title": "!whoami",
    "content": "Show your name and nickname"
    },{
    "title": "!about",
    "content": "About your Community"
    },{
    "title": "!progress",
    "content": "Show your progress"
    },{
    "title": "Ask BOT",
    "content": "Special Channel for talking with the BOT"
    },{
    "title": "Mention BOT",
    "content": "BOT can reply to your questions! Just mention it"
    }
]

#========================================== FUNCTIONS ===============================================#

def generate_help():
    title = "HELP"
    desc = "BOT usage"
    color = 0x4d4dff
    auth = "YPDS-BOT"
    thumb = "https://cdn-icons-png.flaticon.com/512/682/682055.png"
    footer = "Hope that can help you!"
    embed = generate_embed(title, desc, color, auth, thumb, HELP, footer)
    return embed

def level(auth):
    title = "YOUR LEVEL"
    desc = auth.mention
    color = 0x4dff4d
    author = "YPDS-BOT"
    thumb = "https://png.pngtree.com/png-vector/20210207/ourmid/pngtree-simple-modern-level-up-game-interface-with-stars-and-arrow-png-image_2896899.jpg"
    fields = [
       {
          "title": "Current Level",
          "content": f"Your are now classified as {auth.top_role.name}"
       }
    ]
    footer = "If you want to upgrade your level, Test your capacity"
    embed = generate_embed(title, desc, color, author, thumb, fields, footer)
    return embed

def whoami(auth):
    title = "WHO ARE YOU"
    desc = "Informations"
    color = 0xff44ff
    author = auth.display_name
    thumb = "https://w7.pngwing.com/pngs/81/570/png-transparent-profile-logo-computer-icons-user-user-blue-heroes-logo-thumbnail.png"
    fields = [
        {
            "title": "Display name",
            "content": auth.display_name
        },{
            "title": "Nick name",
            "content": auth.nick
        },{
            "title": "Name",
            "content": auth.name
        }
    ]
    footer = "You can change your nickname in the server!"
    embed = generate_embed(title, desc, color, author, thumb, fields, footer)
    return embed

def about(auth):
    title = "ABOUT YOUR COMMUNITY YPDS"
    guild = auth.guild
    desc = guild.name
    color = 0xff0000
    author = "YPDS-BOT"
    thumb = "https://cxp.asia/2020/wp-content/uploads/2021/06/40-1-1024x597-1.jpg"
    fields = []
    categories = guild.categories
    for cat in categories:
        t = cat.name
        channels = ""
        for ch in cat.channels:
            channels += "||" +ch.name
        fields.append({'title': t, 'content': channels})
    fields.append({'title': 'MEMBERS', 'content': len(guild.members)})
    fields.append({'title': 'CREATED AT', 'content': guild.created_at})
    footer = 'If you need more informations about the server, ask YPDS'
    embed = generate_embed(title, desc, color, author, thumb, fields, footer)
    return embed

def progress(auth):
    title = "YOUR PROGRESS"
    desc = 'All your Grades'
    color = 0x00ff00
    author = auth.display_name
    thumb = "https://thumbs.dreamstime.com/b/progress-17252916.jpg"
    fields = []
    for role in auth.roles:
        t = "Level "+ str(role.position)
        content = "As "+ role.name
        fields.append({'title': t, 'content': content})
    footer = 'Never give up! We are here to help you'
    embed = generate_embed(title, desc, color, author, thumb, fields, footer)
    return embed

def not_found():
    title = "NOT FOUND"
    desc = "Command introuvable"
    color = 0xff0000
    author = 'YPDS-BOT'
    thumb = "https://cdn5.vectorstock.com/i/1000x1000/73/49/404-error-page-not-found-miss-paper-with-white-vector-20577349.jpg"
    fields = [{'title': 'Error', 'content': 'Check your spell'}]
    footer = 'Type !help for BOT usage'
    embed = generate_embed(title, desc, color, author, thumb, fields, footer)
    return embed

#============================================#=======================================================#
def generate_reply(auth, message):
    try:
        cmd = message[1:message.index(' ')].casefold().strip()
    except:
        cmd = message[1:].casefold().strip()
    return commands_response(auth, cmd)

def commands_response(auth, cmd):
    if cmd == 'help':
        return generate_help()
    elif cmd == 'level':
        return level(auth)
    elif cmd == 'whoami':
        return whoami(auth)
    elif cmd == 'about':
        return about(auth)
    elif cmd == 'progress':
        return progress(auth)
    else:
        return not_found()
