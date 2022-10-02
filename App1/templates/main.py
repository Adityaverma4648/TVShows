import csv 
import json
import os

def make_json(csvFilePath , jsonFilePath):
    #create a dictonary
    data = {}

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['ID']
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))            



csvFilePath = r'C:\Users\adity\OneDrive\Documents\GitHub\pythonDataAnalysis-TVShows\App1\templates\tv_shows.csv'
jsonFilePath = r'C:\Users\adity\OneDrive\Documents\GitHub\pythonDataAnalysis-TVShows\App1\templates\tv_shows.json'

make_json(csvFilePath, jsonFilePath)

# import pandas as pd
# df = pd.read_csv (r'C:\Users\adity\OneDrive\Documents\GitHub\pythonDataAnalysis-TVShows\App1\templates\tv_shows.csv')
# df.to_json (r'C:\Users\adity\OneDrive\Documents\GitHub\pythonDataAnalysis-TVShows\App1\templates\tv_shows.json')