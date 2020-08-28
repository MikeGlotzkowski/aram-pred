import requests
import os
from monitoring import Logger
import time


class RiotClient:

    def __init__(self, logger):
        self.logger = logger
        self.api_key = os.environ.get("RIOT_API_KEY")
        self.base_url = "https://euw1.api.riotgames.com/lol/match/v4"
        self.waiting_intervall_if_throttled_in_seconds = 5

    @Logger.Logger()
    def get_matchlist_for_encrypted_account_id(self, encrypted_account_id, begin_index, end_index):
        try:
            url = f"{self.base_url}/matchlists/by-account/{encrypted_account_id}?queue=450&api_key={self.api_key}&beginIndex={begin_index}&endIndex={end_index}"
            r = requests.get(url)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError as err:
            self.logger.log('error', str(err))
            if r.status_code == 429:
                retry_after = r.headers['Retry-After']
                self.wait(int(retry_after))
                return self.get_matchlist_for_encrypted_account_id(encrypted_account_id, begin_index, end_index)

    @Logger.Logger()
    def get_match_details_for_game_id(self, game_id):
        try:
            url = f"{self.base_url}/matches/{game_id}?api_key={self.api_key}"
            r = requests.get(url)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError as err:
            self.logger.log('error', str(err))
            if r.status_code == 429:
                retry_after = r.headers['Retry-After']
                self.wait(int(retry_after))
                return self.get_match_details_for_game_id(game_id)

    @Logger.Logger()
    def get_complete_matchlist_for_encrypted_account_id(self, encrypted_account_id):
        matches = []
        begin_index = 0
        tranche = 99
        end_index = begin_index + tranche
        first = self.get_matchlist_for_encrypted_account_id(
            encrypted_account_id, begin_index, end_index)
        self.logger.log(
            'info', f'begin_index {begin_index} end_index {end_index}')
        total_games = first['totalGames']
        for i in range(end_index + 1, total_games, tranche):
            self.logger.log('info', f'begin_index {i} end_index {i + tranche}')
            r = self.get_matchlist_for_encrypted_account_id(
                encrypted_account_id, i, i + tranche)
            matches.extend(r['matches'])
        return matches

    @Logger.Logger()
    def wait(self, retry_after):
        interval = self.waiting_intervall_if_throttled_in_seconds
        time_waited = 0
        while time_waited < retry_after:
            time.sleep(interval)
            time_waited += interval
            self.logger.log(
                'info', f'THROTTLED! Waited {time_waited} of {retry_after} seconds.')
        return True
