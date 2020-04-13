from Entities.State import State
from Game import GameLogic


class AIController:

    def __init__(self, depth=5):
        self.init_depth = depth

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

    def eval(self, state: State): #
        return state.game_state[13] - state.game_state[6]

   # def eval2(self, state: State, depth: int, is_max: bool):
    #    if is_max:
     #       return (state.game_state[13] - state.game_state[6]) + depth * 10
      #  else:
       #     return (state.game_state[6] - state.game_state[13]) - depth * 10

    def eval2(self, state: State, depth: int, is_max: bool):
            return (state.game_state[13] - state.game_state[6]) * (5 - depth)

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
                utilities.append((self.min_value(newState, self.init_depth), action))  # Spillerens tur
            else:
                utilities.append((self.max_value(newState, self.init_depth), action))  # A.I

        if state.human_turn:
            final_action = min(utilities)[1]
        else:
            final_action = max(utilities)[1]
        print(utilities)
        print("action:", final_action)
        return final_action

    def max_value(self, state: State, depth = 3):
        if self.terminal_test(state) or depth == 0:
           # return self.eval2(state, depth, True)
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
           # return self.eval2(state, depth, False)
           return self.eval(state)
        v = 99999999
        for action in self.actions(state):
            newState = self.result(state, action)
            if state.human_turn:
                v = min(v, self.max_value(newState, depth - 1))
            else:
                v = min(v, self.min_value(newState, depth - 1))
        return v

    def alpha_beta_search(self, state: State):
        utilities = []  # (utility value, action) --> max(utility value, action)

        alpha = -9999999
        beta = 9999999

        for action in self.actions(state):
            newState = self.result(state, action)
            if newState.human_turn:  # Human_turn - True/False
                utilities.append((self.alpha_beta_min_value(newState, alpha, beta, self.init_depth), action))  # Spillerens tur
            else:
                utilities.append((self.alpha_beta_max_value(newState, alpha, beta, self.init_depth), action))  # A.I

        if state.human_turn:
            final_action = min(utilities)[1]
        else:
            final_action = max(utilities)[1]
        print(utilities)
        print("action:", final_action)
        return final_action

    def alpha_beta_max_value(self, state: State, alpha, beta, depth=3):
        if self.terminal_test(state) or depth == 0:
            return self.eval(state)
        v = -99999999

        for action in self.actions(state):
            newState = self.result(state, action)

            if newState.human_turn:
                v = max(v, self.alpha_beta_min_value(newState, alpha, beta, depth - 1))

            else:
                v = max(v, self.alpha_beta_max_value(newState, alpha, beta, depth - 1))

            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v


    def alpha_beta_min_value(self, state: State, alpha, beta, depth=3):
        if self.terminal_test(state) or depth == 0:
            return self.eval(state)
        v = 99999999
        for action in self.actions(state):
            newState = self.result(state, action)
            if state.human_turn:
                v = min(v, self.alpha_beta_max_value(newState, alpha, beta, depth - 1))
            else:
                v = min(v, self.alpha_beta_min_value(newState, alpha, beta, depth - 1))

            if v <= alpha:
                return v
            beta = min(beta, v)
        return v