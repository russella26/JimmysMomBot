import gpt_2_simple as gpt2

global sess
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
global phrases
phrases = []

def aitext(hello):
    global phrases
    global sess
    if not phrases:
        """gpt2.load_gpt2(sess)"""
        single_text = gpt2.generate(sess, return_as_list=True)[0]
        phrases = single_text.splitlines()
        phrases[:] = [x for x in phrases if x != "<|endoftext|>"] 
    retval = phrases[0]
    phrases.pop(0)
    return retval
