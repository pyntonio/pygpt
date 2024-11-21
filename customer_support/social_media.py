# content_generation/social_media.py
import openai

class SocialMedia:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_post(self, topic):
        prompt = f"Write a social media post about {topic}."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()
