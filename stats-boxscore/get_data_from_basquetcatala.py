import urllib.request
import json
import sys

sys.path.append("../classes/")
from player import Player, PlayerStats
from data import Game
from team import Team
from play import Play, PlayType


def fill_play_by_play(json_in_out):
    play_list = []
    for in_out in json_in_out:
        play = Play()
        if "IN_TYPE" == in_out["type"]:
            play.definition = PlayType.SUBSTITUTION_IN
        elif "OUT_TYPE" == in_out["type"]:
            play.definition = PlayType.SUBSTITUTION_OUT
        play.minute = int(in_out["minuteAbsolut"])
        play_list.append(play)
    play_list.sort(key=lambda x: x.minute)
    return play_list


def fill_stats(json_stats):
    player_stats = PlayerStats()
    player_stats.minutes = json_stats
    player_stats.defensive_rebounds = int(json_stats["defensiveRebound"])
    player_stats.offensive_rebounds = int(json_stats["offensiveRebound"])
    player_stats.assists = int(json_stats["assists"])
    player_stats.steals = int(json_stats["steals"])
    player_stats.turnovers = int(json_stats["lost"])
    player_stats.blocked_shots = int(json_stats["block"])
    player_stats.blocks_received = int(json_stats["blockReceived"])
    player_stats.fouls_made = int(json_stats["faults"])
    player_stats.fouls_received = int(json_stats["faultReceived"])

    player_stats.two_attempted = int(json_stats["shotsOfTwoAttempted"])
    player_stats.two_made = int(json_stats["shotsOfTwoSuccessful"])
    player_stats.three_attempted = int(json_stats["shotsOfThreeAttempted"])
    player_stats.three_made = int(json_stats["shotsOfThreeSuccessful"])
    player_stats.free_throw_attempted = int(json_stats["shotsOfOneAttempted"])
    player_stats.free_throw_made = int(json_stats["shotsOfOneSuccessful"])
    return player_stats


def fill_team(json_game_team):
    team = Team()
    team.name = json_game_team["name"]
    for player_json in json_game_team["players"]:
        player = Player()
        player.name = player_json["name"]
        player.number = int(player_json["dorsal"])

        player.play_by_play = fill_play_by_play(player_json["inOutsList"])
        player.stats = fill_stats(player_json["data"])
        team.players.append(player)
    return team

basquetcatala_game_url = "https://www.basquetcatala.cat/estadistiques/2020/607c6b25a4d42705fe62bbd8"
game_id = basquetcatala_game_url.split("/")[-1]
json_stats_header_url = "https://msstats.optimalwayconsulting.com/v1/fcbq/getJsonWithMatchStats/"

contents = urllib.request.urlopen(json_stats_header_url + game_id).read()
json_game = json.loads(contents)

game = Game()
game.date = json_game["time"]

game.team_a = fill_team(json_game["teams"][0])
game.team_b = fill_team(json_game["teams"][1])

minute = 1
print(game.get_a_team_five(minute))
print(game.get_b_team_five(minute))

print(game.team_a.get_effective_field_goal())
print(game.team_b.get_effective_field_goal())
print(game.team_a.get_true_shoot())
print(game.team_b.get_true_shoot())