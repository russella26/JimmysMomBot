import gpt_2_simple as gpt2

def aitext(hello):
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)
    single_text = gpt2.generate(sess, return_as_list=True)[0]
    retval = single_text.splitlines()
    return retval[0]
