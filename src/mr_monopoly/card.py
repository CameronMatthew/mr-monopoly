from .player import Player
from .board_context import BoardContext
from ._fields import DisplacementField
from .transport_mode import TransportMode


class Card:

    def side_effect(self, player: Player, board_context: BoardContext) -> None:
        del player, board_context

    def transport_effect(self, player: Player, board_context: BoardContext) -> tuple[TransportMode, DisplacementField]:
        del player, board_context
        return TransportMode.HOP, 0
