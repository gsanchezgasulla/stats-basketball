from .game import Game
from tools.game_loader import GameLoader


class Season:

    def __init__(self):
        self.games = {}
        self.games_loader = GameLoader()

    def fill_season(self, partits):
        print("Carregant els partits...")

        for partit_key in partits.keys():
            print("Carregant el partit vs " + partit_key.replace("_", " "))

            json_game, json_play_by_play = self.games_loader.load_game_from_url(partits[partit_key])
            if len(json_game.keys()) > 0: # we found that in some cases there's an error retrieving the object and is returned empty
                game = Game(partit_key)
                game.fill_game(json_game, json_play_by_play)
                self.games[partit_key] = game