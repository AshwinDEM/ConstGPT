import torch
from transformers import BertTokenizer, BertForSequenceClassification
from safetensors.torch import load_file

# Define the path to the model directory
model_dir = './models/sciqa-bert'

tokenizer = BertTokenizer.from_pretrained(model_dir)
model = BertForSequenceClassification.from_pretrained(model_dir)

# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Example question and options
question = "What is the boiling point of water?"
options = ["10", "50", "100", "200"]

# Tokenize inputs
texts = [f"{question} {option}" for option in options]
inputs = tokenizer(texts, truncation=True, padding=True, return_tensors="pt").to(device)

# Run inference
with torch.no_grad():
    outputs = model(**inputs)

# Get predicted label
predictions = torch.argmax(outputs.logits, dim=-1)
predicted_option = options[predictions[0].item()]  # Correctly access scalar value

print(f"Question: {question}")
print(f"Options: {options}")
print(f"Predicted Answer: {predicted_option}")