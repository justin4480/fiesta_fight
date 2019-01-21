class Character:

    """
    Base Character Object
    """

    MAX_LEVEL = 10
    MAX_MP = 100

    def __init__(self, name, stats):
        self.name = name
        self.level = 1
        self.hp = 100     # hit points
        self.mp = 5       # magic points
        self.stats = stats

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_stats(self):
        return self.stats

    def level_up(self, max_level):
        if self.level < max_level:
            self.level += 1

    # Battle methods

    def use_magic(self):
        pass

    def attack(self):
        pass

    def defend(self):
        pass

    def injure(self, hit_amount):
        self.hp -= hit_amount

    def respawn(self):
        self.hp = 100
