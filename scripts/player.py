import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from constants import REGIONS
from utils import save_json, read_json
from dotenv import load_dotenv
from api.api_calls import get_summoner_by_name, get_matches, get_match_by_id

class Player:
    def __init__(self, summoner_name, tagline):
        self.summoner_name = summoner_name
        self.tagline = tagline
        
        for key, item in REGIONS.items():
            if self.tagline in item:
                self.region = key
                break

    def get_info(self):
        self.info = get_summoner_by_name(self.tagline, self.summoner_name)

    def get_matches(self):
        print(self.info)
        print(self.region)
        print(self.tagline)
        print(self.summoner_name)
        self.matchIds = get_matches(self.region, self.info['puuid'])

    def get_matches_info(self):
        self.matchInfo = []

        for id in self.matchIds:
            data = get_match_by_id(self.region, id)
            self.matchInfo.append(data)

    def save(self):
        print(self)
        

