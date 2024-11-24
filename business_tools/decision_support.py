# business_tools/decision_support.py
import openai

class DecisionSupport:
    def __init__(self, api_key):
        openai.api_key = api_key

    def analyze_decision(self, pros, cons, weights=None):
        """
        Analizza una decisione basandosi sui pro e contro forniti, includendo ponderazioni opzionali.
        """
        pros_score = sum(weights.get(p, 1) for p in pros) if weights else len(pros)
        cons_score = sum(weights.get(c, 1) for c in cons) if weights else len(cons)

        if pros_score > cons_score:
            analysis = "The decision seems favorable based on the pros."
        elif cons_score > pros_score:
            analysis = "The decision seems unfavorable based on the cons."
        else:
            analysis = "The decision seems balanced."

        return {
            "pros_count": len(pros),
            "cons_count": len(cons),
            "pros_score": pros_score,
            "cons_score": cons_score,
            "analysis": analysis,
        }

    def generate_gpt_insights(self, pros, cons, context="general"):
        """
        Usa OpenAI GPT per generare un'analisi approfondita della decisione.
        """
        prompt = (
            f"Analyze the following decision-making scenario:\n"
            f"Pros: {', '.join(pros)}\nCons: {', '.join(cons)}\n"
            f"Provide a detailed analysis and actionable suggestions within the context of {context}."
        )
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()

    def generate_decision_matrix(self, options, criteria, weights=None):
        """
        Genera una matrice decisionale con punteggi basati su criteri e ponderazioni.
        """
        matrix = {}
        for option, criteria_scores in options.items():
            weighted_score = sum(
                criteria_scores[criterion] * (weights.get(criterion, 1) if weights else 1)
                for criterion in criteria_scores
            )
            matrix[option] = {
                "scores": criteria_scores,
                "weighted_score": weighted_score,
            }
        return matrix

    def recommend_best_option(self, decision_matrix):
        """
        Raccomanda l'opzione migliore basandosi sui punteggi ponderati.
        """
        best_option = max(decision_matrix, key=lambda x: decision_matrix[x]["weighted_score"])
        return {
            "best_option": best_option,
            "details": decision_matrix[best_option],
        }
