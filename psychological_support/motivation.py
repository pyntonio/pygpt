# psychological_support/motivation.py
import random

class Motivation:
    def __init__(self):
        self.quotes = [
            "Believe you can and you're halfway there.",
            "The only way to do great work is to love what you do.",
            "Success is not final, failure is not fatal: It is the courage to continue that counts."
        ]

    def get_random_motivational_quote(self):
        return random.choice(self.quotes)
