from .tile import Tile
from ..player import Player
from ..board_context import BoardContext


class Tax(Tile):
    amount: int = 200

    def visit_side_effect(self, player: Player, board_context: BoardContext) -> None:
        _ = board_context  # Unused parameter
        player.debit(self.amount)
