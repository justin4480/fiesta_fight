class Player:

    def __init__(self, player_name):
        self.player_name = player_name
        self.character = None
        self.level = 1
        self.hp = 100
        self.mp = 1
        self.win_record = {'win': 0, 'lose': 0}
        self.score = 0

    def get_name(self):
        return self.player_name

    def get_character(self):
        return self.character

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_win_record(self):
        return self.win_record

    def assign_character(self, character):
        self.character = character

    def injure(self, hit):
        self.hp -= hit

    def print_player_stats(self):
        return str(
            f"\n Player: {self.get_name()}"
            f"\n    Character: {self.character.get_name()}"
            f"\n    MP:        {self.get_mp()}"
            f"\n    Attack:    {self.character.get_stats()['attack']}"
            f"\n    Defense:   {self.character.get_stats()['defense']}"
        )
