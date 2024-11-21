# assistants/language_assistant.py
import openai

class LanguageAssistant:
    def __init__(self, api_key):
        openai.api_key = api_key

    def translate_text(self, text, target_language):
        prompt = f"Translate the following text to {target_language}: {text}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
