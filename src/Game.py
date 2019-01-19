from src.CharacterUniverse import CharacterUniverse


class Game:

    def __init__(self):
        self.score = 0
        self.characters = CharacterUniverse()
        self.player1 = self.characters.get_character()
        self.player2 = self.characters.get_character()

    def run(self):
        print(self.print_player_summary(self.player1))
        print(self.print_player_summary(self.player2))

        if input('\n (a)ttack or r(un): ') == 'a':
            while self.player1.get_health() > 0 and self.player2.get_health() > 0:
                self.player2.injure(5)
                print(self.player2.get_health())

    @staticmethod
    def print_player_summary(player):
        return str(
            f"\n Player 2: {player.get_name()}"
            f"\n    Health:  {player.get_health()}%"
            f"\n    Attack:  {player.get_stats()['Attack']}"
            f"\n    Defense: {player.get_stats()['Defense']}"
            f"\n    Stamina: {player.get_stats()['Stamina']}"
        )
