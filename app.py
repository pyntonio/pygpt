from fastapi import FastAPI, UploadFile, File, Query
from fastapi.responses import FileResponse
from assistants.personal_assistant import PersonalAssistant
from customer_support.automated_chat import AutomatedChat
from content_generation.article_summary import ArticleSummary
from content_generation.social_media import SocialMedia
from psychological_support.motivation import Motivation
from psychological_support.mindfulness import MindfulnessAssistant
from business_tools.decision_support import DecisionSupport
from business_tools.data_analysis import DataAnalysis
from business_tools.stock_analysis import StockAnalysis
from business_tools.portfolio_generator import PortfolioGenerator
from education_tools.lesson_plans import LessonPlans
from assistants.language_assistant import LanguageAssistant
from assistants.writing_assistant import WritingAssistant
from image_tools.image_generation import ImageGenerator
from image_tools.image_upload import ImageUploader
from image_tools.image_editing import ImageEditor
from image_tools.inpainting import Inpainting
from image_tools.creative_composition import CreativeComposition
import os
from dotenv import load_dotenv

load_dotenv()

# Carica la chiave API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Inizializza gli assistenti
assistant = PersonalAssistant()
writing_assistant = WritingAssistant(OPENAI_API_KEY)
language_assistant = LanguageAssistant(OPENAI_API_KEY)
chat_assistant = AutomatedChat(OPENAI_API_KEY)
article_summary = ArticleSummary(OPENAI_API_KEY)
social_media = SocialMedia(OPENAI_API_KEY)
motivation = Motivation(OPENAI_API_KEY)
mindfulness = MindfulnessAssistant(OPENAI_API_KEY)
decision_support = DecisionSupport(OPENAI_API_KEY)
data_analysis = DataAnalysis(OPENAI_API_KEY)
stock_analysis = StockAnalysis(OPENAI_API_KEY)
portfolio_generator = PortfolioGenerator(OPENAI_API_KEY)
lesson_plans = LessonPlans()

# Inizializza i moduli per la gestione delle immagini
image_generator = ImageGenerator(OPENAI_API_KEY)
image_uploader = ImageUploader()
image_editor = ImageEditor()
inpainting = Inpainting(OPENAI_API_KEY)
creative_composition = CreativeComposition(OPENAI_API_KEY)

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

@app.get("/create_lesson_plan")
def create_lesson_plan(subject: str, topic: str, duration: int):
    return lesson_plans.create_lesson_plan(subject, topic, duration)

# Nuovi endpoint per la gestione delle immagini

@app.post("/images/generate")
async def generate_image(prompt: str, size: str = "1024x1024"):
    return await image_generator.generate_image(prompt, size)

@app.post("/images/upload")
async def upload_image(file: UploadFile = File(...)):
    return await image_uploader.upload_image(file)

@app.post("/images/edit")
async def edit_image(file_path: str, operation: str, params: dict = {}):
    return await image_editor.edit_image(file_path, operation, **params)

@app.post("/inpaint_image")
def inpaint_image_endpoint(image_url: str, mask_url: str, description: str):
    return inpainting.inpaint_image(image_url, mask_url, description)

@app.post("/creative_composition")
def creative_composition_endpoint(description: str):
    return creative_composition.create_creative_composition(description)

# Content generation

@app.get("/social_media")
def generate_post(topic: str):
    return social_media.generate_post(topic)

@app.post("/article/summarize")
def summarize_article_endpoint(article: str, length: str = "short", style: str = "neutral"):
    """
    Riassume un articolo con opzioni per lunghezza e stile.
    """
    return article_summary.summarize_article(article, length, style)

@app.post("/article/key_points")
def extract_key_points_endpoint(article: str, num_points: int = 5):
    """
    Estrae i punti chiave dall'articolo.
    """
    return {"key_points": article_summary.extract_key_points(article, num_points)}

@app.post("/article/questions")
def generate_questions_endpoint(article: str, num_questions: int = 3):
    """
    Genera domande basate sull'articolo.
    """
    return {"questions": article_summary.generate_questions(article, num_questions)}

@app.post("/article/rewrite")
def rewrite_summary_endpoint(article: str, target_audience: str = "general"):
    """
    Riscrive il riassunto adattandolo a un pubblico specifico.
    """
    return {"rewritten_summary": article_summary.rewrite_summary(article, target_audience)}

# Parte di chiamate riservate a pysicological support

@app.get("/mindfulness/daily-meditation")
def daily_meditation(mood: str = "neutral"):
    """
    Endpoint per ottenere una meditazione giornaliera personalizzata.
    """
    return {"meditation": mindfulness.daily_meditation(mood)}

@app.get("/mindfulness/guided-meditation")
def guided_meditation(goal: str = "relaxation"):
    """
    Endpoint per ottenere una meditazione guidata personalizzata.
    """
    return {"guided_meditation": mindfulness.guided_meditation(goal)}

@app.get("/mindfulness/stress-relief-tips")
def stress_relief_tips():
    """
    Endpoint per suggerimenti pratici per la gestione dello stress.
    """
    return {"stress_relief_tips": mindfulness.stress_relief_tips()}

@app.get("/mindfulness/journaling-prompt")
def journaling_prompt():
    """
    Endpoint per ottenere un suggerimento di journaling.
    """
    return {"journaling_prompt": mindfulness.journaling_prompt()}

@app.get("/mindfulness/gratitude-exercise")
def gratitude_exercise():
    """
    Endpoint per ottenere un esercizio di gratitudine.
    """
    return {"gratitude_exercise": mindfulness.gratitude_exercise()}

