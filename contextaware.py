import subprocess

def contextaware(message):
    process = subprocess.Popen('cd /home/jimmysmom/JimmysMomBot/gpt2old/src && /home/jimmysmom/JimmysMomBot/venv/bin/python interactive_conditional_samples_context.py --top_k 40 --model_name thegoodone --nsamples 1 --length 100 --wadtext "' + " ".join(message.split().pop(0)) + '"' , stdout=subprocess.PIPE, shell=True)
    processout = process.communicate()[0].strip()
    return (processout.decode("utf-8")[90:])
