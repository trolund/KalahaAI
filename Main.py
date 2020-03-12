from GameState import Board
from GameLogic import GameLogic

if __name__ == '__main__':
    game_logic = GameLogic()
    print("Let the game begin!")
    print("-------------------")
    board = Board()
    print("init state:")
    game_logic.game_loop(board, True)



