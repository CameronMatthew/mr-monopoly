from enum import Enum, auto
from typing import Annotated

from pydantic import Field

from mr_monopoly.exceptions import GameError

from .ownable_tile import OwnableTile
from ..player import Player
from ..board_context import BoardContext
from ..roll import RollResult


class InvalidUtilityConfig(GameError):
    pass


class UtilityType(Enum):
    ELECTRIC_COMPANY = auto()
    WATER_WORKS = auto()


class Utilities(OwnableTile):
    type: UtilityType
    rent_multiplier: list[Annotated[int, Field(gt=0)]]

    def _get_rent_multiplier(self, owned_utilities: int) -> int:
        idx = owned_utilities - 1
        if idx >= len(self.rent_multiplier):
            raise IndexError("Rent index out of range for utilities.")

        return self.rent_multiplier[idx]

    def _check_multipliers(self, board_context: BoardContext) -> None:
        multipliers = len(self.rent_multiplier)
        if multipliers != board_context.utility_count:
            raise InvalidUtilityConfig(
                f"Expected {board_context.utility_count} rent multipliers, got {multipliers}"
            )

    def visit_side_effect(
        self, player: Player, board_context: BoardContext, last_roll: RollResult
    ) -> None:
        self._check_multipliers(board_context)
        if self.is_available():
            return

        if self.is_owner(player):
            return

        owner = self.fetch_owner()
        owned_utilities = owner.tiles.utility_count()
        multiplier = self._get_rent_multiplier(owned_utilities)
        rent = last_roll.total() * multiplier

        player.transfer(owner, rent)
