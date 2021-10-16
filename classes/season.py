import urllib.request
import json

from .game import Game


class Season:
    #This should be in a helper class because of responsability separation, but...
    json_stats_header_url = "https://msstats.optimalwayconsulting.com/v1/fcbq/getJsonWithMatchStats/"
    json_play_by_play_header_url = "https://msstats.optimalwayconsulting.com/v1/fcbq/getJsonWithMatchMoves/"

    def __init__(self):
        self.games = {}

    def __load_game_from_url(self, partit_url):
        id_partit = partit_url.split("/")[-1]

        contents = urllib.request.urlopen(self.json_stats_header_url + id_partit).read()
        json_game = json.loads(contents)

        contents = urllib.request.urlopen(self.json_play_by_play_header_url + id_partit).read()
        json_play_by_play = json.loads(contents)

        return json_game, json_play_by_play

    def fill_season(self, partits):
        print("Carregant els partits...")

        for partit_key in partits.keys():

            json_game, json_play_by_play = self.__load_game_from_url(partits[partit_key])

            game = Game(partit_key)
            game.fill_game(json_game, json_play_by_play)
            self.games[partit_key] = game