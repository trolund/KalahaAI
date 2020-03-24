import copy
import time

def actions(state):
    legal_moves = []
    if state[1]:
        for i in range(6):
            if state[0][i] != 0:
                legal_moves.append(i)
    else:
        for i in range(7, 13):
            if state[0][i] != 0:
                legal_moves.append(i)
    #  print("moves: " + legal_moves.__str__())
    return legal_moves


# Takes the whole tuple as state
def result(state, action):
    # print(state, action)
    stones_in_pit = state[0][action]
    state[0][action] = 0
    i = action
    if state[1]:
        while not stones_in_pit == 0:  # Læg 1 sten i den næste pit
            i += 1
            if i == 13:
                i = 0
            state[0][i] += 1
            stones_in_pit -= 1
        if i == 6:  # Hvis den endelige pit man lander i har 1 sten, så får man
            # en tur mere. Eller hvis man lander i ens store, så får man også en tur mere.
            state[1] = True
            #  return state
        elif 0 <= i <= 5 and state[0][i] == 1:
            get_opposite_points(i, state)
            state[1] = False
        else:
            state[1] = False
            #  return state
    else:
        while not stones_in_pit == 0:  # Læg 1 sten i den næste pit
            i += 1
            if i == 14:
                i = 0
            elif i == 6:
                i = 7
            state[0][i] += 1
            stones_in_pit -= 1
        if i == 13:  # Hvis den endelige pit man lander i har 1 sten, så får man
            # en tur mere. Eller hvis man lander i ens store, så får man også en tur mere.
            state[1] = False
            #  return state
        elif 7 <= i <= 12 and state[0][i] == 1:
            get_opposite_points(i, state)
            state[1] = True
        else:
            state[1] = True
    return state


def get_opposite_points(n, state):
        if n != 6 or n != 13:
            pos = 13 - (n + 1)

            if state[1]:
                state[0][6] += state[0][pos] + state[0][n]
            else:
                state[0][13] += state[0][pos] + state[0][n]

            state[0][pos] = 0
            state[0][n] = 0


def terminal_test(state):
    if sum(state[0][7:13]) == 0 or sum(state[0][0:6]) == 0:
        remaining_player_points = 0
        remaining_ai_points = 0
        for i in range(6):
            remaining_player_points += state[0][i]
        for i in range(7, 13):
            remaining_ai_points += state[0][i]
        state[0][6] += remaining_player_points
        state[0][13] += remaining_ai_points
        return True
    return False


def utility(state):
    if state[0][6] > state[0][13]:
        return 0
    elif state[0][6] == state[0][13]:
        return 0.5
    else:
        return 1


# Definer evaluation funktion


def mini_max(state, depth=2):
    utilities = []

    if state[1]:  # Player

        for action in actions(state):
            #  return max_value(mini_max(result(state, action), depth - 1))
            utilities.append((min_value(result(state, action), depth), action))
            # theAction = utilities.index(minValue)[1]
        minValue = min(utilities)[1]  # [0, 0.5, 1, 0.5, 0] --> 2
        print(minValue)
        return minValue
    else:  # A.I
        for action in actions(state):
            #  return min_value(mini_max(result(state, action), depth - 1))
            utilities.append((max_value(result(state, action), depth), action))
            # theAction = utilities.index(maxValue)[1]
        maxValue = max(utilities)[1]
        print(maxValue)
        return maxValue


def max_value(state, depth):
    if terminal_test(state) or depth == 0:
        return utility(state)
    v = -99999999
    for action in actions(state):
        v = max(v, min_value(result(state, action), depth - 1))
    return v


def min_value(state, depth):
    if terminal_test(state):
        return utility(state)
    v = 99999999
    for action in actions(state):
        v = min(v, max_value(result(state, action), depth - 1))
    return v


def alpha_beta_search(state, depth=2):
    #  v = max_value_alpha_beta(state, -9999, 9999)

    alpha = -9999
    beta = 9999

    utilities = []

    if state[1]:  # Player
        for action in actions(state):
            utilities.append((min_value_alpha_beta(result(state, action), alpha, beta, depth), action))
        minValue = min(utilities)[1]  # [0, 0.5, 1, 0.5, 0] --> 2
        print(minValue)
        return minValue
    else:  # A.I
        for action in actions(state):
            utilities.append((max_value_alpha_beta(result(state, action), alpha, beta, depth), action))
        maxValue = max(utilities)[1]
        print(maxValue)
        return maxValue


def max_value_alpha_beta(state, alpha, beta, depth):
    if terminal_test(state) or depth == 0:
        return utility(state)

    v = alpha
    for action in actions(state):
        v = max(v, min_value_alpha_beta(result(state, action), alpha, beta, depth - 1))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def min_value_alpha_beta(state, alpha, beta, depth):
    if terminal_test(state) or depth == 0:
        return utility(state)

    v = beta
    for action in actions(state):
        v = min(v, max_value_alpha_beta(result(state, action), alpha, beta, depth - 1))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v


def print_state(state):
    print("  ", end="")
    print(*["%2d" % x for x in reversed(state[0][7:13])], sep=" |")
    print("%2d                      %2d" % (state[0][13], state[0][6]))
    print("  ", end="")
    print(*["%2d" % x for x in state[0][0:6]], sep=" |")


def print_endgame(state):
    print(" - - - - - - - - - - - - - - ")
    print("AI                      You")
    print("%2d                      %2d" % (state[0][13], state[0][6]))
    print(" - - - - - - - - - - - - - - ")


def game_setup():
    print(" - Setup the AI - ")
    print("Who starts the game:")
    print("0 - You")
    print("1 - The AI")
    player_turn = int(input()) == 0
    print("Enter algo to use, options are:")
    print("0 - Minimax")
    print("1 - Minimax with pruning")
    algo = int(input())
    print("Enter tree depth:")
    depth = int(input())
    return (player_turn, algo, depth)


if __name__ == '__main__':
    setup = game_setup()
    board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]  # Initial state (s0)
    player_turn = setup[0]  # Player starts
    state = [board, player_turn]
    depth = setup[2]
    algo = setup[1]
    print(state, setup)
    input()
    while not terminal_test(state):  # while game is NOT over
        if state[1]:
            print('---------- Player\'s turn ----------')
            pit_list = actions(state)
            available_pits = ''
            for i in range(len(pit_list)):  # laver for loopet for at udplukke hver pit og lave det om til en streng
                # som jeg kan udskrive to linjer længere nede
                available_pits += pit_list[i].__str__() + ', '
            print('Choose a pit.\nYou can choose: ' + available_pits)
            selected_pit = input()
            while selected_pit.isdigit() and selected_pit not in available_pits:
                print('You must choose between: ' + available_pits)
                selected_pit = input()
            state = result(state, int(selected_pit))
        else:
            print('---------- A.I\'s turn ----------')
            #  state = result(state, ai_move(state))
            copyState = copy.deepcopy(state)
            start = time.monotonic_ns()
            if algo == 0:
                state = result(state, mini_max(copyState, depth))  # Alm. mini-max
            elif algo == 1:
                state = result(state, alpha_beta_search(copyState, depth))
            end = time.monotonic_ns()
            print("time taken: " + str((end - start) / 1000000) + "ms")
        print_state(state)

    print_endgame(state)


