from GameState import Board
from GameLogic import GameLogic


# state is an array with 14 index, 7 and 14 are the stores, other indexes are pits with stones
def player(state):
    return state


def actions(state):
    legal_moves = []
    for i in range(len(state)):
        if state[i] != 0 and i != 6 and i != 13:
            legal_moves.append(i)  # which pits are allowed
    return legal_moves


# Takes the whole tuple as state
def result(state, action):
    if state[1]:
        stones = state[0][action]
        for i in range(stones):
            print(i)

    else:
        stones = state[0][action]
        for i in range(stones):
            print(i)


def terminal_test(state):
    if any(state[8:]) == False or any(state[1:7]) == False:
        return True
    return False


if __name__ == '__main__':
    tuple_state = ([4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0], True)  # the board is the first element, second element
    # is player turn (true for person, false for AI)
    print(actions(tuple_state[0]))
    print(terminal_test(tuple_state[0]))
    print(result(tuple_state, 1))
