from random import randint
from jimmytoken import giveToken
import discord
##function imports
import gm
import uwufunc
import aitext

# assignment for ease of writing
client = discord.Client()

# print when the bot has sucessfully logged in. 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# do we need this? idk (print on message delete)
@client.event
async def on_message_delete(message):
    await message.channel.send("which one of you goobers deleted a message in my house")

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
    # ai text generator function
    elif randint(1, 100) == 69 or message.content.startswith('%rand'):
        await message.channel.send(aitext.aitext(message.content))


client.run(giveToken())
