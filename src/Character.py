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

    def speak(self):
        return str("Hi I'm " + self.name + " and my stats are: " + str(self.stats))

    def level_up(self, max_level):
        if self.level < max_level:
            self.level = + 1
