from GameState import Board


class GameLogic:

    def game_ended(self, board):
        if any(board.state[8:]) == False or any(board.state[1:7]) == False:
            return True
        return False

    def move(self, board, n):
        print(board, n)
        # operations on board
        # return new state
        return board

    def game_loop(self, initial_board=None, player_starts=True):
        board = Board()

         # set init board state if a states is given
        if initial_board is not None:
            board.board = initial_board

        # print init state
        board.print()

        # main game loop
        while 1:
            # player makes move
            if player_starts:
                move = input("Enter bucket number: ")
                board = self.move(board, move)
            # AI makes move
            else:
                print("no move")

            # check if the game is over
            if self.game_ended(board):
                print("Games ended!")
                print("AI : " + board.get_ai_score())
                print("Player : " + board.get_player_score())
                break

