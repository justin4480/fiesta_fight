import random
import pandas as pd
from src.Character import Character


class Game:

    def __init__(self):
        self.score = 0
        self.characters = generate_pokemon_characters()

    def run(self):
        characters = generate_pokemon_characters()

        for i in range(10):
            print(characters[i].speak())


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


def generate_pokemon_characters():

    pokemon_names = pd.read_csv("assets/pokemon_names.txt", sep='\n').values.tolist()
    character_list = []

    for name in pokemon_names:
        character_list.append(Character(name[0], generate_random_stats()))

    random.shuffle(character_list)

    return character_list
