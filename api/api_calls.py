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
    url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}'
    headers = {"X-Riot-Token": api_key}
    response = requests.get(url, headers=headers)
    return response.json()


def get_matches(region, account_puuid, begin_index=0,):
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
    url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{account_puuid}/ids'
    params = {"start": begin_index}
    headers = {"X-Riot-Token": api_key}
    response = requests.get(url, params=params, headers=headers)
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
    url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}'
    headers = {"X-Riot-Token": api_key}
    response = requests.get(url, headers=headers)
    return response.json()
