from game.board import Board
from game.console import Console
from game.move import Move
from game.player import Player
from game.roster import Roster


class Director:
    """This class controls the sequence of the game using objects from the other classes.


    Attributes:
        board: An instance of the class of objects known as Board.
        console: An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        move: An instance of the class of objects known as Move.
        roster: An instance of the class of objects known as Roster.
    """

    def __init__(self):
        """The class constructor.

        Args:
            self (Director): an instance of Director.
        """
        self._board = Board()
        self._console = Console()
        self._keep_playing = True
        self._move = None
        self._roster = Roster()

    def start_game(self):
        self._prepare_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            
    def _prepare_game(self):
        """Gets the player names and adds them to the roster.
        
        """
        for n in range(2):
            name = self._console.read(f"Enter a name for player {n + 1}: ")
            player = Player(name)
            self._roster.add_player(player)  
            
    def _get_inputs(self, hint, code):
        """Gets the inputs at the beginning of each round of play. From each player, get their guess.
        """
        """ displays the game board """
        board = self._board.to_text()
        self._console.write(board)
        
        """ Puts info on the screen to get the player's next move """
        player = self._roster.get_current()
        self._console.write(f"Player {player.get_name()}:")
        guess = self._console.read_number("What is your guess? ")
    
        """ Returns move and puts it in a tuple with the player's guess and their hint, and the actual code.               
        """
        """ instances of move """

        move = Move(guess)
        player.set_move(move, hint, code)
        
    def _do_updates(self):
        """ Updates the board with the current move """
        player = self._roster.get_current()
        move = player.get_move()
        self._board.apply(move)

    def _do_outputs(self):
        "Compares current players guess to code to see if they won."
        player = self._roster.get_current()
        if player.get_guess(self.guess) == Board.code:  #please check this line
            winner = player
            print(f"\n{winner} won!")
            self._keep_playing = False
        self._roster.next_player()
