import os
import re

def aitext(message):
    os.system('cd /home/jimmysmom/JimmysMomBot/venv/bin && source activate && cd /home/jimmysmom/JimmysMomBot/gpt2old && python generate_unconditional_samples.py --top_k 40 --model_name tempmod >> ../temp.txt')
    f = open("temp.txt")
    first = False
    bigstring = ""
    for line in f:
        if first:
             bigstring += line
        first = True
    f.close()
    os.system("rm temp.txt")
    return (bigstring)
