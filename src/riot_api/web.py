import requests
import os

api_key = os.environ.get("RIOT_API_KEY")


def get_matchlist_for_encrypted_account_id(encrypted_account_id):
    try:
        url = f"https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/{encrypted_account_id}?queue=450&api_key={api_key}"
        r = requests.get(url)
        r.raise_for_status()
        return {
            "encrypted_account_id": encrypted_account_id,
            "history": r.json()
        }
    except requests.exceptions.HTTPError as err:
        print(err)


def get_match_details_for_game_id(game_id):
    try:
        url = f"https://euw1.api.riotgames.com/lol/match/v4/matches/{game_id}?api_key={api_key}"
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as err:
        print(err)


