class RowOfPits:
    StonePits = [0, 0, 0, 0, 0, 0]

    def __init__(self, initial_stones_pit):
        self.StonePits = [initial_stones_pit, initial_stones_pit, initial_stones_pit,
                          initial_stones_pit, initial_stones_pit, initial_stones_pit]

    def __setitem__(self, key, value):
        self.StonePits[key] = value

    def __getitem__(self, item):
        return self.StonePits[item]
