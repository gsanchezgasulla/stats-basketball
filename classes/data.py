
class Season:
    def __init__(self):
        self.games = []


class Game:
    def __init__(self):
        self.team_a = None
        self.team_b = None
        self.date = ""
        self.category = ""
        self.play_by_play = []

    def get_possessions_team_a(self):
        return self.team_a.get_possessions()

    def get_possessions_team_b(self):
        return self.team_b.get_possessions()

    def get_a_team_five(self, minute):
        return self.team_a.get_five(minute)

    def get_b_team_five(self, minute):
        return self.team_b.get_five(minute)

    def fill_play_by_play(self, play_by_play):