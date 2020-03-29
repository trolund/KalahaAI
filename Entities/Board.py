from Entities.Player import Player
from Enum.BoardPositions import BoardPositions


class Board:
    human_player = Player("Peter", BoardPositions.Player, 4, 0)
    ai_player = Player("AI", BoardPositions.Computer, 4, 0)

    human_turn = True
    GameFinished = False

    def change_turn(self):
        self.human_turn = not self.human_turn

    def check_game_end(self):
        if not self.human_player.pits or not self.ai_player.pits:  # In Python, all empty lists are False.
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
            game_state.extend(self.ai_player.pits.StonePits)
            game_state.append(self.ai_player.kalaha.score)
            return game_state
        else:
            game_state = []
            game_state.extend(self.ai_player.pits.StonePits)
            game_state.append(self.ai_player.kalaha.score)
            game_state.extend(self.human_player.pits.StonePits)
            game_state.append(self.human_player.kalaha.score)
            return game_state

    def update_game_state(self, game_state):
        if self.human_turn:
            self.human_player.pits.StonePits = game_state[0:6]
            self.human_player.kalaha.score = game_state[6]
            temp = game_state[7:13]
            temp.reverse()
            self.ai_player.pits.StonePits = temp
            self.ai_player.kalaha.score = game_state[13]
        else:
            self.ai_player.pits.StonePits = game_state[0:6]
            self.ai_player.kalaha.score = game_state[6]
            temp = game_state[7:13]
            temp.reverse()
            self.human_player.pits.StonePits = temp
            self.human_player.kalaha.score = game_state[13]

    def move_stones(self, pit_number):
        game_state = self.get_current_game_state()
        stone_amount = game_state[pit_number]
        print("Selected pit: " + str(pit_number) + ". Moving " + str(stone_amount) + " stones.")
        game_state[pit_number] = 0

        if stone_amount is 0:  # Player selected an empty pit.
            print("Invalid pit choice. Please select a pit with stones present.")
        else:
            while stone_amount > 0:
                pit_number += 1
                if pit_number is 13:
                    pit_number = 0
                game_state[pit_number] += 1
                stone_amount -= 1

            self.update_game_state(game_state)
            self.change_turn()

    def print(self):  # Continuously reorients the game board after which player's turn it is.
        if not self.GameFinished:
            if self.human_turn:
                print("     Game board      ")
                print("    Player's turn    ")
                print("#####################")
                temp_list = self.ai_player.pits.StonePits
                temp_list.reverse()
                print(*temp_list, sep=" | ")
                print(str(self.ai_player.kalaha.score) + "                   " + str(self.human_player.kalaha.score))
                print(*self.human_player.pits.StonePits, sep=" | ")
                print("#####################")
                print(self.list_available_pits())

            else:
                print("     Game board      ")
                print("   Computer's turn   ")
                print("#####################")
                temp_list = self.human_player.pits.StonePits
                temp_list.reverse()
                print(*temp_list, sep=" | ")
                print(str(self.human_player.kalaha.score) + "                   " + str(self.ai_player.kalaha.score))
                print(*self.ai_player.pits.StonePits, sep=" | ")
                print("#####################")
                print(self.list_available_pits())

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
            game_winner = BoardPositions.Player.name
        return self.human_player.kalaha.score, self.ai_player.kalaha.score, game_winner
