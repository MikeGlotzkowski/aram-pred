import requests
import os

api_key = os.environ.get("RIOT_API_KEY")

def get_matchlist_for_encryptedAccountId(encrypted_account_id):
    try:
        url = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/{0}?queue=450&api_key={1}".format(encrypted_account_id, api_key)
        r = requests.get(url)
        r.raise_for_status()    
        return {
            "encrypted_account_id" : encrypted_account_id,
            "history": r.json()
        }
    except requests.exceptions.HTTPError as err:
        print(err)