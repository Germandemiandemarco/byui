class Player:
    """to keep track of their identity and last move.
    
    Attributes:
        _name (string of name): The player's name.
        _move (instance of Move): The player's last move.
    """
    def __init__(self, name):

        self._nameplayer = name
        self._move = None
        
    def get_move(self):
        """Returns the player's last move (an instance of Move). If the player 
        hasn't moved yet this method returns None.

        """
        return self._move
        
    def set_move(self, move):
        """Sets the player's last move to the given instance of Move.

        Args:
            move (Move): an instance of Move
        """
        self._move = move

    def get_name(self):
        """Returns the player's name.

        Args:
            self (Player): an instance of Player.
        """
        return self._nameplayer

