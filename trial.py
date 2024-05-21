# !python -m venv llama_env
# !source llama_env/bin/activate  # On Windows use `llama_env\Scripts\activate`

# !pip install torch transformers
# !pip install transformers tensorflow

import tensorflow as tf
from transformers import TFAutoModelForCausalLM, AutoTokenizer

def main():
    # Set this to your Hugging Face token if accessing a private model
    # Leave it as an empty string if using a public model
    hf_token = "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"  # e.g., "YOUR_HUGGINGFACE_TOKEN"

    # Set the model name. Use a public model like "gpt2" or replace with your private model name
    model_name = "gpt2"  # Replace with your model name if different

    # Load tokenizer and model
    if hf_token:
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=hf_token)
        model = TFAutoModelForCausalLM.from_pretrained(model_name, use_auth_token=hf_token)
    else:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = TFAutoModelForCausalLM.from_pretrained(model_name)

    # Ensure model is in evaluation mode
    model.trainable = False

    print("--------------------Starting--------------------")
    # Define your prompt
    prompt = "Summarize this statement in less with 10 words: I\'m saying earlier the one big mist was there travel claim tool which has come now in my in my earlier company also I was using a tool called Conquer."

    # Tokenize the prompt
    inputs = tokenizer(prompt, return_tensors="tf")

    # Generate outputs
    outputs = model.generate(inputs["input_ids"], max_length=50)

    # Decode the outputs
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Response: " + generated_text)
    print("--------------------Ending--------------------")

if __name__ == "__main__":
    main()