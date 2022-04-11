import urllib.request
import json
from urllib.error import URLError

class GameLoader:
    #This should be in a helper class because of responsability separation, but...
    json_stats_header_url = "https://msstats.optimalwayconsulting.com/v1/fcbq/getJsonWithMatchStats/"
    json_play_by_play_header_url = "https://msstats.optimalwayconsulting.com/v1/fcbq/getJsonWithMatchMoves/"

    def load_game_from_url(self, partit_url):
        id_partit = partit_url.split("/")[-1]
        try:

            contents = urllib.request.urlopen(self.json_stats_header_url + id_partit).read()
            json_game = json.loads(contents)

            contents = urllib.request.urlopen(self.json_play_by_play_header_url + id_partit).read()
            json_play_by_play = json.loads(contents)
        except URLError as ex:
            raise Exception(ex)

        return json_game, json_play_by_play