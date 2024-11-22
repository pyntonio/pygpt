# assistants/language_assistant.py
import openai

class LanguageAssistant:
    def __init__(self, api_key):
        openai.api_key = api_key

    def translate_text(self, text, target_language):
        prompt = f"Translate the following text to {target_language}: {text}"
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Usa 'model' al posto di 'engine'
            messages=[{"role": "user", "content": prompt}],  # 'messages' è il formato corretto
            max_tokens=100,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()  # Accesso al contenuto della risposta
