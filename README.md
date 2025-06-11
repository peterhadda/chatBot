# Simple Chatbot with Math Calculation

A simple chatbot using Microsoft's DialoGPT-medium model that can chat conversationally **and** evaluate basic math expressions.

---

## Features

- Conversational chatbot powered by DialoGPT-medium.
- Detects and evaluates simple math expressions involving:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (x or *)
  - Division (/)
- Maintains conversation context for more natural replies.
- Exit the chatbot by typing `exit` or `quit`.

---

## Requirements

- Python 3.7+
- Packages:
  - transformers
  - torch
  - sympy (optional)
  - re (standard Python library)

Install dependencies with:

```bash
pip install transformers torch sympy

