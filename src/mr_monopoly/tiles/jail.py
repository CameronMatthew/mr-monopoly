from .tile import Tile
from ..player import Player
from ..board_context import BoardContext


class Jail(Tile):
    def visit_side_effect(self, player: Player, board_context: BoardContext) -> None:
        _, _ = player, board_context  # Unused parameters
