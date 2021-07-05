
class Season:
    def __init__(self):
        self.games = []


class Game:
    def __init__(self):
        self.team_a = None
        self.team_b = None
        self.date = ""
        self.category = ""

    def get_possessions_team_a(self):
        return self.team_a.get_possessions()

    def get_possessions_team_b(self):
        return self.team_b.get_possessions()



