
class Character:

    """
    Base Character Object
    """

    MAX_LEVEL = 10

    def __init__(self, name, health = 100, level = 1):
        self.name = name
        self.type = type
        self.stats = {'attack':}
        self.skill = {}
        self.health = health
        self.level = level

    def speak(self):
        return str("hello, I'm " + self.name)

    def level_up(self, max_level):
        if self.level < max_level: self.level =+ 1


def main():
    justin = Character("Justin")
    print(justin.speak())


if __name__ == "__main__":
    main()
