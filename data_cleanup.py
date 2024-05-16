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

def remove_filler(text_items, fillers, filler_percentage=0.5):
    filtered_items = []
    for item in text_items:
        text_words = item['text'].lower().split()  # Convert text to lowercase before splitting
        contains_filler = any(filler.lower() in text_words for filler in fillers)  # Convert fillers to lowercase for comparison
        text_length = len(text_words)
        filler_threshold = text_length * (1 - filler_percentage)
        if not contains_filler and text_length >= filler_threshold:
            filtered_items.append(item)
    return filtered_items

def prompted_cleanup(list, threshold=0.8):
    for item in list:
        if int(prompter.prompt(VALUATE_PROMPT, item['text']).trim()) < threshold:
            list.remove(item)
    return list