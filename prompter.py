import tensorflow as tf
from transformers import TFAutoModelForCausalLM, AutoTokenizer

def prompt(inputs):
    
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
    
    generated_texts = []

    for input_text in inputs:
        try:
            # Tokenize the prompt
            print("Input: " + input_text)
            inputs = tokenizer(input_text, return_tensors="tf")

            # Generate outputs
            outputs = model.generate(inputs["input_ids"], max_length=50)

            # Decode the outputs
            generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            print("Response: " + generated_text)
            generated_texts.append(generated_text)

            print("Output: " + generated_text)
        
        except Exception as e:
            generated_texts.append("")

    print("--------------------Ending--------------------")
    
    return generated_texts
