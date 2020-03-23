from Entities.Player import Player
from Enum.BoardPositions import BoardPositions


class Board:
    human_player = Player("Peter", BoardPositions.PlayerPosition, 4)
    ai_player = Player("AI", BoardPositions.AIPosition, 4)

    human_turn = True
    GameFinished = False

    current_game_state = []

    def change_turn(self):
        if self.human_turn:
            self.human_turn = False
        else:
            self.human_turn = True

    def check_game_end(self):
        if not self.human_player.pits or not self.ai_player.pits:  # In Python, all empty lists are False.
            self.GameFinished = True

    def list_available_pits(self, pits):
        return [i for i, v in enumerate(pits) if v > 0]

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
        self.current_game_state = game_state

    def move_stones(self, pit_number):
        game_state = self.get_current_game_state()
        stone_amount = game_state[pit_number]
        game_state[pit_number] = 0

        while stone_amount > 0:
            pit_number += 1
            if pit_number is 13:
                pit_number = 0
            game_state[pit_number] += 1
            stone_amount -= 1

        self.update_game_state(game_state)
        self.change_turn()

    def get_game_score(self):
        if self.ai_player.kalaha > self.human_player.kalaha:
            game_winner = BoardPositions.AIPosition
        else:
            game_winner = BoardPositions.PlayerPosition
        return self.human_player.kalaha, self.ai_player.kalaha, game_winner
