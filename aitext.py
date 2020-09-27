import subprocess
import re

def aitext(message):
    bigstring = subprocess.check_output('cd /home/jimmysmom/JimmysMomBot/venv/bin && source activate && cd /home/jimmysmom/JimmysMomBot/gpt2old/src && python generate_unconditional_samples.py --top_k 40 --model_name tempmod')
    return (bigstring)
