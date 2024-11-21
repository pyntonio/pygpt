# business_tools/data_analysis.py
import numpy as np

class DataAnalysis:
    def __init__(self):
        pass

    def summarize_data(self, data):
        return {
            "mean": np.mean(data),
            "median": np.median(data),
            "std_dev": np.std(data)
        }
