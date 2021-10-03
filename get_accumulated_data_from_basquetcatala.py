import urllib.request
import json


from classes.game import Game
from tools.utils import *



partits = {}
partits["lima_V"] = "https://www.basquetcatala.cat/estadistiques/2021/613ca346a4d427060f7943cc"
partits["granollers_L"] = "https://www.basquetcatala.cat/estadistiques/2021/6145db96a4d4270610364080"
partits["cornella_L"] = "https://www.basquetcatala.cat/estadistiques/2021/614f43d7a4d4270613252d6d"
partits["tgn_V"] = "https://www.basquetcatala.cat/estadistiques/2021/6158af70a4d427060de72f55"

json_stats_header_url = "https://msstats.optimalwayconsulting.com/v1/fcbq/getJsonWithMatchStats/"
json_play_by_play_header_url = "https://msstats.optimalwayconsulting.com/v1/fcbq/getJsonWithMatchMoves/"

accumulated_fives =  {}

for jornada in partits.keys():

    game_id = partits[jornada].split("/")[-1]

    contents = urllib.request.urlopen(json_stats_header_url + game_id).read()
    json_game = json.loads(contents)

    contents = urllib.request.urlopen(json_play_by_play_header_url + game_id).read()
    json_play_by_play = json.loads(contents)

    game = Game(jornada)
    game.fill_game(json_game, json_play_by_play)

    _, fives_list = get_used_five_penya(game)

    key = ""
    for five in fives_list:
        key = "_".join(five.players)
        if key not in accumulated_fives.keys():
            accumulated_fives[key] = five
        else:
            accumulated_fives[key].total_minutes += five.total_minutes
            accumulated_fives[key].points_scored += five.points_scored
            accumulated_fives[key].points_received += five.points_received


str_out = ""
for five in accumulated_fives.values():
    for player in five.players:
        str_out += player + ","
    str_out += str(five.total_minutes) + ","
    str_out += str(five.points_scored) + ","
    str_out += str(five.points_received) + "\n"
print(str_out)
