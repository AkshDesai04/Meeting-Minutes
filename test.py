import onnxruntime as ort
from transformers import AutoTokenizer
import numpy as np

def load_onnx_model(onnx_model_path):
    # Load the ONNX model
    session = ort.InferenceSession(onnx_model_path)
    return session

def generate_response_onnx(prompt, tokenizer, session):
    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors="np", max_length=10240, truncation=True)
    input_ids = inputs["input_ids"]

    # Perform inference
    ort_inputs = {session.get_inputs()[0].name: input_ids}
    ort_outs = session.run(None, ort_inputs)
    logits = ort_outs[0]

    # Decode the output tokens
    output_ids = np.argmax(logits, axis=-1)
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return response

def main(prompt):
    model_name = "gpt2-medium"
    onnx_model_path = "gpt2_medium.onnx"

    # Load the tokenizer and ONNX model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    session = load_onnx_model(onnx_model_path)

    # Generate the response
    response = generate_response_onnx(prompt, tokenizer, session)
    return response

if __name__ == "__main__":
    prompt = "Your 10,000 character long prompt goes here..."
    response = main(prompt)
    print(response)
