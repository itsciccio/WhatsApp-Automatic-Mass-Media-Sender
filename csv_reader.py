import os
import pandas as pd

class CSV_Reader:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
    
    def extract_names(self):
        return list(self.df['Name'])