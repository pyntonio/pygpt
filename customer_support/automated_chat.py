# customer_support/automated_chat.py
import openai

class AutomatedChat:
    def __init__(self, api_key):
        openai.api_key = api_key

    def respond_to_customer(self, message):
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Usa 'model' invece di 'engine'
            messages=[{"role": "user", "content": f"Provide a helpful and polite response to: {message}"}],  # Usa 'messages' con il contenuto del prompt
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()  # Accedere al contenuto della risposta
