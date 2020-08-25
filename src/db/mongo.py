from pymongo import MongoClient
import os

username = os.environ.get("MONGO_USERNAME")
password = os.environ.get("MONGO_PASSWORD")

client = MongoClient(
    "mongodb://{0}:{1}@localhost:27017/".format(username, password))
db = client['aram_data']
collection = db['raw_match_history']


def insert_json(json_data):
    id = collection.insert_one(json_data).inserted_id
    return id
