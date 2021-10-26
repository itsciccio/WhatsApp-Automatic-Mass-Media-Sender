import os
import pandas as pd

class CSV_Reader:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
    
    def clean_name(self, name):
        name = name.split()
        return " ".join(name)

    def extract_names(self):
        promoter_names = list(self.df['Name'])
        return [self.clean_name(name) for name in promoter_names]
