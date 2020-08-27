import requests
import os
from monitoring import Logger


class RiotClient:

    def __init__(self):
        self.api_key = os.environ.get("RIOT_API_KEY")
        self.base_url = "https://euw1.api.riotgames.com/lol/match/v4"

    # @Logger.Logger()
    def get_matchlist_for_encrypted_account_id(self, encrypted_account_id, begin_index, end_index):
        try:
            url = f"{self.base_url}/matchlists/by-account/{encrypted_account_id}?queue=450&api_key={self.api_key}&beginIndex={begin_index}&endIndex={end_index}"
            r = requests.get(url)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError as err:
            print(err)

    @Logger.Logger()
    def get_match_details_for_game_id(self, game_id):
        try:
            url = f"{self.base_url}/matches/{game_id}?api_key={self.api_key}"
            r = requests.get(url)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError as err:
            print(err)

    # @Logger.Logger()
    def get_complete_matchlist_for_encrypted_account_id(self, encrypted_account_id):
        matches = []
        begin_index = 0
        tranche = 99
        end_index = begin_index + tranche
        first = self.get_matchlist_for_encrypted_account_id(
            encrypted_account_id, begin_index, end_index)
        print(f'begin_index {begin_index} end_index {end_index}')
        total_games = first['totalGames']
        for i in range(end_index + 1, total_games, tranche):
            print(f'begin_index {i} end_index {i + tranche}')
            r = self.get_matchlist_for_encrypted_account_id(
                encrypted_account_id, i, i + tranche)
            matches.extend(r['matches'])
        return matches
