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

    stats = {}

    stats["Attack"] = randint(5, 10)
    stats["Defense"] = 15 - stats["Attack"]

    return stats
