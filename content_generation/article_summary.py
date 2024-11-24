# content_generation/article_summary.py
import openai

class ArticleSummary:
    def __init__(self, api_key):
        openai.api_key = api_key

    def summarize_article(self, article, length="short", style="neutral"):
        """
        Riassume un articolo con opzioni per la lunghezza e lo stile.
        :param article: Testo dell'articolo.
        :param length: 'short', 'medium', o 'detailed'.
        :param style: 'neutral', 'formal', o 'informal'.
        :return: Riassunto generato.
        """
        length_prompt = {
            "short": "Summarize briefly in a few sentences.",
            "medium": "Provide a balanced summary in one paragraph.",
            "detailed": "Summarize the article comprehensively."
        }
        style_prompt = {
            "neutral": "Use a neutral tone.",
            "formal": "Use a formal tone appropriate for professional settings.",
            "informal": "Use an engaging and casual tone."
        }

        prompt = (
            f"{length_prompt.get(length, 'Summarize briefly.')}\n"
            f"{style_prompt.get(style, 'Use a neutral tone.')}\n"
            f"Article: {article}"
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300 if length == "detailed" else 150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()

    def extract_key_points(self, article, num_points=5):
        """
        Estrae i punti chiave dall'articolo.
        :param article: Testo dell'articolo.
        :param num_points: Numero di punti chiave da generare.
        :return: Lista di punti chiave.
        """
        prompt = (
            f"Extract the {num_points} key points from the following article:\n"
            f"{article}"
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100 + num_points * 20,
            temperature=0.5
        )
        return response['choices'][0]['message']['content'].strip()

    def generate_questions(self, article, num_questions=3):
        """
        Genera domande basate sull'articolo per verificare la comprensione o stimolare discussioni.
        :param article: Testo dell'articolo.
        :param num_questions: Numero di domande da generare.
        :return: Lista di domande.
        """
        prompt = (
            f"Based on the following article, generate {num_questions} thoughtful questions:\n"
            f"{article}"
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50 + num_questions * 30,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()

    def rewrite_summary(self, article, target_audience="general"):
        """
        Riscrive il riassunto adattandolo a un pubblico specifico.
        :param article: Testo dell'articolo.
        :param target_audience: Pubblico target, ad esempio 'students', 'business professionals', ecc.
        :return: Riassunto riscritto.
        """
        prompt = (
            f"Rewrite the summary of the following article for a target audience of {target_audience}:\n"
            f"{article}"
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
