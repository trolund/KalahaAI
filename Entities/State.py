

class State:

    human_turn = True
    game_state = []

    def __init__(self, human_turn):
        self.human_turn = human_turn
        self.game_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

