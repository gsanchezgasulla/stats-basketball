from team import Team
from player import Player
from play_by_play import Play, PlayType


class Game:
    def __init__(self):
        self.team_a = None
        self.team_b = None
        self.teams = {}
        self.date = ""
        self.category = ""
        self.play_by_play = {}

    def get_possessions_team_a(self):
        return self.teams[self.team_a].get_possessions()

    def get_possessions_team_b(self):
        return self.teams[self.team_b].get_possessions()

    def get_a_team_five(self, minute):
        return self.teams[self.team_a].get_five(minute)

    def get_b_team_five(self, minute):
        return self.teams[self.team_b].get_five(minute)

    def fill_game(self, json_game, json_play_by_play):
        self.__fill_game_details(json_game)
        self.__fill_play_by_play(json_play_by_play)
        self.__fill_players_play_by_play()

    def __fill_game_details(self, json_game):
        self.date = json_game["time"]
        self.team_a = json_game["localId"]
        self.team_b = json_game["visitId"]

        for json_team in json_game["teams"]:
            team = self.__fill_team(json_team)
            self.teams[team.team_id] = team

    def __fill_play_by_play(self, json_play_by_play):
        play_by_play = {}
        for json_play in json_play_by_play:
            play = Play()
            play.player_id = json_play["actorId"]
            play.team_id = json_play["idTeam"]

            # Here minutes go descending from 9 to 0, and are depending on the period, we need to standardize
            play.minute = 10*(json_play["period"]-1) + (10 - json_play["min"])
            play.fill_definition(json_play["idMove"])
            play.score_after_play = json_play["score"]
            if not play.minute in play_by_play.keys():
                play_by_play[play.minute] = []
            play_by_play[play.minute].append(play)

        self.play_by_play = play_by_play

    def __fill_players_play_by_play(self):
        for plays_in_minute in self.play_by_play.values():
            for play in plays_in_minute:
                self.teams[play.team_id].players[play.player_id].play_by_play.append(play)

    @staticmethod
    def __fill_team(json_team):
        team = Team()
        team.team_id = json_team["teamIdIntern"]
        team.name = json_team["name"]
        for player_json in json_team["players"]:
            player = Player()
            player.player_id = player_json["actorId"]
            player.name = player_json["name"]
            player.number = int(player_json["dorsal"])

            if player_json["starting"]:  # We need to create a IN Play
                play = Play()
                play.team_id = team.team_id
                play.player_id = player.player_id
                play.minute = 0
                play.definition = PlayType.SUBSTITUTION_IN

                player.play_by_play.append(play)

            player.fill_stats(player_json["data"])
            team.players[player.player_id] = player
        return team

