import urllib.request
import sys
import json

sys.path.append("./classes")

from classes.game import Game
from tools.utils import *



partits = {}
partits["lima_V"] = "https://www.basquetcatala.cat/estadistiques/2021/613ca346a4d427060f7943cc"
partits["granollers_L"] = "https://www.basquetcatala.cat/estadistiques/2021/6145db96a4d4270610364080"
partits["cornella_L"] = "https://www.basquetcatala.cat/estadistiques/2021/614f43d7a4d4270613252d6d"
partits["tgn_V"] = "https://www.basquetcatala.cat/estadistiques/2021/6158af70a4d427060de72f55"

json_stats_header_url = "https://msstats.optimalwayconsulting.com/v1/fcbq/getJsonWithMatchStats/"
json_play_by_play_header_url = "https://msstats.optimalwayconsulting.com/v1/fcbq/getJsonWithMatchMoves/"




jornada = "tgn_V"
game_id = partits[jornada].split("/")[-1]

contents = urllib.request.urlopen(json_stats_header_url + game_id).read()
json_game = json.loads(contents)

contents = urllib.request.urlopen(json_play_by_play_header_url + game_id).read()
json_play_by_play = json.loads(contents)

game = Game(jornada)
game.fill_game(json_game, json_play_by_play)

# print(game.get_a_team_five(minute))
# print(game.get_b_team_five(minute))
#
# print(game.teams[game.team_a].get_effective_field_goal())
# print(game.teams[game.team_b].get_effective_field_goal())
# print(game.teams[game.team_a].get_true_shoot())
# print(game.teams[game.team_b].get_true_shoot())
# print(game.teams[game.team_a].get_possessions())
# print(game.teams[game.team_b].get_possessions())

fives_by_minute, fives_list = get_used_five_penya(game)

str_out = ""
for five in fives_list:
    for player in five.players:
        str_out += player + ","
    str_out += str(five.total_minutes) + ","
    str_out += str(five.points_scored) + ","
    str_out += str(five.points_received) + "\n"
print(str_out)

print("###############################")
print("###############################")
print("###############################")


five_by_minute_str = get_fives_by_minute_penya(game)
print(five_by_minute_str)
line_scored = "Punts anotats,"
line_received = "Punts rebuts,"
for minute, five in fives_by_minute.items():
    line_scored += str(five.points_scored) +","
    line_received += str(five.points_received) + ","
print(line_scored)
print(line_received)