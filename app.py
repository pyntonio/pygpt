# app.py
from fastapi import FastAPI
from assistants.personal_assistant import PersonalAssistant
from customer_support.automated_chat import AutomatedChat
from content_generation.social_media import SocialMedia
from psychological_support.motivation import Motivation
from business_tools.decision_support import DecisionSupport
from education_tools.lesson_plans import LessonPlans

app = FastAPI()

assistant = PersonalAssistant()
writing_assistant = WritingAssistant("your-openai-api-key")
language_assistant = LanguageAssistant("your-openai-api-key")
chat_assistant = AutomatedChat("your-openai-api-key")
social_media = SocialMedia("your-openai-api-key")
motivation = Motivation()
decision_support = DecisionSupport()
lesson_plans = LessonPlans()

@app.get("/tasks")
def get_tasks():
    return assistant.view_tasks()

@app.post("/tasks")
def add_task(task: str, due_date: str):
    return assistant.add_task(task, due_date)

@app.get("/generate_story/{theme}")
def generate_story(theme: str):
    return writing_assistant.generate_story(theme)

@app.get("/translate")
def translate_text(text: str, target_language: str):
    return language_assistant.translate_text(text, target_language)

@app.get("/respond")
def respond_to_customer(message: str):
    return chat_assistant.respond_to_customer(message)

@app.get("/social_media")
def generate_post(topic: str):
    return social_media.generate_post(topic)

@app.get("/motivational_quote")
def get_motivational_quote():
    return motivation.get_random_motivational_quote()

@app.get("/analyze_decision")
def analyze_decision(pros: list, cons: list):
    return decision_support.analyze_decision(pros, cons)

@app.get("/create_lesson_plan")
def create_lesson_plan(subject: str, topic: str, duration: int):
    return lesson_plans.create_lesson_plan(subject, topic, duration)
