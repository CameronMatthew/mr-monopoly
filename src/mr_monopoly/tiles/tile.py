from abc import ABC, abstractmethod

from pydantic import BaseModel

from ..player import Player
from ..board_context import BoardContext


class Tile(BaseModel, ABC):
    @abstractmethod
    def visit_side_effect(self, player: Player, board_context: BoardContext) -> None:
        pass

    def pass_side_effect(self, player: Player, board_context: BoardContext) -> None:
        _, _ = (
            player,
            board_context,
        )  # Most tiles don't have a pass side effect so we default to noop
