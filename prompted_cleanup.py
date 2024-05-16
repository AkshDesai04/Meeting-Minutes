import prompter

VALUATE_PROMPT = 'Give me a precise decimal value of how important you think this sentence is between 0 and 1. Only give me the number.: '

def prompted_cleanup(list, threshold=0.8):
    for item in list:
        if int(prompter.prompt(VALUATE_PROMPT, item['text']).trim()) < threshold:
            list.remove(item)
    return list