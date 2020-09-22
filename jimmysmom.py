from random import randint
from time import sleep
from uwu import generateUwU
from jimmytoken import giveToken
import os

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
    elif (randint(1, 100) == 69) or message.content.startswith('%rand'):
        os.system("python3 gpt2/sequence_generator.py --seq-len 16384 --context hey >> temp.txt")
        sleep(10)
        f = open("temp.txt")
        first = False
        bigstring = ""
        for line in f:
            if first:
                bigstring += line
            first = True
        f.close()
        os.system("rm temp.txt")
        await message.channel.send(first)


client.run(giveToken())
