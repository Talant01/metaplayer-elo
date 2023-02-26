import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from constants import REGIONS, RATINGS
from utils import save_json, read_json
from dotenv import load_dotenv
from api.api_calls import get_summoner_by_name, get_matches, get_match_by_id, get_tagline

class Player:
    def __init__(self, summoner_name, tagline):
        self.summoner_name = summoner_name
        self.tagline = tagline
        self.delta = 0
        self.matchInfo = []
        self.matchIds = []
        
        for key, item in REGIONS.items():
            if self.tagline in item:
                self.region = key
                break

        self.info = get_summoner_by_name(self.tagline, self.summoner_name)
        
        if self.info['puuid'] in RATINGS:
            self.rating = RATINGS[self.info['puuid']]
        else:
            self.rating = 1300
            RATINGS[self.info['puuid']] = self.rating

    def get_matches(self):
        self.matchIds = get_matches(self.region, self.info['puuid'])

    def get_matches_info(self):
        for id in self.matchIds:
            data = get_match_by_id(self.region, id)
            self.matchInfo.append(data)

    def increase_delta(self, delta):
        self.delta += delta

    @staticmethod
    def get_account_by_puuid(puuid):
        data = get_tagline(puuid);
        data['tagLine'] = 'EUW1'
        return data


    def save(self):
        print(self)
        

