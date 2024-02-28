import os
import enum
from rich import print as rprint
from os.path import join



class PlayerMove(enum.Enum):
    X = 1 # Rock
    Y = 2 # Paper
    Z = 3 # Scissor

class OpponentMove(enum.IntEnum):
    A = 1 # Rock
    B = 2 # Paper
    C = 3 # Scissor

class GameResults(enum.Enum):
    DEFEAT = 0
    DRAW = 3
    VICTORY = 6

RESULTS_CASES = {
    "VICTORY": {
        "A": PlayerMove.Y.value,
        "B": PlayerMove.Z.value,
        "C": PlayerMove.X.value,
        "POINTS": GameResults.VICTORY.value
    },
    "DEFEAT": {
        "A": PlayerMove.Z.value,
        "B": PlayerMove.X.value,
        "C": PlayerMove.Y.value,
        "POINTS": GameResults.DEFEAT.value

    },
    "DRAW": {
        "A": PlayerMove.X.value,
        "B": PlayerMove.Y.value,
        "C": PlayerMove.Z.value,
        "POINTS": GameResults.DRAW.value
    }
}

def detect_result(player_move):
    if player_move == PlayerMove.X.name:
        return GameResults.DEFEAT.name
    elif player_move == PlayerMove.Y.name:
        return GameResults.DRAW.name
    else:
        return GameResults.VICTORY.name



def solve():
	answers = []
	with open(join(__file__[:-9] + "data\input.txt"), "r") as game:
		for round in game:
			opponent_move = round[0]
			player_move = round[2]
			result = detect_result(player_move)
			answers.append(RESULTS_CASES[result]["POINTS"] + RESULTS_CASES[result][opponent_move])
	rprint(sum(answers))

if '__name__' == '__main__':
	solve()