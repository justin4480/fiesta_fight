from src.Character import Character
from random import shuffle, randint
import pandas as pd


class CharacterUniverse:

    def __init__(self):

        pokemon_names = pd.read_csv("assets/pokemon_names.txt", sep='\n').values.tolist()
        self.character_list = []

        for name in pokemon_names:
            self.character_list.append(Character(name[0], generate_random_stats()))

    def get_character(self):
        shuffle(self.character_list)
        return self.character_list.pop()

    def return_character(self, character):
        self.character_list.append(character)


def generate_random_stats():
    rand_numbers = []
    for _ in range(3 - 1):
        rand_numbers.append(randint(0, 15 - sum(rand_numbers)))
        shuffle(rand_numbers)

    rand_numbers.append(15 - sum(rand_numbers))

    return {
        'attack': rand_numbers[0],
        'defense': rand_numbers[1],
        'stamina': rand_numbers[2]
    }
