# business_tools/decision_support.py
class DecisionSupport:
    def __init__(self):
        pass

    def analyze_decision(self, pros, cons):
        if len(pros) > len(cons):
            return "The decision seems favorable based on the pros."
        elif len(cons) > len(pros):
            return "The decision seems unfavorable based on the cons."
        else:
            return "The decision seems balanced."
