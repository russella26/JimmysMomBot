from random import randint
from uwu import generateUwU
from jimmytoken import giveToken

import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('%continue'):
        await message.channel.send('fuck you ' + str(message.author)[:-5])
    elif message.content.startswith('%uwu'):
        await message.channel.send(generateUwU(message.content[5:]))
    elif randint(1, 100) == 69:
        await message.channel.send('eyy wheres the gabbagool')


client.run(giveToken())
