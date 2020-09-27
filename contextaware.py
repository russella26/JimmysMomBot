import subprocess

def contextaware(message):
    process = subprocess.Popen('cd /home/jimmysmom/JimmysMomBot/gpt2old/src && /home/jimmysmom/JimmysMomBot/venv/bin/python interactive_conditional_samples_context.py --top_k 40 --model_name thegoodone --nsamples 1 --length 100 --wadtext "' + message[5:]  + '"' , stdout=subprocess.PIPE, shell=True)
    processout = process.communicate()[0].strip()
    return (message[5:] + processout.decode("utf-8"))
