class Battle:

    def __init__(self, player1, player2):
        self.player = {'attacking': player1, 'defending': player2}
        self.last_move = None

    def begin(self):

        if self.player['attacking'].get_name() == 'Bot':
            user_input = 'a'
            # todo - more bot logic here
        else:
            user_input = input('\n (a)ttack, (d)efend or (m)agic: ')

        # Attack
        if user_input == 'a':
            self.player['defending'].injure(
                (
                    100
                    + self.player['attacking'].get_character().get_stats()['attack']
                    - self.player['defending'].get_character().get_stats()['defense']
                ) / 5
            )
            print(self.player['defending'].get_hp())
        # Defend
        elif user_input == 'd':
            pass
        # Magic
        elif user_input == 'm':
            pass
        else:
            print('invalid entry, try again')
