from monitoring import Logger
from riot_api import RiotClient
from db import Mongo

riot_client = RiotClient.RiotClient()
mongo_client = Mongo.Mongo()


encrypted_account_id = '-w9INIopYVNjHShnEGGgdYhREGEW407RXfAG6ltIjfEi_g'
history = riot_client.get_complete_matchlist_for_encrypted_account_id(
    encrypted_account_id)
mongo_client.insert_player(encrypted_account_id)    
mongo_client.insert_match_history(encrypted_account_id, history)


for match in history:
    riot_client.get_match_details_for_game_id(match['gameId'])

print("done")