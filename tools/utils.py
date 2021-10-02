from classes.data import Five
from classes.play_by_play import PlayType


def get_fives_by_minute_penya(game):
    if game.key.split("_")[-1] == "L":
        return get_fives_by_minute(game.teams[game.team_a])
    elif game.key.split("_")[-1] == "V":
        return get_fives_by_minute(game.teams[game.team_b])


def get_fives_by_minute(team):
    out_string = ","
    for minute in range(1, 41):
        out_string += str(minute)
        out_string += ","
    out_string += "\n"

    for player in team.players.values():
        out_string += player.name
        out_string += ","
        for minute in player.get_minutes_played_distribution().values():
            out_string += str(minute)
            out_string += ","
        out_string += "\n"

    return out_string


def get_used_five_penya(game):
    if game.key.split("_")[-1] == "L":
        return get_used_five_team_a(game)
    elif game.key.split("_")[-1] == "V":
        return get_used_five_team_b(game)


def get_used_five_team_a(game, sort="appearance"):  # the other sort option is by number of minutes desc
    return get_used_five_team(game, game.team_a, sort)


def get_used_five_team_b(game, sort="appearance"):  # the other sort option is by number of minutes desc
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

    return points_scored, points_received
