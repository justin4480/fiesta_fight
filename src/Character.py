class Character:

    """
    Base Character Object
    """

    MAX_LEVEL = 10

    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
        self.health = 100
        self.level = 1

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_stats(self):
        return self.stats

    def get_health(self):
        return self.health

    def injure(self, hit_amount):
        self.health -= hit_amount

    def respawn(self):
        self.health = 100

    def level_up(self, max_level):
        if self.level < max_level:
            self.level = + 1
