from Entities.Kalaha import Kalaha
from Entities.RowOfPits import RowOfPits


class Player:
    name = ""
    board_position = None

    pits = RowOfPits(4)
    kalaha = Kalaha

    def __init__(self, name, board_position):
        self.name = name
        self.boardPosition = board_position
