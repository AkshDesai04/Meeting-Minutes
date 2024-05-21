import prompter

def process_texts(list):
    for text in list:
        prompt_summarize = "Summarize this sentence for me: " + text['text']
        prompt_categorize = "Is this sentence a \'Information\' \'Decision\', or \'Action Item\': " + text['text']

        summary = prompter.prompt(prompt_summarize)
        category = prompter.prompt(prompt_categorize)

        print("Statement: " + text['text'])
        print("Summary: " + summary)
        print("Category: " + category)

        
def process_texts_single_prompt(text):
    print("Statement: " + text)
    prompt_summarize = "Summarize this statement in less with 10 words: " + str(text)
    prompt_categorize = "Reply in one word only. Is this statement a \'Information\' \'Decision\', or \'Action Item\': " + str(text)

    summary = prompter.prompt(prompt_summarize)
    print("summary: " + summary)
    category = prompter.prompt(prompt_categorize)
    print("category: " + category)
    
    print()
    print()
    print()