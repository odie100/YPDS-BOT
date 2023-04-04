# YPDS-BOT
Discord BOT for YOUNG PROFESSIONAL IN DATA SCIENCE

## EXPLANATION
### VIRTUAL ENVIRONMENT
> python -m venv discord_env

### ACTIVATE V.E
> source ./discord_env/bin/activate (LINUX) </br>
> .\discord_env\Scripts\activate (WINDOWS)

### INSTALL REQUIREMENTS
> pip install discord.py

### USE SSH URI FOR CLONING REPOSITORY (NOT HTTPS)
> git clone git@github.com:Loyolan/YPDS-BOT.git

### RUN THE BOT
> cd YPDS-BOT </br>
> python main.py</br>

### CONFIG
(MAKE YOU THAT YOU HAVE THE FILE 'privateapikeys.py' BEFORE RUNNING THE BOT) </br>
This file contains the private TOKEN of your BOT, it cannot be shared in public

### DOCUMENTATIONS
https://discordpy.readthedocs.io/en/stable/api.html </br>
READ COMMENTS IF YOU WANT TO KNOW HOW IT WORK

### CODE STRUCTURE
<b>main.py</b></br>
-the principal code </br>
-all events </br>
-run bot
</br> </br>
<b>responses.commands.py</b></br>
-response generator for specific message or embed (start with '!')</br>
</br></br>
<b>responses.embed.py</b></br>
-contains a generator embed method </br>
if you want to know more about Embed Class: </br>
https://discordpy.readthedocs.io/en/stable/api.html#embed </br>

### DISCORD API DOCS (LINKS)
<b>CLIENT</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#client</br>
<b>CHANNELS EVENTS</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#channels</br>
<b>CONNECTIONS EVENTS</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#connection</br>
<b>GUILDS EVENTS</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#guilds</br>
<b>MEMBERS EVENTS</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#members</br>
<b>MESSAGES EVENTS </b></br>
https://discordpy.readthedocs.io/en/stable/api.html#messages</br>
<b>REACTIONS EVENTS</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#reactions</br>
<b>ROLES EVENTS</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#roles</br></br>
<b>USER MODEL</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#id1 </br>
<b>MESSAGE MODEL</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#message
<b>REACTION MODEL</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#reaction</br>
<b>GUILD MODEL</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#guild</br>
<b>MEMBER MODEL</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#member</br>
<b>EMOJI MODEL</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#emoji</br>
<b>ROLE MODEL</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#role</br></br>
<b>EMBED CLASS</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#embed</br>
<b>FILE CLASS</b></br>
https://discordpy.readthedocs.io/en/stable/api.html#file</br>