from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers.onnx import export
from pathlib import Path

# Load the model and tokenizer
model_name = "gpt2-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Define the ONNX export path
onnx_model_path = Path("gpt2_medium.onnx")

# Export the model to ONNX format
export(
    model=model,
    tokenizer=tokenizer,
    opset=11,  # Set the ONNX opset version
    output=onnx_model_path,
)

print(f"Model exported to {onnx_model_path}")
