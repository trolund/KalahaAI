class Board:
    AI_SCORE = 0
    PLAYER_SCORE = 7

    state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self):
        self.state = self.default_init(4)

    def default_init(self, start_value):
        return [0, start_value, start_value, start_value, start_value, start_value, start_value,
               0, start_value, start_value, start_value, start_value, start_value, start_value]

    def player_points(self, gameover):
        if gameover:
            return sum(self.state[1:8])
        else:
            return self.state[7]

    def ai_points(self, gameover):
        if gameover:
            return self.state[0] + sum(self.state[8:])
        else:
            return self.state[0]

    def print(self, gameover):
        ai_points = self.ai_points(gameover)
        player_points = self.player_points(gameover)
        if not gameover:
            print("  ", end="")
            print(*["%2d" % x for x in reversed(self.state[8:])], sep=" |")
            print("%2d                      %2d" % (ai_points, player_points))
            print("  ", end="")
            print(*["%2d" % x for x in self.state[1:7]], sep=" |")
        else:
            print(" - - - - - - - - - - - - - - ")
            print("AI                      You")
            print("%2d                      %2d" % (ai_points, player_points))
            print(" - - - - - - - - - - - - - - ")
