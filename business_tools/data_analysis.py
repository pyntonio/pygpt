# business_tools/data_analysis.py
import numpy as np
import pandas as pd
import openai

class DataAnalysis:
    def __init__(self, api_key):
        openai.api_key = api_key

    def summarize_data(self, data):
        """
        Restituisce una sintesi statistica di base per una lista di numeri.
        """
        return {
            "mean": np.mean(data),
            "median": np.median(data),
            "std_dev": np.std(data),
            "min": np.min(data),
            "max": np.max(data),
            "range": np.max(data) - np.min(data),
        }

    def analyze_dataframe(self, df):
        """
        Restituisce statistiche descrittive di base per un DataFrame Pandas.
        """
        return df.describe().to_dict()

    def detect_outliers(self, data, threshold=1.5):
        """
        Rileva i valori anomali (outliers) utilizzando il metodo dell'IQR (Interquartile Range).
        """
        q1 = np.percentile(data, 25)
        q3 = np.percentile(data, 75)
        iqr = q3 - q1
        lower_bound = q1 - threshold * iqr
        upper_bound = q3 + threshold * iqr
        outliers = [x for x in data if x < lower_bound or x > upper_bound]
        return {"outliers": outliers, "lower_bound": lower_bound, "upper_bound": upper_bound}

    def correlation_matrix(self, df):
        """
        Calcola e restituisce una matrice di correlazione per un DataFrame.
        """
        correlation_matrix = df.corr()
        return correlation_matrix.to_dict()

    def generate_analysis_report(self, data, context="general"):
        """
        Usa OpenAI GPT per generare un report testuale sull'analisi dei dati.
        """
        prompt = (
            f"Analyze the following dataset: {data}. Provide insights and suggestions "
            f"related to the context of {context}. Make it clear and actionable."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()

    def generate_dataframe_report(self, df, context="general"):
        """
        Usa OpenAI GPT per generare un report testuale basato su un DataFrame.
        """
        prompt = (
            f"Analyze the following dataset in tabular form: {df.to_string(index=False)}. "
            f"Provide insights and suggestions for improving business strategies related to {context}."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
