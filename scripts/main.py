import os
import requests
import pandas as pd
import json
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from player import Player
from utils import save_json, read_json
from dotenv import load_dotenv
from api.api_calls import get_summoner_by_name, get_matches, get_match_by_id

load_dotenv()

# Envs
riot_api = os.environ['RIOT_API']

# Todo: Read Players
input_data = read_json('data/input.json')
tournament_players = []

for item in input_data['players']:
    tournament_players.append(Player(item['name'], item['tagline']))

# Todo: retrieve player info and matches
for i in range(len(tournament_players)):
    tournament_players[i].get_info()
    tournament_players[i].get_matches()
    tournament_players[i].get_matches_info()
    tournament_players[i].save()
    break