# content_generation/article_summary.py
import openai

class ArticleSummary:
    def __init__(self, api_key):
        openai.api_key = api_key

    def summarize_article(self, article):
        prompt = f"Summarize the following article: {article}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
