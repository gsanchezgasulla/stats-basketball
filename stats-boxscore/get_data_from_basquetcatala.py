import urllib.request
import json
import sys

sys.path.append("../classes/")
from player import Player, PlayerStats
from data import Game
from team import Team

basquetcatala_game_url = "https://www.basquetcatala.cat/estadistiques/2020/607c6b25a4d42705fe62bbd8"
game_id = basquetcatala_game_url.split("/")[-1]
json_stats_header_url = "https://msstats.optimalwayconsulting.com/v1/fcbq/getJsonWithMatchStats/"

contents = urllib.request.urlopen(json_stats_header_url + game_id).read()
json_game = json.loads(contents)

game = Game()
game.date = json_game["time"]
print(game)
team_a = Team()
team_a.name = json_game["teams"][0]["name"]
for player_json in json_game["teams"][0]["players"]:
    player = Player()
    player.name = player_json["name"]
    player.number = int(player_json["dorsal"])
    team_a.players.append(player)

team_b = Team()
team_b.name = json_game["teams"][1]["name"]
for player_json in json_game["teams"][1]["players"]:
    player = Player()
    player.name = player_json["name"]
    player.number = int(player_json["dorsal"])
    team_a.players.append(player)
