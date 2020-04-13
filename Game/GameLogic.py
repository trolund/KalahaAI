from Entities.State import State
import copy


def list_available_pits(state: State):
    if state.human_turn:
        return [i for i, v in enumerate(state.game_state[0:6]) if v > 0]
    else:
        temp_val = [i for i, v in enumerate(state.game_state[7:13]) if v > 0]
        for i, value in enumerate(temp_val):
            temp_val[i] += 7  # 0, 2, 10 (7, 9, 17)
        return temp_val


def new_state(state: State, pit_number):  # 5
    newState = copy.deepcopy(state)
    stone_amount = newState.game_state[pit_number]
    newState.game_state[pit_number] = 0

    while stone_amount > 0:  # Standard stone movement procedure.
        pit_number += 1
        if state.human_turn and pit_number == 13:
            pit_number = 0
        elif not state.human_turn and pit_number == 14:
            pit_number = 0
        elif not state.human_turn and pit_number == 6:
            pit_number = 7
        newState.game_state[pit_number] += 1
        stone_amount -= 1

    if not (newState.human_turn and pit_number == 6) and not (not newState.human_turn and pit_number == 13):
        if newState.human_turn and 0 <= pit_number <= 5 and newState.game_state[pit_number] == 1:  # stjæl points
            pos = 13 - (pit_number + 1)
            newState.game_state[6] += newState.game_state[pos] + newState.game_state[pit_number]
            newState.game_state[pos] = 0
            newState.game_state[pit_number] = 0
        elif not newState.human_turn and 7 <= pit_number <= 12 and newState.game_state[pit_number] == 1:  # stjæl points
            pos = 13 - (pit_number + 1)
            newState.game_state[13] += newState.game_state[pos] + newState.game_state[pit_number]
            newState.game_state[pos] = 0
            newState.game_state[pit_number] = 0
        newState.human_turn = not newState.human_turn
    return newState


def game_finished(state: State):
    if sum(state.game_state[0:6]) == 0:
        state.game_state[13] += sum(state.game_state[7:13])
        for i in range(7, 13):
            state.game_state[i] = 0
        return True
    elif sum(state.game_state[7:13]) == 0:
        state.game_state[6] += sum(state.game_state[0:6])
        for i in range(6):
            state.game_state[i] = 0
        return True
    else:
        return False


def print_state(state: State):  # Continuously reorients the game board after which player's turn it is.
    if not game_finished(state):

        print(state.game_state)

        print("     Game board      ")
        if state.human_turn:
            print("  Player One's turn    ")  #
        else:
            print("  Player Two's turn    ")  #
        print("#####################")
        temp_list = state.game_state[7:13]  # 0 - 5
        temp_list.reverse()
        print(*temp_list, sep=" | ")
        print(str(state.game_state[13]) + "                   " + str(state.game_state[6]))
        print(*state.game_state[0:6], sep=" | ")
        print("#####################\nAvailable pits: " + str(list_available_pits(state)))

    else:
        print("      Game over!")
        scoreboard = state.game_state.copy()
        print("    Game finished    ")
        print("#####################")
        #  print("Game winner: " + str(scoreboard[2]))
        print("    Scoreboard:")
        print("   Player One: " + str(scoreboard[6]) + "\n   Player Two: " + str(scoreboard[13]))
        print("#####################")
