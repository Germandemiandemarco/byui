class Roster:
    """This class keeps track of the players.
    

    Attributes:
        _current (integer): The index of the current player.
        _players (list): A list of Player objects.
    """
    def __init__(self):
 
        self.current = -1
        self.players = []
        
    def add_player(self, player):
        """Adds the given player to the roster
        
        Args:
            self: An instance of Roster.
            player (Player): The player object to add.
        """
        if player not in self.players:
            self.players.append(player)

    def get_current(self):
        """Gets the current player object.
        
        
        Returns:
            Player: The current player.
        """
        return self.players[self.current]
    
    def next_player(self):
        """Advances the turn to the next player.
        
        Args:
            self (Roster): An instance of Roster.
        """
        self.current = (self.current + 1) % len(self.players)
