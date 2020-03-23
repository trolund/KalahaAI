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
            state[1] = True
            #  return state
            #  pos = 13 - i
            #  state[0][6] += state[0][i] + state[0][pos]
            #  state[0][pos] = 0
            #  state[0][i] = 0
        else:
            state[1] = False
            #  return state
        return state
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
            state[1] = False
            #  return state
            #  pos = 13 - i
            #  state[0][13] += state[0][i] + state[0][pos]
            #  state[0][pos] = 0
            #  state[0][i] = 0
        else:
            state[1] = True
        #  print(state)
        return state


def terminal_test(state):
    print("State?: ", state)
    if sum(state[0][7:]) == 0 or sum(state[0][0:6]) == 0:
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

def mini_max(state):
    utilities = []

    if state[1]:
        for action in actions(state):
            #  return max_value(mini_max(result(state, action), depth - 1))
            utilities.append(min_value(result(state, action)))
            minValue = min(utilities)
            print(minValue)
            return utilities.index(minValue)
    else:
        for action in actions(state):
            #  return min_value(mini_max(result(state, action), depth - 1))
            utilities.append(max_value(result(state, action)))
            maxValue = max(utilities)
            print(maxValue)
            return utilities.index(maxValue)


def max_value(state, depth=2):
    if terminal_test(state) or depth == 0:
        return utility(state)
    v = -99999999
    for action in actions(state):
        v = max(v, min_value(result(state, action), depth - 1))
    return v


def min_value(state, depth=2):
    if terminal_test(state):
        return utility(state)
    v = 99999999
    for action in actions(state):
        v = min(v, max_value(result(state, action), depth - 1))
    return v


if __name__ == '__main__':
    board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]  # Initial state (s0)
    player_turn = True  # Player starts
    state = [board, player_turn]
    print(state)
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
            copyState = state
            state = result(state, mini_max(copyState))
        print(state)

    print('----------------------------------------------------------------------')
    print(utility(state))
    print('----------------------------------------------------------------------')
