from Entities.Board import Board

gameboard = Board()
print("Player stats:")
print(gameboard.human_player.pits.StonePits)
print(gameboard.human_player.kalaha.score)
print("AI stats:")
print(gameboard.ai_player.pits.StonePits)
print(gameboard.ai_player.kalaha.score)

print("Printing gameboard:")

# print(gameboard.get_current_game_state())


gameboard.print()
# gameboard.move_stones(0)


gameboard.move_stones(2)
gameboard.print()
print("Printing gameboard after change:")
print(gameboard.get_current_game_state())

gameboard.move_stones(2)
gameboard.print()
print("Printing gameboard after change:")
print(gameboard.get_current_game_state())
