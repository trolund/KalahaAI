from Entities.Board import Board


class AIController:

    board = None
    state = None

    def __init__(self):
        self.board = Board("", 0, 1)

    def setState(self, state):
        self.board.update_game_state(state)

    def actions(self, state):
        self.board.update_game_state(state)
        return self.board.list_available_pits()

    def utility(self, state):
        if not state[len(state) - 1]:
            if state[6] > state[13]:  #Hvis A.Is kalaha > player kalaha
                return 1
            elif state[6] == state[13]:
                return 0.5
            else:
                return 0
        else:
            if state[13] > state[6]:  #Hvis A.Is kalaha > player kalaha
                return 1
            elif state[13] == state[6]:
                return 0.5
            else:
                return 0

    def result(self, state, action):
        self.board.update_game_state(state)
        self.board.move_stones(action)
        return self.board.get_current_game_state()

    def terminal_test(self, state):
        self.board.update_game_state(state)
        return self.board.check_game_end()

    def mini_max(self, state):
        utilities = []

        if state[-1]:  # Player
            for action in self.actions(state):
                newState = self.result(state, action)
                if newState[-1]:
                    utilities.append((self.min_value(newState), action))  # Spillerens tur
                else:
                    utilities.append((self.max_value(newState), action))  # A.I
            minValue = min(utilities)[1]
            return minValue
        else:  # A.I
            for action in self.actions(state):
                newState = self.result(state, action)
                if newState[-1]:
                    utilities.append((self.min_value(newState), action))  # Spillerens tur
                else:
                    utilities.append((self.max_value(newState), action))  # A.I
            maxValue = max(utilities)[1]
            return maxValue

    def max_value(self, state):
        if self.terminal_test(state):
            return self.utility(state)
        v = -99999999
        for action in self.actions(state):
            v = max(v, self.mini_max(self.result(state, action)))
        return v

    def min_value(self, state):
        if self.terminal_test(state):
            return self.utility(state)
        v = 99999999
        for action in self.actions(state):
            v = min(v, self.mini_max(self.result(state, action)))
        return v