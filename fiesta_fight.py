import random
import pandas as pd


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

    def speak(self):
        return str("hello, I'm " + self.name)

    def level_up(self, max_level):
        if self.level < max_level: self.level =+ 1


def main():

    def generate_random_stats():
        rand_numbers = []
        for _ in range(3-1):
            rand_numbers.append(random.randint(0, 15-sum(rand_numbers)))
            random.shuffle(rand_numbers)

        rand_numbers.append(15 - sum(rand_numbers))

        return {
            'attack': rand_numbers[0],
            'defense': rand_numbers[1],
            'stamina': rand_numbers[2]
        }

    tom = Character("tom", generate_random_stats())
    print(tom.speak())

    jerry = Character("jerry", {'attack': 5, 'defense': 5, 'stamina': 5})
    print(jerry.speak())

    itchy = Character("itchy", {'attack': 5, 'defense': 5, 'stamina': 5})
    print(itchy.speak())

    scratchy = Character("scratchy", {'attack': 5, 'defense': 5, 'stamina': 5})
    print(scratchy.speak())


if __name__ == "__main__":
    main()
