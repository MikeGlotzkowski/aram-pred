from monitoring import Logger
from riot_api import PlayerCrawler
from db import Mongo

encrypted_account_id = '-w9INIopYVNjHShnEGGgdYhREGEW407RXfAG6ltIjfEi_g'
crawler = PlayerCrawler.PlayerCrawler(encrypted_account_id)
crawler.run()