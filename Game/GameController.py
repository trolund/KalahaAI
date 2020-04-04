from AI.AIController import AIController
from Entities.Board import Board
from Game import GameLogic
from Entities.State import State
import time

class GameController:
    bool_default = 1
    state = State(True)
    game_board = None
    aiController = AIController(7)
    aiController2 = AIController(7)

    def initial_setup(self):
        self.bool_default = int(input(
            "Welcome to Kalaha. Please enter '1' for a default game, or enter '0' for a custom setup.\n"))

        if self.bool_default == 0:
            print("Custom game selected. Please walk through the initial game setup: ")
            player_name = input("Please enter desired player name: ")
            stone_amount_start = int(input("Please enter desired stone amount per pit (default is 4): "))
            ai_difficulty = int(input(
                "Please enter desired AI difficulty ranging from 1 to 3, with 3 being the most difficult: "))

            print("Setting up game...")
            self.game_board = Board(player_name, stone_amount_start, ai_difficulty)

        else:
            print("Default game selected. Setting up game...")
            self.game_board = Board("Human", 4, 3)

    def game_loop(self):
        GameLogic.print_state(self.state)
        player1_counter = 0
        player1_sum = 0
        player2_counter = 0
        player2_sum = 0
        while not GameLogic.game_finished(self.state):

            if self.state.human_turn:
                # self.state = GameLogic.new_state(self.state, int(input("Please enter desired pit to move: ")))
                start = time.monotonic_ns()
                self.state = GameLogic.new_state(self.state, self.aiController.mini_max(self.state))
                end = time.monotonic_ns()
                print("time taken mini-max: " + str((end - start) / 1000000) + "ms")
                player1_counter += 1
                player1_sum += (end - start) / 1000000

            else:
                start = time.monotonic_ns()
                self.state = GameLogic.new_state(self.state, self.aiController2.alpha_beta_search(self.state))
                end = time.monotonic_ns()
                print("time taken alpha-beta: " + str((end - start) / 1000000) + "ms")
                player2_counter += 1
                player2_sum += (end - start) / 1000000

            GameLogic.print_state(self.state)

        print("player1 average: " + str(player1_sum / player1_counter))
        print("player2 average: " + str(player2_sum / player2_counter))


