from prompter import prompter

VALUATE_PROMPT = 'Give me a precise decimal value of how important you think this sentence is between 0 and 1. Only give me the number.: '

def master_cleanup(list):
    print(list)
    print("hola start")
    list = manual_cleanup(list)
    print(list)
    print("hola end")
    # list = prompted_cleanup(list)

    return list

def manual_cleanup(list, word_count = 5):
    filler_words = ['um', 'uh', 'er', 'like', 'well', 'you know', 'so', 'anyway', 'i mean', 'actually', 'basically', 'literally', 'kind of', 'sort of', 'right', 'exactly', 'right', 'yeah', 'mhmm', 'hmm', 'thank you', 'thank you so much', 'thank you very much']
    list = remove_small_sentences(list, word_count)
    list = remove_filler(list, filler_words, 0.5)
    return list

def remove_small_sentences(list, word_count):
    list = [item for item in list if len(item['text'].split()) >= word_count]
    return list

def remove_filler(list, fillers, filler_percentage=0.5):
    filtered_list = []
    
    for text in list:
        original_length = len(text)
        modified_text = text
        
        for filler in fillers:
            modified_text = modified_text.replace(filler, '')
        
        modified_length = len(modified_text)
        
        if modified_length/original_length >= filler_percentage:
            filtered_list.append(text)
    
    list[:] = filtered_list
    return list

def prompted_cleanup(list, threshold=0.8):
    for item in list:
        if int(prompter.prompt(VALUATE_PROMPT, item['text']).trim()) < threshold:
            list.remove(item)
    return list