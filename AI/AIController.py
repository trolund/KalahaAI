from Entities.State import State
from Game import GameLogic


class AIController:

    def actions(self, state: State):
        return GameLogic.list_available_pits(state)

    def utility(self, state: State): # TODO bedre utility funktion engang i fremtiden
        if state.game_state[6] > state.game_state[13]:
            return 0
        elif state.game_state[6] == state.game_state[13]:
            return 0.5
        else:
            return 1

    def result(self, state: State, action):
        return GameLogic.new_state(state, action)

    def terminal_test(self, state: State):
        return GameLogic.game_finished(state)

    #A.I er max spiller
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

        return final_action

    def max_value(self, state: State):
        if self.terminal_test(state):
            return self.utility(state)
        v = -99999999
        for action in self.actions(state):
            newState = self.result(state, action)
            if newState.human_turn:
                v = max(v, self.min_value(newState))
            else:
                v = max(v, self.max_value(newState))
        return v

    def min_value(self, state: State):
        if self.terminal_test(state):
            return self.utility(state)
        v = 99999999
        for action in self.actions(state):
            newState = self.result(state, action)
            if state.human_turn:
                v = min(v, self.max_value(newState))
            else:
                v = min(v, self.min_value(newState))
        return v
