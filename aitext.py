import subprocess

def aitext(message):
    process = subprocess.Popen("cd /home/jimmysmom/JimmysMomBot/venv/bin && source activate && cd /home/jimmysmom/JimmysMomBot/gpt2old/src && python generate_unconditional_samples.py --top_k 40 --model_name tempmod", stdout=subprocess.PIPE, shell=True)
    processout = process.communicate()[0].strip()
    return (processout)
