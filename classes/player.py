import inspect

class Player:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.stats = None
        self.uid = 0
        self.play_by_play = []

class PlayerStats:
    def __init__(self):
        self.minutes = 0
        self.defensive_rebounds = 0
        self.offensive_rebounds = 0
        self.assists = 0
        self.steals = 0
        self.turnovers = 0
        self.blocked_shots = 0
        self.blocks_received = 0
        self.fouls_made = 0
        self.fouls_received = 0

        # Points section
        self.two_attempted = 0
        self.two_made = 0
        self.three_attempted = 0
        self.three_made = 0
        self.free_throw_attempted = 0
        self.free_throw_made = 0

    def get_points(self):
        return self.two_made * 2 + self.three_made * 3 + self.free_throw_made

    def get_assists(self):
        return self.assists

    def get_steals(self):
        return self.steals

    def get_turnovers(self):
        return self.turnovers

    def get_blocked_shots(self):
        return self.blocked_shots

    def get_blocks_received(self):
        return self.blocks_received

    def get_total_rebounds(self):
        return self.defensive_rebounds + self.offensive_rebounds

    def get_defensive_rebounds(self):
        return self.defensive_rebounds

    def get_offensive_rebounds(self):
        return self.offensive_rebounds

    def get_fouls_made(self):
        return self.fouls_made

    def get_fouls_received(self):
        return self.fouls_received

    def get_two_percentage(self):
        return self.two_made / float(self.two_attempted)

    def get_three_percentage(self):
        return self.three_made / float(self.three_attempted)

    def get_free_throw_percentage(self):
        return self.free_throw_made / float(self.free_throw_attempted)

    def get_two_attempted(self):
        return self.two_attempted

    def get_two_made(self):
        return self.two_made

    def get_three_attempted(self):
        return self.three_attempted

    def get_three_made(self):
        return self.three_made

    def get_free_throw_attempted(self):
        return self.free_throw_attempted

    def get_free_throw_made(self):
        return self.free_throw_made

    # Advanced stats
    def get_possessions(self):
        return self.two_attempted + self.three_attempted + 0.44 * self.free_throw_attempted + self.turnovers - self.offensive_rebounds

    def get_effective_field_goal(self):
        return float(self.two_made + 1.5 * self.three_made) / (self.two_attempted + self.three_attempted)

    def get_true_shoot(self):
        return float(self.get_points()) / ((0.44 * self.two_attempted + self.two_attempted + self.three_attempted) * 2)

    def get_usage_two(self):
        return float(self.two_attempted)/(self.two_attempted + self.three_attempted + 0.44*self.free_throw_attempted + self.turnovers)

    def get_usage_three(self):
        return float(self.three_attempted) / (self.two_attempted + self.three_attempted + 0.44 * self.free_throw_attempted + self.turnovers)

    def get_turnover_percentage(self):
        return float(self.turnovers) / (self.two_attempted + self.three_attempted + 0.44 * self.free_throw_attempted + self.turnovers)

    def get_free_throw_attempt_rate(self):
        return float(self.free_throw_made) / (self.three_attempted + self.two_attempted)
