from src.CharacterUniverse import CharacterUniverse


class Game:

    def __init__(self):
        self.score = 0
        self.characters = CharacterUniverse()
        self.player1 = self.characters.get_character()
        self.player2 = self.characters.get_character()

    def run(self):

        print(
            f"\n Player 1: {self.player1.get_name()}"
            f"\n    Health:  {self.player1.get_health()}%"
            f"\n    Attack:  {self.player1.get_stats()['Attack']}"
            f"\n    Defense: {self.player1.get_stats()['Defense']}"
            f"\n    Stamina: {self.player1.get_stats()['Stamina']}"
        )
        print(
            f"\n Player 2: {self.player2.get_name()}"
            f"\n    Health:  {self.player2.get_health()}%"
            f"\n    Attack:  {self.player2.get_stats()['Attack']}"
            f"\n    Defense: {self.player2.get_stats()['Defense']}"
            f"\n    Stamina: {self.player2.get_stats()['Stamina']}"
        )
