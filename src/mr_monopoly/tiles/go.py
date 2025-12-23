from .tile import Tile
from ..player import Player
from ..board_context import BoardContext


class Go(Tile):
    def visit_side_effect(self, player: Player, board_context: BoardContext) -> None:
        _, _ = player, board_context

    def pass_side_effect(self, player: Player, board_context: BoardContext) -> None:
        _ = board_context  # Unused
        player.credit(200)
