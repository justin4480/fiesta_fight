from src.CharacterUniverse import CharacterUniverse
from src.Battle import Battle
from src.Player import Player


class Game:

    def __init__(self, player_name):
        self.character_universe = CharacterUniverse()
        self.player1 = Player(player_name)
        self.player2 = Player('Bot')

    def run(self):

        self.player1.assign_character(self.character_universe.get_character())

        running_state = True

        while running_state:

            self.player2.assign_character(self.character_universe.get_character())

            print(self.player1.print_player_stats())
            print(self.player2.print_player_stats())

            user_input = input('\n (b)attle, (r)un or (q)uit: ')

            # Exit game
            if user_input == 'q':
                running_state = False

            # Battle
            elif user_input == 'b':
                battle = Battle(self.player1, self.player2)
                battle.begin()
                input('Press any key to continue')
