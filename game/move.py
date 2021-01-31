class Move:
    """Move keeps track of the guesses
    

    Attributes:
        _guess (integer): The guess the player makes.

    """

    def __init__(self, guess):
        self._guess = guess
        

    def get_guess(self):
        """ Returns the guess the player makes
        """

        return self._guess
    
