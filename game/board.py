

import random


class Board:

    def __init__(self):
        self._prepare()
        self.hint = "****"
        self.guess = "----"
        

        

    
    def _prepare(self, player):

"""
    Comments belong here
"""
        name = player.get_name()
        code = str(random.randint(1000, 10000))
        self._items[name] = [code, guess, hint]
    
    def _create_hint(self, code, guess):

"""
    Comments belong here
"""
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return self.hint
    
    def apply(self, move):
        """
        This method will apply the move to the board by using the Move class
        """
        guess = move.get_guess
        self.hint = self._create_hint(guess)
    
    def to_text(self):
        """
        This method will take the information from the move and convert it to text the user will see
        """
        text =  "\n--------------------"
        for player in Roster.players: # i am not sure about this line
            text += (f"\n Player: " + {player} + ": " + {self._create_hint})
        text += "\n--------------------"

