from Game.GameController import GameController
# from Game.TestGameController import TestGameController as TestGameController


def main():
    # Create game controller object
    game_controller = GameController()

    # Create a test game controller object
    # game_controller = TestGameController()

    # Set up game
    game_controller.initial_setup()

    # Play game until win condition
    game_controller.game_loop()


if __name__ == '__main__':
    main()
