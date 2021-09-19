import urllib.request
import json
import sys

sys.path.append("../classes/")
sys.path.append("../tools/")
from data import Five
from game import Game
from play_by_play import Play, PlayType

from utils import print_fives_by_minute_in_csv


def get_used_five_team_a(game, sort):  # the other sort option is by number of minutes desc
    return get_used_five_team(game, game.team_a, sort)


def get_used_five_team_b(game, sort):  # the other sort option is by number of minutes desc
    return get_used_five_team(game, game.team_b, sort)


def get_used_five_team(game, team_id, sort="appearance"):  # the other sort option is by number of minutes desc

    fives_by_minute = {}
    for i in range(0, 40):
        fives_by_minute[i] = Five()
    for player in game.teams[team_id].players.values():
        minutes_played_distribution = player.get_minutes_played_distribution()
        for minute in minutes_played_distribution.keys():
            if minutes_played_distribution[minute]:
                fives_by_minute[minute].players.append(player.name)
    for minute in range(0, 40):
        team_a_score, team_b_score = get_buckets_in_minute(game, minute)
        fives_by_minute[minute].points_scored = team_a_score
        fives_by_minute[minute].points_received = team_b_score

    fives_list = []
    for minute, five_players in fives_by_minute.items():
        added = False
        for five in fives_list:
            if len(set(five.players) & set(five_players.players)) == 5:  # same five
                five.total_minutes += 1
                five.points_scored += five_players.points_scored
                five.points_received += five_players.points_received
                added = True

        if not added:
            new_five = Five()
            new_five.total_minutes += 1
            new_five.players = five_players.players
            new_five.points_scored += five_players.points_scored
            new_five.points_received += five_players.points_received
            fives_list.append(new_five)

    # for bucket in scoreboard:
    if sort == "appearance":
        pass
    elif sort == "minutes":
        fives_list.sort(key=lambda x: x.total_minutes, reverse=True)
    elif sort == "points_scored":
        fives_list.sort(key=lambda x: x.points_scored, reverse=True)
    elif sort == "points_received":
        fives_list.sort(key=lambda x: x.points_received, reverse=True)

    return fives_by_minute, fives_list


def get_buckets_in_minute(game, minute):
    team_a_score = 0
    team_b_score = 0

    for play in game.play_by_play[minute + 1]:
        if play.definition == PlayType.FREE_THROW_MADE:
            if game.team_a == play.team_id:
                team_a_score += 1
            elif game.team_b == play.team_id:
                team_b_score += 1
        elif play.definition == PlayType.TWO_MADE:
            if game.team_a == play.team_id:
                team_a_score += 2
            elif game.team_b == play.team_id:
                team_b_score += 2
        elif play.definition == PlayType.THREE_MADE:
            if game.team_a == play.team_id:
                team_a_score += 3
            elif game.team_b == play.team_id:
                team_b_score += 3

    return team_a_score, team_b_score

basquetcatala_game_url = "https://www.basquetcatala.cat/estadistiques/2021/613ca346a4d427060f7943cc"
game_id = basquetcatala_game_url.split("/")[-1]
json_stats_header_url = "https://msstats.optimalwayconsulting.com/v1/fcbq/getJsonWithMatchStats/"
json_play_by_play_header_url = "https://msstats.optimalwayconsulting.com/v1/fcbq/getJsonWithMatchMoves/"

contents = urllib.request.urlopen(json_stats_header_url + game_id).read()
json_game = json.loads(contents)

contents = urllib.request.urlopen(json_play_by_play_header_url + game_id).read()
json_play_by_play = json.loads(contents)

game = Game()
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

fives_by_minute, fives_list = get_used_five_team_a(game, "points_received")

# for five in fives_list:
#     print("========")
#     print(five.players)
#     print("Total minutes: " + str(five.total_minutes))
#     print("Points scored: " + str(five.points_scored))
#     print("Points received: " + str(five.points_received))

# for minute, five in fives_by_minute.items():
#     print(five.players)
#     print(minute)
#     print(five.points_scored)
#     print(five.points_received)

print_fives_by_minute_in_csv(game.teams[game.team_b].players.values())