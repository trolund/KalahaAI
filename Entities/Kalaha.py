class Kalaha:
    score = 0

    def __init__(self, score):
        self.score = score

    def add_to_kalaha(self, points):
        self.score += points

    def __setitem__(self, key, value):
        self.score = value

    def __getitem__(self, item):
        return self.score
