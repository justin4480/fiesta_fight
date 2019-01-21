from src.CharacterUniverse import CharacterUniverse
from src.Battle import Battle


class Game:

    def __init__(self):
        self.score = 0
        self.characters = CharacterUniverse()
        self.player1 = self.characters.get_character()
        self.player2 = self.characters.get_character()

    def run(self):

        running_state = True

        while running_state:
            self.characters.return_character(self.player2)  # return character to the stack
            self.player2 = self.characters.get_character()  # take a new character

            print(self.print_player_summary(self.player1, 'Player 1'))
            print(self.print_player_summary(self.player2, 'Player 2'))

            user_input = input('\n (b)attle, (r)un or (q)uit: ')

            # Exit game
            if user_input == 'q':
                running_state = False

            # Battle
            elif user_input == 'b':
                battle = Battle(self.player1, self.player2)
                battle.begin()
                input('Press any key to continue')

    @staticmethod
    def print_player_summary(player, player_name):
        return str(
            f"\n {player_name}: {player.get_name()}"
            f"\n    Level:   {player.get_level()}"
            f"\n    HP:      {player.get_hp()}"
            f"\n    MP:      {player.get_mp()}"
            f"\n    Attack:  {player.get_stats()['Attack']}"
            f"\n    Defense: {player.get_stats()['Defense']}"
        )
