from mr_monopoly.exceptions import IllegalMoveError, GameError

from .ownable_tile import OwnableTile
from ..player import Player
from ..property import Property
from ..colour import Colour
from ..board_context import BoardContext


class NotOwnerError(IllegalMoveError):
    pass


class AlreadyOwnedError(IllegalMoveError):
    pass


class NoMonopolyError(IllegalMoveError):
    pass


class ImpossibleBoardContextError(GameError):
    pass


class Plot(OwnableTile):
    name: str
    colour: Colour
    property: Property

    def _owns_monopoly(self, player: Player, board_context: BoardContext) -> bool:
        player_ownerships = player.colour_counts().get(self.colour, 0)
        on_board = board_context.colour_counts.get(self.colour)

        if on_board is None:
            raise ImpossibleBoardContextError("This tile has a colour that isn't on the board")
        
        if player_ownerships > on_board:
            raise ImpossibleBoardContextError("Somehow a player has more ownerships than tiles on the board")

        return player_ownerships == on_board
    
    def _check_monopoly(self, player: Player, board_context: BoardContext) -> None:
        if not self._owns_monopoly(player, board_context):
            raise NoMonopolyError("This action requires a monopoly")

    def build_property(self, player: Player, board_context: BoardContext) -> None:
        self._check_monopoly(player, board_context)
        self.check_ownership(player)
        self.property.build_property(player)

    def visit_side_effect(self, player: Player, board_context: BoardContext) -> None:
        _ = board_context  # Unused parameter
        if self.is_available():
            return

        if not self.is_owner(player):
            rent = self.property.rent()
            player.transfer(self.fetch_owner(), rent)
