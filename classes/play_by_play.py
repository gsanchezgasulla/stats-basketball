from enum import Enum


class Play:

    def __init__(self):
        self.minute = 0
        self.team_id = 0
        self.player_id = 0
        self.definition = ""
        self.coordinates = []
        self.score_after_play = "0-0"

    def fill_definition(self, id_play):
        if id_play == 92:
            self.definition = PlayType.FREE_THROW_MADE
        elif id_play == 93:
            self.definition = PlayType.TWO_MADE
        elif id_play == 94:
            self.definition = PlayType.THREE_MADE
        elif id_play == 96:
            self.definition = PlayType.FREE_THROW_ATTEMPTED
        elif id_play == 97:
            self.definition = PlayType.TWO_ATTEMPTED
        elif id_play == 98:
            self.definition = PlayType.THREE_ATTEMPTED
        elif id_play == 106:
            self.definition = PlayType.TURNOVER
        elif id_play == 109:
            self.definition = PlayType.OFFENSIVE_FOUL_MADE
        elif id_play == 112:
            self.definition = PlayType.SUBSTITUTION_IN
        elif id_play == 115:
            self.definition = PlayType.SUBSTITUTION_OUT
        elif id_play == 159:
            self.definition = PlayType.FOUL_MADE
        elif id_play == 160:  # 1 point shot
            self.definition = PlayType.FOUL_MADE
        elif id_play == 161:  # 2 points shot
            self.definition = PlayType.FOUL_MADE


    def fill_score(self, score_string):
        pass


class PlayType(Enum):

    SUBSTITUTION_IN = "SUBSTITUTION_IN"
    SUBSTITUTION_OUT = "SUBSTITUTION_OUT"
    ASSIST = "ASSIST"
    STEAL = "STEAL"
    TURNOVER = "TURNOVER"
    BLOCKED_SHOT = "BLOCKED_SHOT"
    BLOCKS_RECEIVED = "BLOCKS_RECEIVED"
    OFFENSIVE_FOUL_MADE = "OFFENSIVE_FOUL_MADE"
    FOUL_MADE = "FOUL_MADE"
    FOUL_RECEIVED = "FOUL_RECEIVED"
    TWO_ATTEMPTED = "TWO_ATTEMPTED"
    TWO_MADE = "TWO_MADE"
    THREE_ATTEMPTED = "THREE_ATTEMPTED"
    THREE_MADE = "THREE_MADE"
    FREE_THROW_ATTEMPTED = "FREE_THROW_ATTEMPTED"
    FREE_THROW_MADE = "FREE_THROW_MADE"
