from GameState import Board

class GameLogic:

    def move(self, board, n, realplayer):
        # operations on board
        move_again, i = self.one_step(board, n, realplayer)
        if realplayer:
            if board.state[i] == 1 and (7 > i > 0):
                self.get_opposite_points(n, board, realplayer)
                move_again = False
        else:
            if board.state[i] == 1 and (13 > i > 7):
                self.get_opposite_points(n, board, realplayer)
                move_again = False

        return board, move_again

    def one_step(self, board, n, realplayer):
        move_again = False
        hand_count = board.state[n]
        board.state[n] = 0
        i = self.next_bucket(n) # ungå at smide kule i samme pit som man tager fra.
        while not hand_count == 0:
            board.state[i] = board.state[i] + 1
            hand_count = hand_count - 1

            if i == board.PLAYER_SCORE and realplayer:
                move_again = True
            if i == board.AI_SCORE and not realplayer:
                move_again = True

            i = self.next_bucket(i)



        return move_again, i;

    def next_bucket(self, current_bucket):
        if current_bucket == 13:
            return 0
        else:
            return current_bucket + 1

    def get_opposite_points(self, n, board, realplayer):
        if n != board.PLAYER_SCORE or n != board.AI_SCORE:
            pos = 14 - n

            if realplayer:
                board.state[board.PLAYER_SCORE] = board.state[board.PLAYER_SCORE] + board.state[pos]
            else:
                board.state[board.AI_SCORE] = board.state[board.AI_SCORE] + board.state[pos]

            board.state[pos] = 0

    @staticmethod
    def get_input(realplayer, board):
        current_move = -1
        if realplayer:
            while not (0 < current_move < 7) or board.state[current_move] == 0:
                if board.state[current_move] == 0:
                    print("You can not choose a bucket with 0 stones.")
                current_move = int(input("Real player, enter bucket number: "))
                if not (0 < current_move < 7):
                    print("Please enter a number between 1 and 6")
        else:
            while not (7 < current_move < 14) or board.state[current_move] == 0:
                if board.state[current_move] == 0:
                    print("You can not choose a bucket with 0 stones.")
                current_move = int(input("AI, enter bucket number: "))
                if not (7 < current_move < 14):
                    print("Please enter a number between 7 and 13")

        return current_move

    def game_loop(self, initial_board=None, player_starts=True):
        board = Board()

         # set init board state if a states is given
        if initial_board is not None:
            board.board = initial_board

        # print init state
        board.print(self.game_ended(board))

        # main game loop
        while 1:
            # player makes move
            if player_starts:
                has_move = True
                while has_move:
                    move = self.get_input(True, board)
                    board, has_move = self.move(board, move, True)
                    player_starts = False
                    board.print(self.game_ended(board))
            # AI makes move
            else:
                has_move = True
                while has_move:
                    move = self.get_input(False, board)
                    board, has_move = self.move(board, move, False)
                    player_starts = True
                    board.print(self.game_ended(board))



            # check if the game is over
            if self.game_ended(board):
                print("Games ended!")
                break


    def game_ended(self, board):
        if any(board.state[8:]) == False or any(board.state[1:7]) == False:
            return True
        return False
