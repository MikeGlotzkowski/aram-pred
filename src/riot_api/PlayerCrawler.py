from db import Mongo
from riot_api import RiotClient
from monitoring import Logger


class PlayerCrawler:

    def __init__(self, encrypted_account_id):
        self.logger = Logger.Logger()
        self.persistency = Mongo.Mongo(self.logger)
        self.api = RiotClient.RiotClient(self.logger)
        self.encrypted_account_id = encrypted_account_id

    def run(self):
        self.logger.log(
            'info', f'Fetching all games for encrypted_account_id {self.encrypted_account_id}.')
        history = self.api.get_complete_matchlist_for_encrypted_account_id(
            self.encrypted_account_id)
        self.persistency.insert_match_history(
            self.encrypted_account_id, history)
        for match in history:
            game_id = match['gameId']
            match_persistet = self.persistency.get_match_details(game_id)
            if match_persistet:
                self.logger.log(
                    'info', f'Game with id {game_id} already in db.')
                pass
            else:
                match_data = self.api.get_match_details_for_game_id(game_id)
                self.persistency.insert_match_details(match_data)
        self.logger.log(
            'info', f'Fetched all games for encrypted_account_id {self.encrypted_account_id}.')
