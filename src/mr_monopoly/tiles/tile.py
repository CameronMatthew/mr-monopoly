from abc import ABC, abstractmethod

from pydantic import BaseModel

from ..player import Player
from ..board_context import BoardContext
from ..roll import RollResult


class Tile(BaseModel, ABC):
    @abstractmethod
    def visit_side_effect(
        self, player: Player, board_context: BoardContext, last_roll: RollResult
    ) -> None:
        pass

    def pass_side_effect(
        self, player: Player, board_context: BoardContext, roll: RollResult
    ) -> None:
        del player, board_context, roll
