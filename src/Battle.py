from random import randint


class Battle:

    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.active_player_toggle = randint(0, 1)

    def begin(self):
        user_input = input('\n (a)ttack, (d)efend or (m)agic: ')

        if user_input == 'a':
            pass
        elif user_input == 'd':
            pass
        elif user_input == 'm':
            pass
        else:
            print('invalid entry, try again')
