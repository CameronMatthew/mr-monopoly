class IllegalMoveError(Exception):
    """
    Raised when a player attempts to make an illegal move in the game.
    """

    pass


class GameError(Exception):
    """
    Raised when the game gets itself into an undefined or impossible state somehow.
    """

    pass
