from Entities.Player import Player
from Enum.BoardPositions import BoardPositions


class Board:
    human_player = Player("Peter", BoardPositions.PlayerPosition)
    ai_player = Player("AI", BoardPositions.AIPosition)

    humanTurn = True
    GameFinished = False

    pit_amount = 6

    def change_turn(self):
        if self.humanTurn:
            self.humanTurn = False
        else:
            self.humanTurn = True

    def check_game_end(self):
        if not self.human_player.pits or not self.ai_player.pits:  # In Python, all empty lists are False.
            self.GameFinished = True

    def list_available_pits(self, pits):
        return [i for i, v in enumerate(pits) if v > 0]

    def get_active_player(self):  # Get active player's identity.
        if self.humanTurn:
            return BoardPositions.PlayerPosition
        else:
            return BoardPositions.AIPosition

    def move_stones(self, pit_number):
        pit_side = self.get_active_player()
        if pit_side == BoardPositions.PlayerPosition:
            stone_amount = self.human_player.pits[pit_number]
        else:
            stone_amount = self.ai_player.pits[pit_number]

        if pit_side == BoardPositions.PlayerPosition:  # Case human player
            if stone_amount >= len(
                    self.human_player.pits.StonePits) - pit_number + 1:  # Case A: Amount of stones smaller/equal to remaining pits
                self.human_player.pits.StonePits[pit_number] = 0
                for i in self.human_player.pits:
                    self.human_player.pits[i] += 1
            elif stone_amount == len(
                    self.human_player.pits.StonePits) - pit_number + 1 + 1:  # Case B: Amount of stones equal to remaining pits + 1
                self.human_player.pits.StonePits[pit_number] = 0
                for i in self.human_player.pits:
                    self.human_player.pits[i] += 1
                self.human_player.kalaha += 1
            else:  # Case C: Amount of stones exceeds remaining pits, moves to opponents side.
                self.human_player.pits.StonePits[pit_number] = 0
                for i in range(self.human_player.pits[pit_number], self.pit_amount):
                    self.human_player.pits[i] += 1
                    stone_amount -= 1
                self.human_player.kalaha += 1
                for i in range(self.ai_player.pits[0], self.ai_player.pits[stone_amount]):
                    self.ai_player.pits[i] += 1

        if pit_side == BoardPositions.AIPosition:  # Case ai player
            if stone_amount <= len(
                    self.ai_player.pits.StonePits) - pit_number + 1:  # Case A: Amount of stones smaller/equal to remaining pits
                self.ai_player.pits.StonePits[pit_number] = 0
                self.ai_player.pits[pit_number:] += 1
            elif stone_amount == len(self.ai_player.pits.StonePits) - (
                    pit_number + 1) + 1:  # Case B: Amount of stones equal to remaining pits + 1
                self.ai_player.pits.StonePits[pit_number] = 0
                self.ai_player.pits[pit_number:] += 1
                self.ai_player.kalaha += 1
            else:  # Case C: Amount of stones exceeds remaining pits, moves to opponents side.
                self.ai_player.pits.StonePits[pit_number] = 0

                for i in range(self.ai_player.pits[pit_number], self.pit_amount):
                    self.ai_player.pits[pit_number:] += 1
                    stone_amount -= 1
                self.ai_player.kalaha += 1
                for i in range(self.human_player.pits[0], self.human_player.pits[stone_amount]):
                    self.human_player.pits[i] += 1

    def get_game_score(self):
        if self.ai_player.kalaha > self.human_player.kalaha:
            game_winner = BoardPositions.AIPosition
        else:
            game_winner = BoardPositions.PlayerPosition
        return self.human_player.kalaha, self.ai_player.kalaha, game_winner
