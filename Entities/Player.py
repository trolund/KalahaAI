from Entities.Kalaha import Kalaha
from Entities.RowOfPits import RowOfPits


class Player:
    name = ""
    board_position = None

    kalaha = Kalaha

    def __init__(self, name, board_position, stone_amount):
        self.name = name
        self.boardPosition = board_position
        self.pits = RowOfPits(stone_amount)
