class AIController:

    def __init__(self, board):
        self.board = board
        print(board)

    def actions(self, state):
        legal_actions = []
        for i in range(6):
            if state[i] != 0:
                legal_actions.append(state[i])

    def utility(self, state):
        if state[6] > state[13]:  #Hvis A.Is kalaha > player kalaha
            return 1
        elif state[6] == state[13]:
            return 0.5
        else:
            return 0


    def result(self, state, action):
        print(state)


    def terminal_test(self, state):
        print(state)


