from pymongo.mongo_client import MongoClient
import pandas as pd
import json


import urllib.parse

username = urllib.parse.quote_plus("anandbhagat345")
password = urllib.parse.quote_plus("MilyYoZdlunsiq59")

uri = f"mongodb+srv://{username}:{password}@cluster0.3yla3.mongodb.net/?appName=Cluster0"

#create new client and connect to server
client = MongoClient(uri)

df = pd.read_csv("C:\Users\anand\OneDrive\Desktop\sensorproject\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)

#converting into json

json_record = list(json.loads(df.T.to_json()).values())
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)