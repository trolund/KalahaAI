from Entities.State import State
from Game import GameLogic


class AIController:

    def actions(self, state: State):
        temp_val = GameLogic.list_available_pits(state)
        return temp_val

    def utility(self, state: State):  # TODO bedre utility funktion engang i fremtiden
        if state.game_state[6] > state.game_state[13]:
            return 0
        elif state.game_state[6] == state.game_state[13]:
            return 0.5
        else:
            return 1

    def eval(self, state: State):
        return state.game_state[13] - state.game_state[6]

    def result(self, state: State, action):
        return GameLogic.new_state(state, action)

    def terminal_test(self, state: State):
        return GameLogic.game_finished(state)

    # A.I er max spiller
    def mini_max(self, state: State):
        utilities = []  # (utility value, action) --> max(utility value, action)

        for action in self.actions(state):
            newState = self.result(state, action)
            if newState.human_turn:  # Human_turn - True/False
                utilities.append((self.min_value(newState), action))  # Spillerens tur
            else:
                utilities.append((self.max_value(newState), action))  # A.I

        if state.human_turn:
            final_action = min(utilities)[1]
        else:
            final_action = max(utilities)[1]
        print(utilities)
        print("action:", final_action)
        return final_action

    def max_value(self, state: State, depth=3):
        if self.terminal_test(state) or depth == 0:
            return self.eval(state)
        v = -99999999
        # deepcopy her???
        for action in self.actions(state):
            newState = self.result(state, action)
            if newState.human_turn:
                v = max(v, self.min_value(newState, depth - 1))
            else:
                v = max(v, self.max_value(newState, depth - 1))
        return v

    def min_value(self, state: State, depth=3):
        if self.terminal_test(state) or depth == 0:
            return self.eval(state)
        v = 99999999
        for action in self.actions(state):
            newState = self.result(state, action)
            if state.human_turn:
                v = min(v, self.max_value(newState, depth - 1))
            else:
                v = min(v, self.min_value(newState, depth - 1))
        return v
