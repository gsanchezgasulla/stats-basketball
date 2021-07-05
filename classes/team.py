import inspect

from play import Play, PlayType

class Team:
    def __init__(self):
        self.name = ""
        self.players = []

    def get_points(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_total_rebounds(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_offensive_rebounds(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_defensive_rebounds(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_assists(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_turnovers(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_steals(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_blocked_shots(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_blocks_received(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_fouls_made(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_fouls_attempted(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_two_attempted(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_two_made(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_three_attempted(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_three_made(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_free_throw_attempted(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_free_throw_made(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_two_percentage(self):
        return float(self.get_two_made())/self.get_two_attempted()

    def get_three_percentage(self):
        return float(self.get_three_made())/self.get_three_attempted()

    def get_free_throw_percentage(self):
        return float(self.get_free_throw_made())/self.get_free_throw_attempted()

    def get_five(self, minute):
        five = []
        for player in self.players:
            for index, play in enumerate(player.play_by_play):
                if play.minute >= minute:
                    previous_play = player.play_by_play[index - 1]
                    if previous_play.definition == PlayType.SUBSTITUTION_IN:
                        five.append(player.name)
                    break
        return five

    # Advanced stats
    def get_possessions(self):
        return self.get_two_attempted() + self.get_three_attempted() + 0.44 * self.get_free_throw_attempted() + self.get_turnovers() - self.get_offensive_rebounds()

    def get_effective_field_goal(self):
        return float(self.get_two_made() + 1.5 * self.get_three_made()) / (self.get_two_attempted() + self.get_three_attempted())

    def get_true_shoot(self):
        return float(self.get_points()) / ((0.44 * self.get_free_throw_made() + self.get_two_attempted() + self.get_three_attempted()) * 2)

    def get_usage_two(self):
        return float(self.get_two_attempted())/(self.get_two_attempted() + self.get_three_attempted() + 0.44*self.get_free_throw_attempted() + self.get_turnovers())

    def get_usage_three(self):
        return float(self.get_three_attempted()) / (self.get_two_attempted() + self.get_three_attempted() + 0.44 * self.get_free_throw_attempted() + self.get_turnovers())

    def get_turnover_percentage(self):
        return float(self.get_turnovers()) / (self.get_two_attempted() + self.get_three_attempted() + 0.44 * self.get_free_throw_attempted() + self.get_turnovers())

    def get_free_throw_attempt_rate(self):
        return float(self.get_free_throw_made()) / (self.get_three_attempted() + self.get_two_attempted())

    def __get_generic(self, data_string):
        total = 0
        for player in self.players:
            total += getattr(player.stats, data_string)()
        return total
