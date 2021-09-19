

def print_fives_by_minute_in_csv(players):
    out_string = ","
    for minute in range(1,41):
        out_string += str(minute)
        out_string += ","
    out_string += "\n"

    for player in players:
        out_string += player.name
        out_string += ","
        for minute in player.get_minutes_played_distribution().values():
            out_string += str(minute)
            out_string += ","
        out_string += "\n"
    print(out_string)

    return out_string