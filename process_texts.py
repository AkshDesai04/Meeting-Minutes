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
    print("Statement: " + str(text['text']))
    prompt_summarize = "Summarize this sentence for me: " + str(text['text'])
    print("Summary: " + summary)
    prompt_categorize = "Is this sentence a \'Information\' \'Decision\', or \'Action Item\': " + str(text['text'])
    print("Category: " + category)

    summary = prompter.prompt(prompt_summarize)
    category = prompter.prompt(prompt_categorize)

    print(summary)
    print(category)