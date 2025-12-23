from .ownable_tile import OwnableTile
from .._fields import MoneyField
from ..board_context import BoardContext
from ..player import Player
from ..roll import RollResult


class Station(OwnableTile):
    name: str
    rent: list[MoneyField]

    def _get_rent(self, owned_utilities: int) -> MoneyField:
        idx = owned_utilities - 1
        if idx >= len(self.rent):
            raise IndexError("Rent index out of range for utilities.")

        return self.rent[idx]

    def visit_side_effect(
        self, player: Player, board_context: BoardContext, last_roll: RollResult
    ) -> None:
        del board_context, last_roll  # Unused
        if self.is_available():
            return

        if self.is_owner(player):
            return

        owner = self.fetch_owner()
        owned_utilities = owner.utility_count()
        rent = self._get_rent(owned_utilities)

        player.transfer(owner, rent)
