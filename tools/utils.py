from classes.data import Five
from classes.play_by_play import PlayType


def get_fives_by_minute(game, minutes_distribution):
    if game.key.split("_")[-1] == "L":
        return get_fives_by_minute_object_by_team(game.teams[game.team_a], minutes_distribution, game.total_minutes)
    elif game.key.split("_")[-1] == "V":
        return get_fives_by_minute_object_by_team(game.teams[game.team_b], minutes_distribution, game.total_minutes)


def get_fives_by_minute_object_by_team(team, minutes_distribution, game_total_minutes):
    for player in team.players.values():
        if player.name not in minutes_distribution.keys():
            minutes_distribution[player.name] = []
            for minute in range(0, game_total_minutes):
                minutes_distribution[player.name].append(0)
        for minute, in_game in player.get_minutes_played_distribution(game_total_minutes).items():
            minutes_distribution[player.name][minute] += in_game

    return minutes_distribution


def get_used_five(game):
    if game.key.split("_")[-1] == "L":
        return get_used_five_team_a(game)
    elif game.key.split("_")[-1] == "V":
        return get_used_five_team_b(game)


def get_used_five_team_a(game, sort="appearance"):  # the other sort option is by number of minutes desc
    return get_used_five_team(game, game.team_a, game.total_minutes, sort)


def get_used_five_team_b(game, sort="appearance"):  # the other sort option is by number of minutes desc
    return get_used_five_team(game, game.team_b, game.total_minutes, sort)


def get_used_five_team(game, team_id, game_total_minutes, sort="appearance"):  # the other sort option is by number of minutes desc

    fives_by_minute = {}
    for i in range(0, game_total_minutes):
        fives_by_minute[i] = Five()
    for player in game.teams[team_id].players.values():
        minutes_played_distribution = player.get_minutes_played_distribution(game_total_minutes)
        for minute in minutes_played_distribution.keys():
            if minutes_played_distribution[minute]:
                fives_by_minute[minute].players.append(player.name)
    for minute in range(0, game_total_minutes):
        points_scored, points_received = get_buckets_in_minute(game, team_id, minute)
        fives_by_minute[minute].points_scored = points_scored
        fives_by_minute[minute].points_received = points_received

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


def get_buckets_in_minute(game, team_id, minute):
    points_scored = 0
    points_received = 0

    if minute + 1 in game.play_by_play.keys():
        for play in game.play_by_play[minute + 1]:
            if play.definition == PlayType.FREE_THROW_MADE:
                if team_id == play.team_id:
                    points_scored += 1
                else:
                    points_received += 1
            elif play.definition == PlayType.TWO_MADE:
                if team_id == play.team_id:
                    points_scored += 2
                else:
                    points_received += 2
            elif play.definition == PlayType.THREE_MADE:
                if team_id == play.team_id:
                    points_scored += 3
                else:
                    points_received += 3
    else:
        pass

    return points_scored, points_received


def get_player_usage(game, players_usage):
    if game.key.split("_")[-1] == "L":
        return get_player_usage_by_team(game.teams[game.team_a], players_usage)
    elif game.key.split("_")[-1] == "V":
        return get_player_usage_by_team(game.teams[game.team_b], players_usage)


def get_player_usage_by_team(team, players_usage):
    for player in team.players.values():
        if player.name not in players_usage.keys():
            players_usage[player.name] = {"two_made": 0, "three_made": 0, "free_throw_made": 0,
                                          "two_attempted": 0, "three_attempted": 0, "free_throw_attempted": 0,
                                          "minutes": 0}
        players_usage[player.name]["two_made"] += player.stats.get_two_made()
        players_usage[player.name]["three_made"] += player.stats.get_three_made()
        players_usage[player.name]["free_throw_made"] += player.stats.get_free_throw_made()
        players_usage[player.name]["two_attempted"] += player.stats.get_two_attempted()
        players_usage[player.name]["three_attempted"] += player.stats.get_three_attempted()
        players_usage[player.name]["free_throw_attempted"] += player.stats.get_free_throw_attempted()
        players_usage[player.name]["minutes"] += player.stats.get_minutes()
    return players_usage


def initialize_all_players(games_to_display):
    all_players = []
    for game in games_to_display:
        if game.key.split("_")[-1] == "L":
            team = game.teams[game.team_a]
        elif game.key.split("_")[-1] == "V":
            team = game.teams[game.team_b]
        for player in team.players.values():
            if player.name not in all_players:
                all_players.append((player.name, player.player_id))
    return all_players

def get_player_usage_evolution(game, all_players, players_usage):
    if game.key.split("_")[-1] == "L":
        return get_player_usage_evolution_by_team(game.teams[game.team_a], all_players, players_usage, game.key)
    elif game.key.split("_")[-1] == "V":
        return get_player_usage_evolution_by_team(game.teams[game.team_b], all_players, players_usage, game.key)


def get_player_usage_evolution_by_team(team, all_players, players_evolution, game_key):
    # for player in team.players.values():
    for (player_name, player_id) in all_players:
        if player_name not in players_evolution.keys():
            players_evolution[player_name] = {}
        players_evolution[player_name][game_key] = {"two_made": 0, "three_made": 0, "free_throw_made": 0,
                                          "two_attempted": 0, "three_attempted": 0, "free_throw_attempted": 0,
                                          "minutes": 0}
        for player in team.players.values():
            if player_name == player.name:
                players_evolution[player_name][game_key]["two_made"] += player.stats.get_two_made()
                players_evolution[player_name][game_key]["three_made"] += player.stats.get_three_made()
                players_evolution[player_name][game_key]["free_throw_made"] += player.stats.get_free_throw_made()
                players_evolution[player_name][game_key]["two_attempted"] += player.stats.get_two_attempted()
                players_evolution[player_name][game_key]["three_attempted"] += player.stats.get_three_attempted()
                players_evolution[player_name][game_key]["free_throw_attempted"] += player.stats.get_free_throw_attempted()
                players_evolution[player_name][game_key]["minutes"] += player.stats.get_minutes()
    return players_evolution


def get_possessions_by_team(team):
    return team.get_possessions()


def get_possessions_by_match(game):
    possessions_team_to_study = 0
    possessions_opponent = 0
    if game.key.split("_")[-1] == "L":
        possessions_team_to_study = get_possessions_by_team(game.teams[game.team_a])
        possessions_opponent = get_possessions_by_team(game.teams[game.team_b])
    elif game.key.split("_")[-1] == "V":
        possessions_team_to_study = get_possessions_by_team(game.teams[game.team_b])
        possessions_opponent = get_possessions_by_team(game.teams[game.team_a])

    return possessions_team_to_study, possessions_opponent