from codecs import ignore_errors
import requests
import pandas as pd

sheet_url = open('local/sheet_url.txt').readline()
response = requests.get(sheet_url)

retrieved_data = response.content.decode('utf-8').replace('\r','').split('\n')

promoter_data = [promoter.split(',') for promoter in retrieved_data[1:]]

all_promoter_dict = []
for promoter in promoter_data:
    promoter_dict = {
        'Name': promoter[0],
        'Mobile Number': promoter[1],
        'Nickname': promoter[2],
        'Gender': promoter[3],
        'Year': promoter[4],
        'Notes': promoter[5]
    }
    all_promoter_dict.append(promoter_dict)

dataframe = pd.DataFrame(all_promoter_dict)

dataframe.to_csv("csv_files/GS - OD Promoters.csv", index=False)

