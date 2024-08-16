from transformers import GPT2Tokenizer, GPT2LMHeadModel

def load_model(model_name="gpt2-large"):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    return tokenizer, model

def generate_text(tokenizer, model, prompt, max_length=100, temperature=0.7, top_p=0.9, repetition_penalty=1.2):
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
