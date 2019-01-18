from src.CharacterUniverse import CharacterUniverse


class Game:

    def __init__(self):
        self.score = 0
        self.characters = CharacterUniverse()
        self.player = self.characters.get_character()
        self.ai = self.characters.get_character()

    def run(self):
        print(
            'Health', '[', '*' * int(self.player.get_health()/5), ']',
            self.print_buffer(50),
            'Health', '[', '*' * int(self.player.get_health()/5), ']',
        )
        print(self.player.get_name(), '(Player)', self.print_buffer(18), self.ai.get_name(), '(AI)')

    def print_buffer(self, subtract):
        name_length = len(self.player.get_name()) + len(self.ai.get_name())
        return str(' ' * (80 - name_length - subtract))
