# education_tools/quiz_generator.py
import random

class QuizGenerator:
    def __init__(self):
        pass

    def generate_quiz(self, questions_and_answers):
        quiz = []
        for q, a in questions_and_answers.items():
            quiz.append({"question": q, "answer": a, "options": random.sample(list(questions_and_answers.values()), 3)})
        return quiz
