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
        phrases[:] = [x for x in phrases if ((x != "<|endoftext|>") and (x != "{Attachments}"))] 
    retval = phrases[0]
    phrases.pop(0)
    return retval

def contextgen(context):
    global sess
    response = gpt2.generate(sess, length=30, prefix=context, nsamples=1, batch_size=1, truncate='\n', include_prefix=False, return_as_list=True)
    return response[0]

