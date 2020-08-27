from monitoring import Logger
from riot_api import RiotClient

riot_client = RiotClient.RiotClient()
seed = riot_client.get_complete_matchlist_for_encrypted_account_id(
    '-w9INIopYVNjHShnEGGgdYhREGEW407RXfAG6ltIjfEi_g')