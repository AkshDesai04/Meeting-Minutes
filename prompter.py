from gpt4all import GPT4All

class prompter:
    model = None
    def __init__(self):
        print("Holaaaaaaa")
        model = GPT4All("nous-hermes-llama2-13b.Q4_0.gguf")
        model = GPT4All(model_name='nous-hermes-llama2-13b.Q4_0.gguf')

    def prompt(input, temperature = 0):
        model = GPT4All("nous-hermes-llama2-13b.Q4_0.gguf") # Temp fix
        model = GPT4All(model_name='nous-hermes-llama2-13b.Q4_0.gguf') # Temp fix
        with model.chat_session():
            return(model.generate(prompt=input, temp=temperature))