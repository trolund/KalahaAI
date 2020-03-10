from GameState import Board

class GameLogic:

    def game_ended(self, board):
        if any(board.state[8:]) == False or any(board.state[1:7]) == False:
            return True
        return False

    def move(self, board, n, realplayer):
        iterator = n
        # operations on board
        if realplayer:
            bucket_count = board.state[n];
            while not bucket_count == 0:
                if iterator == board.AI_SCORE:
                    iterator = iterator + 1
                else:
                    board.state[iterator] = board.state[iterator] + 1
                    iterator = iterator + 1
                    bucket_count = bucket_count - 1

        # return new state
        return board, True

    def next(self, i):
        if i == 6:
            i = 0
        else

    @staticmethod
    def get_input():
        current_move = -1
        while not (0 < current_move < 7):
            current_move = int(input("Enter bucket number: "))
            if not (0 < current_move < 7):
                print("Please enter a number between 1 and 6")

        return current_move

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
                has_move = True
                while has_move:
                    move = self.get_input()
                    board, one_more_move = self.move(board, move, True)
                    has_move = one_more_move
            # AI makes move
            else:
                print("no move")

            # check if the game is over
            if self.game_ended(board):
                print("Games ended!")
                print("AI : " + board.get_ai_score())
                print("Player : " + board.get_player_score())
                break

