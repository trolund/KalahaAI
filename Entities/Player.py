from Entities.Kalaha import Kalaha
from Entities.RowOfPits import RowOfPits


class Player:

    def __init__(self, name, board_position, stone_amount, initial_score):
        self.name = name
        self.boardPosition = board_position
        self.pits = RowOfPits(stone_amount)
        self.kalaha = Kalaha(initial_score)
