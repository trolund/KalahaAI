from AI.AIController import AIController
from AI.RandomAgent import RandomAgent
from Game import GameLogic
from Entities.State import State
import time
import sys


class GameController:
    bool_default = 1
    state = State(True)
    game_board = None
    ai1_difficulty = 0  # Default mini-max
    ai2_difficulty = 0
    depth1 = 3
    depth2 = 3
    aiController = None
    aiController2 = None
    aiController3 = None

    def initial_setup(self):
        self.bool_default = int(input(
            "Welcome to Kalaha.\nPlease enter '1' for a default game (Human player vs AI), or enter '0' for AI vs AI.\n"))

        if self.bool_default == 0:  # custom setup
            print("Custom game selected. Please walk through the initial game setup: ")
            self.ai1_difficulty = int(
                input("Please enter '0' for Minimax without alpha-beta pruning and '1' for Minimax with "
                      "alpha-beta pruning for AI1: "))
            self.ai2_difficulty = int(
                input("Please enter '0' for Minimax without alpha-beta pruning and '1' for Minimax with "
                      "alpha-beta pruning for AI2: "))
            self.depth1 = int(input("Enter depth for AI1 (preferably somewhere around 1-7): "))
            self.depth2 = int(input("Enter depth for AI2 (preferably somewhere around 1-7): "))

            print("Setting up game...")
        else:  # Player vs a.i
            print("Default game selected. Please walk through the initial game setup: ")
            self.ai1_difficulty = int(input("Please enter '0' for mini-max without pruning and '1' for mini-max with "
                                            "pruning for AI: "))
            self.depth1 = int(input("Enter depth for AI (preferably somewhere around 1-7): "))
            print("Default game selected. Setting up game...")

        self.aiController = AIController(self.depth1)
        self.aiController2 = AIController(self.depth2)
        self.aiController3 = RandomAgent()

    def game_loop(self):
        GameLogic.print_state(self.state)
        player1_counter = 0
        player1_sum = 0
        player2_counter = 0
        player2_sum = 0

        while not GameLogic.game_finished(self.state):
            if self.bool_default == 1:  # If default game is selected, shift between player and AI
                if self.state.human_turn:
                    self.state = GameLogic.new_state(self.state, int(input("Please enter desired pit to move: ")))
                else:
                    if self.ai1_difficulty == 0:  # If mini-max is selected run this
                        self.state = GameLogic.new_state(self.state, self.aiController.mini_max(self.state))
                    else:  # Otherwise run alpha_beta
                        self.state = GameLogic.new_state(self.state, self.aiController.alpha_beta_search(self.state))
            elif self.bool_default == 0:  # AI vs AI is selected
                if self.state.human_turn:
                    start = time.monotonic_ns()
                    if self.ai1_difficulty == 0:  # If mini-max is selected run this
                        self.state = GameLogic.new_state(self.state, self.aiController.mini_max(self.state))
                    else:  # Otherwise run alpha_beta
                        self.state = GameLogic.new_state(self.state, self.aiController.alpha_beta_search(self.state))
                    end = time.monotonic_ns()
                    player1_counter += 1
                    player1_sum += (end - start) / 1000000

                else:
                    start = time.monotonic_ns()
                    if self.ai2_difficulty == 0:  # If mini-max is selected run this
                        self.state = GameLogic.new_state(self.state, self.aiController2.mini_max(self.state))
                    else:  # Otherwise run alpha_beta
                        self.state = GameLogic.new_state(self.state, self.aiController2.alpha_beta_search(self.state))
                    end = time.monotonic_ns()
                    player2_counter += 1
                    player2_sum += (end - start) / 1000000
            else:
                print("Input not recognised. Closing program!")
                sys.exit()

            GameLogic.print_state(self.state)

        if self.bool_default == 0:
            print("Player1 average time per turn: " + str(player1_sum / player1_counter))
            print("Player2 average time per turn: " + str(player2_sum / player2_counter))
            print("Number of moves: " + str(player1_counter + player2_counter))
