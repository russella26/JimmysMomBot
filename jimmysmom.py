from random import randint
from jimmytoken import giveToken
import discord
##function imports
import gm
import uwufunc
import generate

# assignment for ease of writing
client = discord.Client()

# print when the bot has sucessfully logged in. 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# do we need this? idk (print on message delete)
#@client.event
#async def on_message_delete(message):
#    await message.channel.send("which one of you goobers deleted a message in my house")
# wow this was really dumb


# message based bot commands

global replymode
global replychannel
replymode = False
replychannel = 0

@client.event
async def on_message(message):
    global replymode
    global replychannel
    if message.author == client.user:
        return
    elif message.content.startswith('%replymode'):
        replymode = not replymode
        replystring = "Reply mode is currently set to: " + str(replymode)
        await message.channel.send(replystring)
    elif message.content.startswith('%replychannel'):
        replychannel = message.channel
        replystring = "This is now the only channel I will reply in :)"
        await message.channel.send(replystring)
    # good morning function
    elif message.content.startswith('%gm'): 
        await message.channel.send(gm.gm(message.author.nick))
    # uwu function
    elif message.content.startswith('%uwu'):
        await message.channel.send((uwufunc.uwufunc(message.content)))
    # random ai text generator function
    elif message.content.startswith('%rand'):
        async with message.channel.typing():
            aigen = generate.aitext(message.content)
        await message.channel.send(aigen)
    # with context ai text generator function
    elif (replymode and (message.channel == replychannel)) or message.content.startswith('%con'):
        maxlen = 2600
        contstring = ""
        for cached in client.cached_messages:
            if cached.channel == replychannel:
                contstring += cached.content + '\n'
        if len(contstring) > maxlen:
            curdiff = len(contstring) - maxlen
            contstring = contstring[curdiff:]
        print(len(contstring)) 
        async with message.channel.typing():
            aigen = generate.contextgen((contstring))
        await message.reply(aigen)



client.run(giveToken())
