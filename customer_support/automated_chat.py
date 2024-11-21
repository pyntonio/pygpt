# customer_support/automated_chat.py
import openai

class AutomatedChat:
    def __init__(self, api_key):
        openai.api_key = api_key

    def respond_to_customer(self, message):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Provide a helpful and polite response to: {message}",
            max_tokens=150
        )
        return response.choices[0].text.strip()
