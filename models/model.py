from flask import Flask, request, jsonify
from transformers import GPT2Tokenizer, GPT2LMHeadModel

app = Flask(__name__)

# Load the model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_text(prompt, max_length=100, temperature=0.7, top_p=0.9, repetition_penalty=1.2):
    inputs = tokenizer(prompt, return_tensors='pt')
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask'] if 'attention_mask' in inputs else None
    outputs = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=max_length,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
        temperature=temperature,
        top_p=top_p,
        repetition_penalty=repetition_penalty
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get("question")
    response_text = generate_text(question)
    return jsonify({"answer": response_text})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
