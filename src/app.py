from monitoring import Logger
from riot_api import PlayerCrawler
from db import Mongo

# ARAM
queue_id = 450
logger = Logger.Logger()
persistency = Mongo.Mongo(logger)

# seed for crawling
seed_encrypted_account_id = '-w9INIopYVNjHShnEGGgdYhREGEW407RXfAG6ltIjfEi_g'
PlayerCrawler.PlayerCrawler(seed_encrypted_account_id).run()


while True:
    match = persistency.get_uncrawled_game(queue_id)
    for participant_identity in match['participantIdentities']:
        encrypted_account_id = participant_identity['player']['currentAccountId']
        if encrypted_account_id == seed_encrypted_account_id:
            pass
        else:
            PlayerCrawler.PlayerCrawler(encrypted_account_id).run()
    persistency.mark_match_as_crawled(match['gameId'])