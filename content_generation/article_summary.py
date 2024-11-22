# content_generation/article_summary.py
import openai

class ArticleSummary:
    def __init__(self, api_key):
        openai.api_key = api_key

    def summarize_article(self, article):
        prompt = f"Summarize the following article: {article}"
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Usa 'model' al posto di 'engine'
            messages=[{"role": "user", "content": prompt}],  # 'messages' è il formato corretto
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()  # Accesso al contenuto della risposta
