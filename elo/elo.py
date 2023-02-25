import os
import requests
import pandas as pd
import json

from dotenv import load_dotenv

load_dotenv()

# Envs
riot_api = os.environ['RIOT_API']

def save_json(data):
    with open('data.json', 'w') as fp:
        json.dump(data, fp)


def get_player(region, name):
    api_url = f'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={riot_api}'

    response = requests.get(api_url)
    data = response.json()

    return data


def get_matches(region, puuid, count = 20):
    api_url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}&api_key={riot_api}'

    response = requests.get(api_url)
    data = response.json()

    return data

def get_match_by_id(region, matchId):
    api_url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/{matchId}?api_key={riot_api}'

    response = requests.get(api_url)
    data = response.json()

    return data


# Constants
name = 'Noah7'
region_short = 'euw1'
region = 'europe'

player = {}

player['info'] = get_player(region_short, name)
player['matchId'] = get_matches(region, player['info']['puuid'], 2)
player['matchInfo'] = []

for id in player['matchId']:
    player['matchInfo'].append(get_match_by_id(region, id))

for participant in player['matchInfo'][0]['info']['participants']:
    print(participant['win'])


save_json(player)