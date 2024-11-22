# content_generation/social_media.py
import openai

class SocialMedia:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_post(self, topic):
        prompt = f"Write a social media post about {topic}."
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Usa 'model' invece di 'engine'
            messages=[{"role": "user", "content": prompt}],  # Usa 'messages' per il contenuto
            max_tokens=100,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()  # Accesso al contenuto della risposta
