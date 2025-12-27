from pydantic import BaseModel

from .._fields import DisplacementField
from ..player import Player
from ..board_context import BoardContext
from ..board import Board
from ..roll import RollResult
from ..transport_mode import TransportMode


class Tile(BaseModel):
    def visit_side_effect(
        self, player: Player, board_context: BoardContext, last_roll: RollResult
    ) -> None:
        del player, board_context, last_roll

    def pass_side_effect(
        self, player: Player, board_context: BoardContext, roll: RollResult
    ) -> None:
        del player, board_context, roll

    def transport_effect(self, player: Player, board: Board) -> tuple[TransportMode, DisplacementField]:
        del player, board
        return TransportMode.HOP, 0
