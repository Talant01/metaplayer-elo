import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Envs
api_key = os.environ['RIOT_API']

def get_summoner_by_name(region, summoner_name):
    """
    Retrieves summoner information by summoner name.

    Parameters:
    region (str): The region code of the server to query.
    api_key (str): The Riot API key.
    summoner_name (str): The summoner name to search for.

    Returns:
    dict: The summoner information as a dictionary.
    """
    while True:
        url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
        headers = {"X-Riot-Token": api_key}
        response = requests.get(url, headers=headers)

        if response.status_code == 503:
            time.sleep(5)
            continue

        return response.json()


def get_matches(region, account_puuid, begin_index=0,count=5):
    """
    Retrieves a list of recent matches for a given account ID.

    Parameters:
    region (str): The region code of the server to query.
    api_key (str): The Riot API key.
    account_puuid (str): The account puuid to retrieve match history for.
    begin_index (int): Optional. The index of the first match to retrieve. Defaults to 0.
    end_index (int): Optional. The index of the last match to retrieve. Defaults to 100.

    Returns:
    list: A list of recent matches as dictionaries.
    """
    while True:
        url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{account_puuid}/ids'
        params = {"start": begin_index, "count": count}
        headers = {"X-Riot-Token": api_key}
        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 503:
            time.sleep(5)
            continue

        return response.json()


def get_match_by_id(region, match_id):
    """
    Retrieves detailed information about a single match by match ID.

    Parameters:
    region (str): The region code of the server to query.
    api_key (str): The Riot API key.
    match_id (int): The ID of the match to retrieve.

    Returns:
    dict: The match information as a dictionary.
    """
    while True:
        url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}'
        headers = {"X-Riot-Token": api_key}
        response = requests.get(url, headers=headers)

        if response.status_code == 503:
            time.sleep(5)
            continue

        return response.json()


def get_tagline(puuid):
    """
    Retrieves detailed information about a single match by match ID.

    Parameters:
    region (str): The region code of the server to query.
    api_key (str): The Riot API key.
    match_id (int): The ID of the match to retrieve.

    Returns:
    dict: The match information as a dictionary.
    """
    while True:
        url = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}'
        headers = {"X-Riot-Token": api_key}
        response = requests.get(url, headers=headers)

        if response.status_code == 503:
            time.sleep(5)
            continue

        return response.json()
    
def get_champions_info():
    url = 'http://ddragon.leagueoflegends.com/cdn/13.4.1/data/en_US/champion.json'
    response = requests.get(url)
    data = response.json()

    champions = {}

    for key, item in data['data'].items():
        champions[key] = item['info']

    return champions

