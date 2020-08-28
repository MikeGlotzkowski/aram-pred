import pymongo as pm
import os
import sys


class Mongo:

    def __init__(self):
        username = os.environ.get('MONGO_USERNAME')
        password = os.environ.get('MONGO_PASSWORD')
        client = pm.MongoClient(
            f'mongodb://{username}:{password}@127.0.0.1:27017/')
        db = client['aram_data']
        self.player_collection = db['player_collection']
        self.raw_match_history = db['raw_match_history']
        self.raw_match_details = db['raw_match_details']

    def insert_player(self, player_as_json):
        self.insert_if_not_exists(player_as_json,
                                  self.player_collection, 'currentAccountId')

    def insert_match_history(self, encrypted_account_id, match_history):
        self.insert_if_not_exists({'accountId': encrypted_account_id, 'matchHistory': match_history},
                                  self.raw_match_history, 'accountId')

    def insert_match_details(self, match_detail_as_json):
        self.insert_if_not_exists(match_detail_as_json,
                                  self.raw_match_details, 'gameId')

    def insert_if_not_exists(self, obj, collection, _key):
        try:
            obj['_id'] = obj[_key]
            collection.insert_one(obj)
        except pm.errors.DuplicateKeyError:
            pass
        except:
            print(sys.exc_info()[0])
