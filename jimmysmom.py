from random import randint
from jimmytoken import giveToken
import discord
##function imports
import gm
import uwufunc
import generate
import contextaware

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
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # good morning function
    if message.content.startswith('%gm'):
        await message.channel.send(gm.gm(message.author.nick))
    # uwu function
    elif message.content.startswith('%uwu'):
        await message.channel.send((uwufunc.uwufunc(message.content)))
    # random ai text generator function
    elif randint(1, 100) == 69 or message.content.startswith('%rand'):
        async with message.channel.typing():
            aigen = generate.aitext(message.content)
        await message.channel.send(aigen)
    # with context ai text generator function
    elif message.content.startswith('%con'):
        async with message.channel.typing():
            aigen = contextaware.contextaware(message.content)
        await message.channel.send(aigen)


client.run(giveToken())
