def actions(state, player_turn):
    legal_moves = []
    if player_turn:
        for i in range(6):
            if state[i] != 0:
                legal_moves.append(i)
    else:
        for i in range(8, 13):
            if state[i] != 0:
                legal_moves.append(i)

    return legal_moves


# Takes the whole tuple as state
def result(state, player_turn, action):
    if player_turn:
        stones_in_pit = state[action]
        state[action] = 0
        i = action + 1
        while not stones_in_pit == 0:  # Læg 1 sten i den næste pit
            if i == 13:
                i = 0
            state[i] += 1
            stones_in_pit -= 1
            i += 1
        if state[i] == 1:
            return state, True  # Hvis den endelige pit man lander i har 1 sten, så får man en tur mere.
        else:
            return state, not player_turn
    else:
        stones_in_pit = state[action]
        state[action] = 0
        i = action + 1
        while not stones_in_pit == 0:  # Læg 1 sten i den næste pit
            if i == 14:
                i = 0
            elif i == 6:
                i = 7
            state[i] += 1
            stones_in_pit -= 1
            i += 1
        if state[i] == 1:  # Hvis den endelige pit man lander i har 1 sten, så får man en tur mere.
            return state, False
        else:
            return state, not player_turn


def terminal_test(state):
    if any(state[8:]) == False or any(state[1:7]) == False:
        return True
    return False


def utility(state):
    if state[7] > state[14]:
        return 1, 0
    elif state[7] < state[14]:
        return 0, 1
    elif state[7] == state[14]:
        return 0.5, 0.5


if __name__ == '__main__':
    state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]  # Initial state (s0)
    player_turn = True  # Player starts
    while not terminal_test(state):  # while game is NOT over
        if player_turn:
            pit_list = actions(state, player_turn)
            available_pits = ''
            for i in range(len(pit_list)):
                available_pits += pit_list[i].__str__() + ', '  # TODO if / else hvis man vil fjerne kommaet på det sidste tal.
            print('Choose a pit.\nYou can choose: ' + available_pits)
            selected_pit = input()
            while selected_pit.isdigit() and (selected_pit in pit_list):
                print('You must choose between: ' + available_pits)
                selected_pit = input()
            state, player_turn = result(state, player_turn, int(selected_pit))
        else:
            pit_list = actions(state, player_turn)
            available_pits = ''
            for i in range(len(pit_list)):
                available_pits += pit_list[
                                      i].__str__() + ', '  # TODO if / else hvis man vil fjerne kommaet på det sidste tal.
            print('Choose a pit.\nYou can choose: ' + available_pits)
            selected_pit = input()
            while selected_pit.isdigit() and (selected_pit in pit_list):
                print('You must choose between: ' + available_pits)
                selected_pit = input()
            state, player_turn = result(state, player_turn, int(selected_pit))
        print(state)

    print(utility(state))