import inspect

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

    def get_two_percentage(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_three_percentage(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def get_free_throw_percentage(self):
        return self.__get_generic(inspect.currentframe().f_code.co_name)

    def __get_generic(self, data_string):
        total = 0
        for player in self.players:
            total += getattr(player.stats, data_string)
        return total
