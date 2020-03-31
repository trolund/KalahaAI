from Game.GameController import GameController


def main():
    # Create game controller object
    game_controller = GameController()

    # Set up game
    game_controller.initial_setup()

    # Play game until win condition
    game_controller.game_loop()


if __name__ == '__main__':
    main()
