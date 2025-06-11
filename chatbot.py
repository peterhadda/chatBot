from sympy import evaluate
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import re

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
print("DialoGPT chatbot ready! Type 'exit' to quit")

chat_history_ids=None
def extract_math_expression(text):
    match = re.search(r"(\d+\s*[\+\-\*/xX]\s*\d+)", text)
    if match:
        return match.group(1)
    return None

def evaluate_math_expression(expr):
    expr = expr.lower().replace('x', '*')
    try:
        result = eval(expr)
        return f"{expr} = {result}"
    except:
        return "Je ne peux pas calculer cela."

while True:
    user_input = input("Toi : ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bot: Goodbye!")
        break

    math_expr = extract_math_expression(user_input)
    if math_expr:
        response = evaluate_math_expression(math_expr)
    else:
        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
        if chat_history_ids is not None:
            bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)
        else:
            bot_input_ids = new_input_ids

        chat_history_ids = model.generate(
            bot_input_ids,
            max_length=1000,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.7
        )

        response = tokenizer.decode(
            chat_history_ids[:, bot_input_ids.shape[-1]:][0],
            skip_special_tokens=True
        )

    print(f"Bot: {response}\n")


