# assistants/mindfulness_assistant.py
import openai

class MindfulnessAssistant:
    def __init__(self, api_key):
        openai.api_key = api_key

    def daily_meditation(self, mood="neutral"):
        """
        Genera una meditazione giornaliera personalizzata in base all'umore.
        """
        prompt = (
            f"Create a daily meditation exercise for someone feeling {mood}. "
            "The exercise should be simple, calming, and suitable for a 5-minute practice."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()

    def guided_meditation(self, goal="relaxation"):
        """
        Fornisce una meditazione guidata in base a un obiettivo specifico.
        """
        prompt = (
            f"Write a guided meditation script aimed at achieving {goal}. "
            "Make it soothing, clear, and easy to follow for beginners."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()

    def stress_relief_tips(self):
        """
        Suggerisce 5 consigli pratici per la gestione dello stress.
        """
        prompt = (
            "Provide 5 practical stress relief tips based on mindfulness techniques. "
            "Each tip should be concise and easy to apply."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()

    def journaling_prompt(self):
        """
        Fornisce un suggerimento per il journaling basato sulla mindfulness.
        """
        prompt = (
            "Generate a reflective journaling prompt for someone practicing mindfulness. "
            "The prompt should encourage self-awareness and emotional exploration."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()

    def gratitude_exercise(self):
        """
        Suggerisce un esercizio di gratitudine basato sulla mindfulness.
        """
        prompt = (
            "Create a gratitude exercise suitable for a mindfulness practice. "
            "The exercise should be uplifting and encourage daily reflection."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
