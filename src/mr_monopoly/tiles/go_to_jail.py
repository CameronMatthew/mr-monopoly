from mr_monopoly.exceptions import GameError

from .tile import Tile
from .jail import Jail
from .._fields import DisplacementField, PositionField
from ..player import Player
from ..board import Board
from ..transport_mode import TransportMode


class GoToJailWithNoJailError(GameError):
    pass


class GoToJail(Tile):
    @staticmethod
    def _next_jail_position(current_position: int, board: Board) -> PositionField:
        positions = [position for position, _ in board.tiles.type_filter(Jail)]
        if len(positions) == 0:
            raise GoToJailWithNoJailError("No Jail tile found on the board")

        for position in positions:
            if position > current_position:
                return position

        return positions[0]

    def transport_effect(self, player: Player, board: Board) -> tuple[TransportMode, DisplacementField]:
        current_position = player.position
        jail_position = self._next_jail_position(current_position, board)
        displacement = jail_position - current_position
        return TransportMode.TELEPORT, displacement
