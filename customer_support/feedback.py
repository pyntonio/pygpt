# customer_support/feedback.py
class Feedback:
    def __init__(self):
        self.feedback_list = []

    def add_feedback(self, feedback, user):
        self.feedback_list.append({"user": user, "feedback": feedback})
        return "Feedback added."

    def analyze_feedback(self):
        positive_feedback = [f for f in self.feedback_list if "good" in f["feedback"]]
        negative_feedback = [f for f in self.feedback_list if "bad" in f["feedback"]]
        return {"positive": len(positive_feedback), "negative": len(negative_feedback)}
