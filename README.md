#Simple Chatbot with Math Calculation
#This is a simple chatbot built using Microsoft's DialoGPT-medium model that can both chat conversationally and evaluate basic math expressions typed by the user.

Features
Conversational Chatbot: Powered by the DialoGPT-medium transformer model for casual and friendly conversations.

Math Calculation: Detects and evaluates simple math expressions involving addition (+), subtraction (-), multiplication (x or *), and division (/).

Easy to use: Just type your message and get a reply. Type math expressions to get quick calculations.

Exit anytime: Type exit or quit to end the conversation.

#Requirements
Python 3.7+

transformers library

torch

sympy (optional, you import it but currently not used)

re (regular expressions)

Install required Python packages with:

bash
Copy
Edit
pip install transformers torch sympy
How to Run
Save the chatbot code to a Python file, e.g., chatbot.py.

Run the script:

bash
Copy
Edit
python chatbot.py
Start chatting! Examples:

yaml
Copy
Edit
Toi : Hello!
Bot: Hi there!

Toi : 15 + 4
Bot: 15+4 = 19

Toi : What is 12 x 8?
Bot: 12*8 = 96

Toi : exit
Bot: Goodbye!
Code Overview
extract_math_expression(text): Uses regex to find simple math expressions in user input.

evaluate_math_expression(expr): Replaces 'x' with '*' and evaluates the expression safely with Python's eval().

Chat history is maintained to provide context-aware conversational replies using DialoGPT.

If a math expression is detected, it replies with the calculated result instead of chatting.

Notes
Only supports simple two-number expressions like 3 + 4 or 7 x 8.

For security reasons, avoid using eval() on untrusted input in production.

The chatbot runs locally and requires an internet connection on first run to download the DialoGPT model.
