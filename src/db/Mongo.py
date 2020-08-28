import pymongo as pm
import os
from monitoring import Logger
import sys


class Mongo:

    def __init__(self, logger):
        self.logger = logger
        username = os.environ.get('MONGO_USERNAME')
        password = os.environ.get('MONGO_PASSWORD')
        client = pm.MongoClient(
            f'mongodb://{username}:{password}@127.0.0.1:27017/')
        db = client['aram_data']
        self.player_collection = db['player_collection']
        self.raw_match_history = db['raw_match_history']
        self.raw_match_details = db['raw_match_details']
        self.logger.log('info', 'Database connection established.')

    @Logger.Logger()
    def insert_match_history(self, encrypted_account_id, match_history):
        self.insert_if_not_exists({'accountId': encrypted_account_id, 'matchHistory': match_history},
                                  self.raw_match_history, 'accountId')

    @Logger.Logger()
    def insert_match_details(self, match_detail_as_json):
        self.insert_if_not_exists(match_detail_as_json,
                                  self.raw_match_details, 'gameId')

    @Logger.Logger()
    def get_match_details(self, game_id):
        return self.raw_match_details.find_one({'_id': game_id})

    @Logger.Logger()
    def get_uncrawled_game(self, queue_id):
        return self.raw_match_details.find_one({'queueId': queue_id, 'used_for_crawling': {'$exists': False}})

    @Logger.Logger()
    def mark_match_as_crawled(self, game_id):
        self.raw_match_details.update_one(
            {'_id': game_id}, {'$set': {'used_for_crawling': 1}})

    @Logger.Logger()
    def insert_if_not_exists(self, obj, collection, _key):
        try:
            obj['_id'] = obj[_key]
            collection.insert_one(obj)
        except pm.errors.DuplicateKeyError:
            pass
        except:
            print(sys.exc_info()[0])
