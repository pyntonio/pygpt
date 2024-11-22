import openai

class WritingAssistant:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate_text(self, prompt: str):
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Modello che stai utilizzando
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response['choices'][0]['message']['content']

    def generate_story(self, theme: str):
        prompt = f"Write a creative story about the theme: {theme}."
        return self.generate_text(prompt)
