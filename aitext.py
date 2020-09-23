import os
import re

def aitext(message):
    os.system('cd /home/jimmysmom/JimmysMomBot/gpt2 && python3 sequence_generator.py --seq-len 2048 --context "' + (re.sub(r'^%rand','', message)) + '" >> ../temp.txt')
    f = open("temp.txt")
    first = False
    bigstring = ""
    for line in f:
        if first:
             bigstring += line
        first = True
    f.close()
    os.system("rm temp.txt")
    return (re.sub(r'^Generated seq by model:-','', bigstring))
