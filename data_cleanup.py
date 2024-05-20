from prompter import prompter
from process_texts import process_texts_single_prompt

VALUATE_PROMPT = 'Only reply with a decimal number. Give a decimal value of the importance of this sentence between 0 and 1: '

def master_cleanup(lst):
    print(lst)
    print("hola start")
    lst = manual_cleanup(lst)
    print("Manual Cleanup Completed")
    print(lst)
    lst = prompted_cleanup(lst)
    print("Prompted Cleanup Completed")
    print(lst)
    # list = prompted_cleanup(list)

    return lst

def manual_cleanup(lst, word_count = 5):
    filler_words = ['um', 'uh', 'er', 'like', 'well', 'you know', 'so', 'anyway', 'i mean', 'actually', 'basically', 'literally', 'kind of', 'sort of', 'right', 'exactly', 'right', 'yeah', 'mhmm', 'hmm', 'thank you', 'thank you so much', 'thank you very much', 'I\'m with you']
    lst = remove_small_sentences(lst, word_count)
    lst = remove_filler(lst, filler_words, 0.5)
    return lst

def remove_small_sentences(lst, word_count):
    lst = [item for item in lst if len(item['text'].split()) >= word_count]
    return lst

def remove_filler(lst, fillers, filler_percentage=0.5):
    filtered_list = []
    
    for item in lst:
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
    
    lst[:] = filtered_list
    return lst

def prompted_cleanup(lst, threshold=0.9):
    cleaned_list = []
    for item in lst:
        try:
            # Prompt user for input
            temp = prompter.prompt(VALUATE_PROMPT + item['text'], 0.1)
            # temp = " 0.9 "
            print("temp: ", temp)
            user_input = temp.strip()
            # Convert the input to a float
            user_input_float = float(user_input)
            # Check if the input is above or equal to the threshold
            if user_input_float >= threshold:
                # Temp
                process_texts_single_prompt(item['text'])
                # Temp
                cleaned_list.append(item)
        except ValueError:
            print("Invalid input! Please provide a valid decimal number between 0 and 1.")
    return cleaned_list
