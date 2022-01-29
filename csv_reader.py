import os
import pandas as pd

class CSV_Reader:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
    
    def clean_name(self, name):
        name = name.split()
        return " ".join(name)

    def extract_details(self):
        promoter_details = {}

        promoter_names = [self.clean_name(name) for name in list(self.df['Name'])]       
        promoter_nicknames = list(self.df['Nickname'])     
        promoter_numbers= list(self.df['Mobile Number'])

        for (name, nickname, phone_number) in zip(promoter_names, promoter_nicknames, promoter_numbers):
            promoter_details[str(name)] = {"Nickname" : str(nickname), "Mobile Number": str(phone_number)}

        return promoter_details

    # def extract_names(self):
    #     promoter_names = list(self.df['Name'])
    #     return [self.clean_name(name) for name in promoter_names]
