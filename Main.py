def actions(state, player_turn):
    legal_moves = []
    if player_turn:
        for i in range(6):
            if state[i] != 0:
                legal_moves.append(i)
    else:
        for i in range(7, 13):
            if state[i] != 0:
                legal_moves.append(i)

    return legal_moves


# Takes the whole tuple as state
def result(state, player_turn, action):
    stones_in_pit = state[action]
    state[action] = 0
    i = action
    if player_turn:
        while not stones_in_pit == 0:  # Læg 1 sten i den næste pit
            i += 1
            if i == 13:
                i = 0
            state[i] += 1
            stones_in_pit -= 1
        if (0 <= i <= 5 and state[i] == 1) or i == 6: # Hvis den endelige pit man lander i har 1 sten, så får man
            # en tur mere. Eller hvis man lander i ens store, så får man også en tur mere.
            return state, True
        else:
            return state, not player_turn
    else:
        while not stones_in_pit == 0:  # Læg 1 sten i den næste pit
            i += 1
            if i == 14:
                i = 0
            elif i == 6:
                i = 7
            state[i] += 1
            stones_in_pit -= 1
        if (7 <= i <= 12 and state[i] == 1) or i == 13:  # Hvis den endelige pit man lander i har 1 sten, så får man
            # en tur mere. Eller hvis man lander i ens store, så får man også en tur mere.
            return state, False
        else:
            return state, not player_turn


def terminal_test(state):
    if any(state[7:]) == False or any(state[0:6]) == False:
        remaining_player_points = 0
        remaining_ai_points = 0
        for i in range(6):
            remaining_player_points += state[i]
        for i in range(7, 13):
            remaining_ai_points += state[i]
        state[6] += remaining_player_points
        state[13] += remaining_ai_points
        return True
    return False


def utility(state):
    if state[6] > state[13]:
        return 'Player points: ' + state[6].__str__() + ', A.I points: ' + state[13].__str__() + ', which means that ' \
                                                                                                 'the player won! '
        #  return 1, 0
    elif state[6] < state[13]:
        return 'Player points: ' + state[6].__str__() + ', A.I points: ' + state[13].__str__() + ', which means that ' \
                                                                                                 'the A.I won! '
        #  return 0, 1
    elif state[6] == state[13]:
        return 'Player points: ' + state[6].__str__() + ', A.I points: ' + state[13].__str__() + ', which means that ' \
                                                                                                 'it is a draw '
        #  return 0.5, 0.5


if __name__ == '__main__':
    state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]  # Initial state (s0)
    player_turn = True  # Player starts
    print(state)
    while not terminal_test(state):  # while game is NOT over
        if player_turn:
            print('---------- Player\'s turn ----------')
            pit_list = actions(state, player_turn)
            available_pits = ''
            for i in range(len(pit_list)):  # laver for loopet for at udplukke hver pit og lave det om til en streng
                # som jeg kan udskrive to linjer længere nede
                available_pits += pit_list[i].__str__() + ', '
            print('Choose a pit.\nYou can choose: ' + available_pits)
            selected_pit = input()
            while selected_pit.isdigit() and (selected_pit in pit_list):
                print('You must choose between: ' + available_pits)
                selected_pit = input()
            state, player_turn = result(state, player_turn, int(selected_pit))
        else:
            print('---------- A.I\'s turn ----------')
            pit_list = actions(state, player_turn)  # actions returnerer et array med hver mulig pit
            available_pits = ''
            for i in range(len(pit_list)):
                available_pits += pit_list[i].__str__() + ', '
            print('Choose a pit.\nYou can choose: ' + available_pits)
            selected_pit = input()
            while selected_pit.isdigit() and (selected_pit in pit_list):
                print('You must choose between: ' + available_pits)
                selected_pit = input()
            state, player_turn = result(state, player_turn, int(selected_pit))
        print(state)

    print('----------------------------------------------------------------------')
    print(utility(state))
    print('----------------------------------------------------------------------')