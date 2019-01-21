class Character:

    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_stats(self):
        return self.stats

    def use_magic(self):
        pass

    def attack(self):
        pass

    def defend(self):
        pass
