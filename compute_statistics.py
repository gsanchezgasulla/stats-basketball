
from llista_partits import Partits
from classes.season import Season
from tools.utils import *


class ComputeStatistics():
    partits = Partits().llista_partits
    season = None

    def __init__(self):
        self.season = Season()
        self.season.fill_season(self.partits)

    def __get_games_to_display(self, game_key):
        if game_key == "all":  # we want all games
            return self.season.games.values()
        else:
            return [self.season.games[game_key]]

    def get_scores_by_fives(self, game_key):

        games_to_display = self.__get_games_to_display(game_key)
        accumulated_fives = {}

        for game in games_to_display:
            _, fives_list = get_used_five(game)

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

        return str_out

    def get_minutes_distribution_in_game(self, game_key):
        games_to_display = self.__get_games_to_display(game_key)
        minutes_distribution = {}
        minutes_score = {}
        out_str = ","
        for minute in range(0, 40):
            out_str += str(minute)
            out_str += ","
            minutes_score[minute] = {"points_scored": 0, "points_received": 0}
        out_str += "\n"

        for game in games_to_display:
            minutes_distribution = get_fives_by_minute(game, minutes_distribution)
            fives_by_minute, _ = get_used_five(game)

            for minute, five in fives_by_minute.items():
                minutes_score[minute]["points_scored"] += five.points_scored
                minutes_score[minute]["points_received"] += five.points_received

        for player in minutes_distribution.keys():
            out_str += player + ","
            for minute in range(0, 40):
                out_str += str(minutes_distribution[player][minute]) + ","
            out_str += "\n"

        out_str += "Punts anotats," + ",".join(
            [str(minutes_score[minute]["points_scored"]) for minute in range(0, 40)]) + "\n"
        out_str += "Punts rebuts," + ",".join(
            [str(minutes_score[minute]["points_received"]) for minute in range(0, 40)]) + "\n"

        return out_str

    def get_player_usage(self, game_key):
        games_to_display = self.__get_games_to_display(game_key)
        players = {}
        for game in games_to_display:
            players = get_player_usage(game, players)

        out_str = "Jugadora, %T2, %T3, %TLL, %Us2, %Us3, %UsLL, %UsEquip, %UsMinute\n"
        team_usage = {"two_made": 0, "three_made": 0, "free_throw_made": 0,
                      "two_attempted": 0, "three_attempted": 0, "free_throw_attempted": 0,
                      "minutes": 0}
        for player in players.values():
            for stat in player.keys():
                team_usage[stat] += player[stat]

        for player, stats in players.items():
            out_str += player + ","
            out_str += "%.2f," % (stats["two_made"]/float(stats["two_attempted"])*100 if stats["two_attempted"] != 0 else 0)
            out_str += "%.2f," % (stats["three_made"]/float(stats["three_attempted"])*100  if stats["three_attempted"] != 0 else 0)
            out_str += "%.2f," % (stats["free_throw_made"]/float(stats["free_throw_attempted"])*100 if stats["free_throw_attempted"] != 0 else 0)
            total_attempted = float(stats["two_attempted"] + stats["three_attempted"] + 0.44*stats["free_throw_attempted"])
            out_str += "%.2f," % (stats["two_attempted"]/total_attempted*100 if total_attempted != 0 else 0)
            out_str += "%.2f," % (stats["three_attempted"]/total_attempted*100 if total_attempted != 0 else 0)
            out_str += "%.2f," % (stats["free_throw_attempted"]*0.44/total_attempted*100 if total_attempted != 0 else 0)
            player_usage = ((stats["two_attempted"] + stats["three_attempted"] + stats["free_throw_attempted"]) / float(team_usage["two_attempted"] + team_usage["three_attempted"] + team_usage["free_throw_attempted"])*100)
            out_str += "%.2f," % player_usage
            out_str += "%.2f" % ((player_usage * team_usage["minutes"])/float(5*stats["minutes"]) if stats["minutes"] != 0 else 0)
            out_str += "\n"

        return out_str

    def get_player_usage_evolution(self, game_key):
        games_to_display = self.__get_games_to_display(game_key)

        out_str = "%T2 \n"
        players_evolution = {}
        for game in games_to_display:
            out_str += game.key + ","
            players_evolution = get_player_usage_evolution(game, players_evolution)
        out_str += "\n"
        for player_name in players_evolution.keys():
            out_str += player_name + ","
            for game_key, stats in players_evolution[player_name].items():
                out_str += "%.2f," % (stats["two_made"]/float(stats["two_attempted"])*100 if stats["two_attempted"] != 0 else 0)
            out_str += "\n"

        out_str += "\n%T3 \n"
        players_evolution = {}
        for game in games_to_display:
            out_str += game.key + ","
            players_evolution = get_player_usage_evolution(game, players_evolution)
        out_str += "\n"
        for player_name in players_evolution.keys():
            out_str += player_name + ","
            for game_key, stats in players_evolution[player_name].items():
                out_str += "%.2f," % (
                    stats["three_made"] / float(stats["three_attempted"]) * 100 if stats["three_attempted"] != 0 else 0)
            out_str += "\n"

        out_str += "\n%TLL \n"
        players_evolution = {}
        for game in games_to_display:
            out_str += game.key + ","
            players_evolution = get_player_usage_evolution(game, players_evolution)
        out_str += "\n"
        for player_name in players_evolution.keys():
            out_str += player_name + ","
            for game_key, stats in players_evolution[player_name].items():
                out_str += "%.2f," % (
                    stats["free_throw_made"] / float(stats["free_throw_attempted"]) * 100 if stats["free_throw_attempted"] != 0 else 0)
            out_str += "\n"

        out_str += "\n% Us2 \n"
        players_evolution = {}
        for game in games_to_display:
            out_str += game.key + ","
            players_evolution = get_player_usage_evolution(game, players_evolution)
        out_str += "\n"
        for player_name in players_evolution.keys():
            out_str += player_name + ","
            for game_key, stats in players_evolution[player_name].items():
                total_attempted = float(
                    stats["two_attempted"] + stats["three_attempted"] + 0.44 * stats["free_throw_attempted"])
                out_str += "%.2f," % (stats["two_attempted"]/total_attempted*100 if total_attempted != 0 else 0)
            out_str += "\n"

        out_str += "\n% Us3 \n"
        players_evolution = {}
        for game in games_to_display:
            out_str += game.key + ","
            players_evolution = get_player_usage_evolution(game, players_evolution)
        out_str += "\n"
        for player_name in players_evolution.keys():
            out_str += player_name + ","
            for game_key, stats in players_evolution[player_name].items():
                total_attempted = float(
                    stats["two_attempted"] + stats["three_attempted"] + 0.44 * stats["free_throw_attempted"])
                out_str += "%.2f," % (stats["three_attempted"]/total_attempted*100 if total_attempted != 0 else 0)
            out_str += "\n"


        out_str += "\n% UsLL \n"
        players_evolution = {}
        for game in games_to_display:
            out_str += game.key + ","
            players_evolution = get_player_usage_evolution(game, players_evolution)
        out_str += "\n"
        for player_name in players_evolution.keys():
            out_str += player_name + ","
            for game_key, stats in players_evolution[player_name].items():
                total_attempted = float(
                    stats["two_attempted"] + stats["three_attempted"] + 0.44 * stats["free_throw_attempted"])
                out_str += "%.2f," % (0.44 * stats["free_throw_attempted"]/total_attempted*100 if total_attempted != 0 else 0)
            out_str += "\n"

        out_str += "\n% UsEquip per minut \n,"
        team_usage_global = {}
        players_all = {}

        for game in games_to_display:
            out_str += game.key + ","
            players = get_player_usage(game, {})
            players_all = {**players_all, **players}
            team_usage = {"two_made": 0, "three_made": 0, "free_throw_made": 0,
                      "two_attempted": 0, "three_attempted": 0, "free_throw_attempted": 0,
                      "minutes": 0}
            for player in players.values():
                for stat in player.keys():
                    team_usage[stat] += player[stat]
            team_usage_global[game.key] = team_usage
        out_str += "\n"

        for player in players_all:
            out_str += player + ","
            for game in games_to_display:
                players = get_player_usage(game, {})

                if player in players.keys():
                    stats = players[player]
                    player_usage = (
                            (stats["two_attempted"] + stats["three_attempted"] + stats["free_throw_attempted"]) /
                            float(team_usage_global[game.key]["two_attempted"] +
                                  team_usage_global[game.key]["three_attempted"] +
                                  team_usage_global[game.key]["free_throw_attempted"]) * 100)
                    # out_str += "%.2f," % player_usage
                    out_str += "%.2f," % ((player_usage * team_usage_global[game.key]["minutes"]) /
                                         float(5 * stats["minutes"]) if stats["minutes"] != 0 else 0)
                else:
                    out_str += "0.0,"
            out_str += "\n"



        # for game in games_to_display:
        #     players = get_player_usage(game, {})
        #     for player, stats in players.items():
        #         out_str += player + ","
        #         player_usage = (
        #                     (stats["two_attempted"] + stats["three_attempted"] + stats["free_throw_attempted"]) /
        #                     float(team_usage_global[game.key]["two_attempted"] +
        #                           team_usage_global[game.key]["three_attempted"] +
        #                           team_usage_global[game.key]["free_throw_attempted"]) * 100)
        #         out_str += "%.2f," % player_usage
        #         out_str += "%.2f" % ((player_usage * team_usage_global[game.key]["minutes"]) / float(5 * stats["minutes"]) if
        #                              stats["minutes"] != 0 else 0)

        return out_str




