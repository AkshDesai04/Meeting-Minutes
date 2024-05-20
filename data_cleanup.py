from prompter import prompter

VALUATE_PROMPT = 'Give me a precise decimal value of how important you think this sentence is between 0 and 1. Only give me the number.: '

def master_cleanup(list):
    print(list)
    print("hola start")
    list = manual_cleanup(list)
    print("Manual Cleanup Completed")
    print(list)
    list = prompted_cleanup(list)
    print("Prompted Cleanup Completed")
    print(list)
    # list = prompted_cleanup(list)

    return list

def manual_cleanup(list, word_count = 5):
    filler_words = ['um', 'uh', 'er', 'like', 'well', 'you know', 'so', 'anyway', 'i mean', 'actually', 'basically', 'literally', 'kind of', 'sort of', 'right', 'exactly', 'right', 'yeah', 'mhmm', 'hmm', 'thank you', 'thank you so much', 'thank you very much', 'I\'m with you']
    list = remove_small_sentences(list, word_count)
    list = remove_filler(list, filler_words, 0.5)
    return list

def remove_small_sentences(list, word_count):
    list = [item for item in list if len(item['text'].split()) >= word_count]
    return list

def remove_filler(list, fillers, filler_percentage=0.5):
    filtered_list = []
    
    for item in list:
        if 'text' not in item:
            continue
        
        original_text = item['text']
        modified_text = original_text
        
        # Convert both original text and fillers to lowercase
        original_text_lower = original_text.lower()
        fillers_lower = [filler.lower() for filler in fillers]
        
        # Remove fillers from the modified text while preserving case
        for filler in fillers_lower:
            modified_text = original_text_lower.replace(filler, '')
        
        original_length = len(original_text)
        modified_length = len(modified_text)

        print(original_text)
        print(modified_length / original_length)
        print(modified_length / original_length >= filler_percentage)
        print()
        print()
        print()

        if modified_length / original_length >= filler_percentage:
            filtered_list.append(item)
    
    list[:] = filtered_list
    return list

def prompted_cleanup(list, threshold=0.8):
    cleaned_list = []
    for item in list:
        try:
            # Prompt user for input and convert it to a float
            user_input = float(prompter.prompt(VALUATE_PROMPT, item['text']).strip())
            # Check if the input is above or equal to the threshold
            if user_input >= threshold:
                cleaned_list.append(item)
        except ValueError:
            print("Invalid input! Please provide a valid decimal number between 0 and 1.")
    return cleaned_list
