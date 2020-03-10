class Board:
    AI_SCORE = 0
    PLAYER_SCORE = 7

    state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self):
        self.state = self.default_init(4)

    def get_ai_score(self):
        return self.state[self.AI_SCORE]

    def get_player_score(self):
        return self.state[self.PLAYER_SCORE]

    def default_init(self, start_value):
        return [0, start_value, start_value, start_value, start_value, start_value, start_value,
               0, start_value, start_value, start_value, start_value, start_value, start_value]

    def print(self):
        print("  ", end="")
        print(*["%2d" % x for x in reversed(self.state[8:])], sep=" |")
        print("%2d                      %2d" % (self.get_ai_score(), self.get_player_score()))
        print("  ", end="")
        print(*["%2d" % x for x in self.state[1:7]], sep=" |")
