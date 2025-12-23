from .tile import Tile
from ..player import Player
from ..board_context import BoardContext
from ..roll import RollResult


class GoToJail(Tile):
    def visit_side_effect(
        self, player: Player, board_context: BoardContext, last_roll: RollResult
    ) -> None:
        del last_roll  # Unused
        relevant_jail = board_context.next_jail_location(player.position)
        player.teleport(relevant_jail)
