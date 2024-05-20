from prompter import prompter

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
    print(text)
    prompt_summarize = "Simplify this statement in less with 15 words: " + str(text)
    # print(prompt_summarize)
    prompt_categorize = "Reply in one word only. Is this statement a \'Information\' \'Decision\', or \'Action Item\': " + str(text)
    # print(prompt_categorize)

    summary = prompter.prompt(prompt_summarize)
    print(summary)
    category = prompter.prompt(prompt_categorize)
    print(category)
    
    print("Statement: " + text)
    print("Summary: " + summary)
    print("Category: " + category)