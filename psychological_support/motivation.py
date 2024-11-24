# psychological_support/motivation.py
import openai
import random

class Motivation:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.quotes_by_context = {
            "personal_growth": [
                "The only limit to our realization of tomorrow is our doubts of today.",
                "Don’t watch the clock; do what it does. Keep going.",
                "What you get by achieving your goals is not as important as what you become by achieving your goals."
            ],
            "overcoming_challenges": [
                "It’s not whether you get knocked down, it’s whether you get up.",
                "When you come to the end of your rope, tie a knot and hang on.",
                "Out of difficulties grow miracles."
            ],
            "teamwork": [
                "Coming together is a beginning, staying together is progress, and working together is success.",
                "Alone we can do so little; together we can do so much.",
                "Success is best when it’s shared."
            ],
            "self_confidence": [
                "You are braver than you believe, stronger than you seem, and smarter than you think.",
                "Self-confidence is the first requisite to great undertakings.",
                "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."
            ],
            "resilience": [
                "Strength grows in the moments when you think you can't go on but you keep going anyway.",
                "Fall seven times, stand up eight.",
                "You may have to fight a battle more than once to win it."
            ],
            "change": [
                "The secret of change is to focus all your energy not on fighting the old but on building the new.",
                "Life is 10% what happens to us and 90% how we react to it.",
                "If you don’t like something, change it. If you can’t change it, change your attitude."
            ],
        }

    def get_random_motivational_quote(self, context="personal_growth"):
        """
        Restituisce una citazione motivazionale casuale in base al contesto.
        """
        if context in self.quotes_by_context:
            return random.choice(self.quotes_by_context[context])
        else:
            return "Context not found. Please try again with a valid context."

    def generate_personalized_quote(self, context="general"):
        """
        Genera una citazione motivazionale personalizzata utilizzando OpenAI GPT.
        """
        prompt = (
            f"Generate a motivational quote suitable for someone in the context of {context}. "
            "Make it uplifting and inspiring."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=60,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()

    def motivational_paragraph(self, context="overcoming challenges"):
        """
        Genera un breve paragrafo motivazionale su un tema specifico.
        """
        prompt = (
            f"Write a motivational paragraph to inspire someone who is facing {context}. "
            "The tone should be uplifting, empathetic, and encouraging."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
