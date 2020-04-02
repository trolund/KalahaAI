from Entities.Player import Player
from Enum.BoardPositions import BoardPositions


class Board:
    GameFinished = False

    def __init__(self, human_name, stone_amount, human_turn):
        self.human_player = Player(human_name, BoardPositions.Player, stone_amount)
        self.ai_player = Player("AI", BoardPositions.Computer, stone_amount)
        self.human_turn = human_turn

    def change_turn(self):
        self.human_turn = not self.human_turn

    def check_game_end(self):
        if sum(self.human_player.pits.StonePits) == 0 or not self.list_available_pits():
            self.ai_player.kalaha.score += sum(self.ai_player.pits.StonePits)
            self.GameFinished = True
        elif sum(self.ai_player.pits.StonePits) == 0 or not self.list_available_pits():
            self.human_player.kalaha.score += sum(self.human_player.pits.StonePits)
            self.GameFinished = True

    def list_available_pits(self):
        if self.human_turn:
            return [i for i, v in enumerate(self.human_player.pits.StonePits) if v > 0]
        else:
            return [i for i, v in enumerate(self.ai_player.pits.StonePits) if v > 0]

    def get_active_player(self):  # Get active player's identity.
        if self.human_turn:
            return BoardPositions.PlayerPosition
        else:
            return BoardPositions.AIPosition

    def get_current_game_state(self):
        if self.human_turn:
            game_state = []
            game_state.extend(self.human_player.pits.StonePits)
            game_state.append(self.human_player.kalaha.score)
            temp = self.ai_player.pits.StonePits.copy()  # Super important to implement .copy().
            # Otherwise it makes a reference.
            temp.reverse()
            game_state.extend(temp)
            game_state.append(self.ai_player.kalaha.score)
            return game_state

        else:
            game_state = []
            game_state.extend(self.ai_player.pits.StonePits)
            game_state.append(self.ai_player.kalaha.score)
            temp = self.human_player.pits.StonePits.copy()  # Super important to implement .copy().
            # Otherwise it makes a reference.
            temp.reverse()
            game_state.extend(temp)
            game_state.append(self.human_player.kalaha.score)
            return game_state

    def update_game_state(self, game_state):
        if self.human_turn:
            self.human_player.pits.StonePits = game_state[0:6]
            self.human_player.kalaha.score = game_state[6]
            self.ai_player.pits.StonePits = game_state[7:13]
            self.ai_player.kalaha.score = game_state[13]
        else:
            self.ai_player.pits.StonePits = game_state[0:6]
            self.ai_player.kalaha.score = game_state[6]
            self.human_player.pits.StonePits = game_state[7:13]
            self.human_player.kalaha.score = game_state[13]

    def move_stones(self, pit_number):
        keep_turn = False
        game_state = self.get_current_game_state()
        if pit_number not in self.list_available_pits():  # Invalid pit selected.
            print("Invalid pit choice. Please select a valid pit.")
        else:
            stone_amount = game_state[pit_number]
            print("Selected pit: " + str(pit_number) + ". Moving " + str(stone_amount) + " stones.")
            game_state[pit_number] = 0

            while stone_amount > 0:  # Standard stone movement procedure.
                pit_number += 1
                if pit_number == 13:
                    pit_number = 0
                game_state[pit_number] += 1
                stone_amount -= 1

            if pit_number == 6:  # Check to see if rule of Kalaha continuety is a fulfilled.
                print("Last stone was added to Kalaha! Extra turn rewarded.")
                self.update_game_state(game_state)
                keep_turn = True

            elif not 0 >= pit_number <= 5:
                if self.human_turn:
                    if game_state[pit_number] == 1:
                        game_state[6] += game_state[pit_number] + game_state[13 - (pit_number + 1)]
                        game_state[pit_number] = 0
                        game_state[13 - (pit_number + 1)] = 0
                        self.update_game_state(game_state)
                        keep_turn = True
                else:
                    if game_state[pit_number] == 1:
                        game_state[6] += game_state[pit_number] + game_state[13 - (pit_number + 1)]
                        game_state[pit_number] = 0
                        game_state[13 - (pit_number + 1)] = 0
                        self.update_game_state(game_state)
                        keep_turn = True

            self.update_game_state(game_state)
            self.check_game_end()

            if not keep_turn:
                self.change_turn()

    def print(self):  # Continuously reorients the game board after which player's turn it is.
        if not self.GameFinished:
            if self.human_turn:
                print("     Game board      ")
                print("    " + self.human_player.name + "'s turn    ")
                print("#####################")
                temp_list = self.ai_player.pits.StonePits
                temp_list.reverse()
                print(*temp_list, sep=" | ")
                print(str(self.ai_player.kalaha.score) + "                   " + str(self.human_player.kalaha.score))
                # temp_list2 = self.human_player.pits.StonePits
                # temp_list2.reverse()
                print(*self.human_player.pits.StonePits, sep=" | ")
                print("#####################\nAvailable pits: " + str(self.list_available_pits()))

            else:
                print("     Game board      ")
                print("   Computer's turn   ")
                print("#####################")
                temp_list = self.human_player.pits.StonePits
                temp_list.reverse()
                print(*temp_list, sep=" | ")
                print(str(self.human_player.kalaha.score) + "                   " + str(self.ai_player.kalaha.score))
                # temp_list2 = self.ai_player.pits.StonePits
                # temp_list2.reverse()
                print(*self.ai_player.pits.StonePits, sep=" | ")
                print("#####################\nAvailable pits: " + str(self.list_available_pits()))

        else:
            scoreboard = self.get_game_score()
            print("    Game finished    ")
            print("#####################")
            print("Game winner: " + str(scoreboard[2]))
            print("    Scoreboard       ")
            print("Player: " + str(scoreboard[0]) + " Computer: " + str(scoreboard[1]))
            print("#####################")

    def get_game_score(self):
        if self.ai_player.kalaha.score > self.human_player.kalaha.score:
            game_winner = BoardPositions.Computer.name
        else:
            game_winner = self.human_player.name
        return self.human_player.kalaha.score, self.ai_player.kalaha.score, game_winner
