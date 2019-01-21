from src.Game import Game


def main():

    player_name = input('Player 1, enter your name: ')
    game = Game(player_name)
    game.run()


if __name__ == "__main__":
    main()