@app.get("/motivation/random-quote")
def get_random_quote():
    """
    Endpoint per ottenere una citazione motivazionale casuale da contesti predefiniti.
    """
    return {"quote": motivation.get_random_motivational_quote()}

@app.get("/motivation/contextual-quote")
def get_contextual_quote(context: str = "personal_growth"):
    """
    Endpoint per ottenere una citazione motivazionale basata su un contesto specifico.
    """
    return {"quote": motivation.get_random_motivational_quote(context)}

@app.get("/motivation/personalized-quote")
def get_personalized_quote(context: str = "general"):
    """
    Endpoint per ottenere una citazione motivazionale personalizzata.
    """
    return {"quote": motivation.generate_personalized_quote(context)}

@app.get("/motivation/motivational-paragraph")
def get_motivational_paragraph(context: str = "overcoming challenges"):
    """
    Endpoint per ottenere un paragrafo motivazionale dettagliato.
    """
    return {"paragraph": motivation.motivational_paragraph(context)}


# Business tools


@app.post("/data/summarize")
def summarize_data(data: list):
    """
    Endpoint per ottenere una sintesi statistica di base per una lista di dati numerici.
    """
    return data_analysis.summarize_data(data)

@app.post("/data/analyze_dataframe")
def analyze_dataframe(file: UploadFile = File(...)):
    """
    Endpoint per ottenere statistiche descrittive da un file CSV caricato.
    """
    df = pd.read_csv(file.file)
    return data_analysis.analyze_dataframe(df)

@app.post("/data/outliers")
def detect_outliers(data: list, threshold: float = 1.5):
    """
    Endpoint per rilevare outliers in un dataset numerico.
    """
    return data_analysis.detect_outliers(data, threshold)

@app.post("/data/correlation_matrix")
def get_correlation_matrix(file: UploadFile = File(...)):
    """
    Endpoint per ottenere la matrice di correlazione da un file CSV.
    """
    df = pd.read_csv(file.file)
    return data_analysis.correlation_matrix(df)

@app.post("/data/generate_report")
def generate_analysis_report(data: list, context: str = "general"):
    """
    Endpoint per generare un report analitico utilizzando OpenAI GPT.
    """
    return {"report": data_analysis.generate_analysis_report(data, context)}

@app.post("/data/generate_dataframe_report")
def generate_dataframe_report(file: UploadFile = File(...), context: str = "general"):
    """
    Endpoint per generare un report analitico per un DataFrame utilizzando OpenAI GPT.
    """
    df = pd.read_csv(file.file)
    return {"report": data_analysis.generate_dataframe_report(df, context)}

@app.post("/decision/analyze")
def analyze_decision(pros: list, cons: list, weights: dict = None):
    """
    Endpoint per analizzare una decisione basandosi su pro e contro.
    """
    return decision_support.analyze_decision(pros, cons, weights)

@app.post("/decision/generate_insights")
def generate_decision_insights(pros: list, cons: list, context: str = "general"):
    """
    Endpoint per generare insight dettagliati basati su OpenAI GPT.
    """
    return {"insights": decision_support.generate_gpt_insights(pros, cons, context)}

@app.post("/decision/matrix")
def create_decision_matrix(options: dict, criteria: list, weights: dict = None):
    """
    Endpoint per creare una matrice decisionale con criteri e punteggi ponderati.
    """
    decision_matrix = decision_support.generate_decision_matrix(options, criteria, weights)
    return decision_matrix

@app.post("/decision/recommend")
def recommend_best_option(options: dict, criteria: list, weights: dict = None):
    """
    Endpoint per raccomandare l'opzione migliore basandosi su una matrice decisionale.
    """
    decision_matrix = decision_support.generate_decision_matrix(options, criteria, weights)
    best_option = decision_support.recommend_best_option(decision_matrix)
    return best_option

@app.post("/business_tools/analyze_stock_or_index")
async def analyze_stock_or_index(
    stock_name: str = Query(..., description="Name of the stock or index"),
    period: str = Query(..., description="Analysis period (e.g., 1 month, 1 year)"),
    additional_context: str = Query("", description="Additional details or context")
):
    try:
        # Genera l'analisi usando la funzione appropriata
        analysis = stock_analysis.analyze_stock_or_index(stock_name, period, additional_context)

        # Definisci il percorso del file nella directory "reports"
        directory = "reports"
        file_name = f"{stock_name}_analysis.docx"
        file_path = os.path.join(directory, file_name)

        # Assicurati che la directory esista
        os.makedirs(directory, exist_ok=True)

        # Genera il file Word
        stock_analysis.generate_word_report(analysis, file_path)

        # Restituisci l'analisi e un link per scaricare il file
        return {
            "analysis": analysis,
            "download_link": f"/download/{file_name}"
        }
    
    except Exception as e:
        return {"error": str(e)}


@app.post("/business_tools/generate_portfolio")
async def generate_portfolio(
    budget: float = Query(..., description="Investment budget"),
    goals: str = Query(..., description="Investment goals (e.g., growth, stability)"),
    timeline: str = Query(..., description="Investment timeline (e.g., 5 years)"),
    preferences: str = Query("", description="Optional preferences for the portfolio")
):
    portfolio = portfolio_generator.generate_portfolio(budget, goals, timeline, preferences)
    file_path = portfolio_generator.generate_word_report(portfolio, "portfolio_report.docx")
    return {"portfolio": portfolio, "download_link": f"/download/{os.path.basename(file_path)}"}

@app.get("/download/{file_name}")
async def download_file(file_name: str):
    file_path = os.path.join("reports", file_name)
    if not os.path.exists(file_path):
        return {"error": "File not found"}
    return FileResponse(file_path, media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", filename=file_name)