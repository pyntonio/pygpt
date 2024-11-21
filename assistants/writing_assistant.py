# assistants/writing_assistant.py
import openai

class WritingAssistant:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_text(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()

    def generate_story(self, theme):
        prompt = f"Write a creative story about {theme}."
        return self.generate_text(prompt)
