from gpt4all import GPT4All
model = GPT4All("nous-hermes-llama2-13b.Q4_0.gguf")
model = GPT4All(model_name='nous-hermes-llama2-13b.Q4_0.gguf')
with model.chat_session():
    response0 = model.generate(prompt='prompt 1', temp=0)
    print(response0)
    response0 = model.generate(prompt='prompt 2', temp=0)
    print(response1)