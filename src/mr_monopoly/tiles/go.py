from .tile import Tile
from ..player import Player
from ..board_context import BoardContext
from ..roll import RollResult


class Go(Tile):
    def visit_side_effect(
        self, player: Player, board_context: BoardContext, last_roll: RollResult
    ) -> None:
        del player, board_context, last_roll

    def pass_side_effect(
        self, player: Player, board_context: BoardContext, roll: RollResult
    ) -> None:
        del board_context, roll  # Unused
        player.credit(200)
