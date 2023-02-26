import math
import os
import time
import requests
import pandas as pd
import json
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from score_functions import normalize_dict, expected_win_rate
from player import Player
from utils import save_json, read_json
from dotenv import load_dotenv
from api.api_calls import get_champions_info

load_dotenv()

# Envs
riot_api = os.environ['RIOT_API']
K = 32

# Todo: Read Players
input_data = read_json('data/input.json')
attribute_data = read_json('data/attributes.json')
champion_data = get_champions_info()
tournament_players = []
players = {}


for item in input_data['players']:
    tournament_players.append(Player(item['name'], item['tagline']))

# Todo: Retrieve player info and matches
for i in range(len(tournament_players)):
    tournament_players[i].get_matches()
    tournament_players[i].get_matches_info()
    players[tournament_players[i].info['puuid']] = tournament_players[i]

# Todo: Normalize data
for key, item in attribute_data.items():
    for skey, sitem in item.items():
        attribute_data[key][skey] = normalize_dict(sitem)

champion_data = {key: normalize_dict(item) for key, item in champion_data.items()}


# Todo: Identify all possible games and calculate ratings
for player in tournament_players:
    print(player.matchIds)
    for match in player.matchInfo:
        for puuid in match['metadata']['participants']:
            if puuid not in players.keys():
                account = Player.get_account_by_puuid(puuid)
                new_player = Player(account['gameName'], account['tagLine'])
                players[puuid] = new_player


        win = []
        lose = []
        for info in match['info']['participants']:
            current_player = players[info['puuid']]
            if info['win']:
                win.append(current_player)
            else:
                lose.append(current_player)

        teamA = sum([item.rating for item in win])
        teamB = sum([item.rating for item in lose])

        win_alpha = expected_win_rate(teamA,teamB)
        lose_alpha = expected_win_rate(teamB, teamA)

        print(win_alpha, lose_alpha)
        for info in match['info']['participants']:
            current_player = players[info['puuid']]
            if info['win']:
                current_player.rating += K * (1 - win_alpha) * info['kills']
                current_player.delta += K * (1 - win_alpha) * info['kills']
            else:
                current_player.rating += K * (0 - lose_alpha) * info['kills']

        for key, item in players.items():
            print("Name: {:<20} Rating: {:>10.0f} Delta: {:>10.0f}".format(item.summoner_name, item.rating, item.delta))

        time.sleep(10)
