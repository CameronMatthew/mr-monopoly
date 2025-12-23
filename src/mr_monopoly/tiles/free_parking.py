from mr_monopoly.board_context import BoardContext
from mr_monopoly.player import Player
from mr_monopoly.roll import RollResult
from .tile import Tile


class FreeParking(Tile):
    def visit_side_effect(
        self, player: Player, board_context: BoardContext, last_roll: RollResult
    ) -> None:
        del player, board_context, last_roll
