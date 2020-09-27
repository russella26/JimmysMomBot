import subprocess

def aitext(message):
    process = subprocess.Popen("cd /home/jimmysmom/JimmysMomBot/gpt2old/src && /home/jimmysmom/JimmysMomBot/venv/bin/python generate_unconditional_samples.py --top_k 40 --model_name tempmod --nsamples 1 --length 50", stdout=subprocess.PIPE, shell=True)
    processout = process.communicate()[0].strip()
    return (processout.decode("utf-8")[90:])
