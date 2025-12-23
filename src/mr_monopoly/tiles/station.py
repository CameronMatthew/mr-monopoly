from mr_monopoly.exceptions import GameError

from .ownable_tile import OwnableTile
from .._fields import MoneyField
from ..board_context import BoardContext
from ..player import Player
from ..roll import RollResult


class InvalidStationConfig(GameError):
    pass


class Station(OwnableTile):
    name: str
    rent: list[MoneyField]

    @classmethod
    def rename(cls, name: str, station: "Station") -> "Station":
        return cls(name=name, rent=station.rent, purchase_price=station.purchase_price)

    def _get_rent(self, owned_stations: int) -> MoneyField:
        idx = owned_stations - 1
        if idx >= len(self.rent):
            raise IndexError("Rent index out of range for stations.")

        return self.rent[idx]

    def _check_rent(self, board_context: BoardContext) -> None:
        values = len(self.rent)
        if values != board_context.utility_count:
            raise InvalidStationConfig(
                f"Expected {board_context.utility_count} rent values, got {values}"
            )

    def visit_side_effect(
        self, player: Player, board_context: BoardContext, last_roll: RollResult
    ) -> None:
        del last_roll  # Unused

        self._check_rent(board_context)
        if self.is_available():
            return

        if self.is_owner(player):
            return

        owner = self.fetch_owner()
        owned_stations = owner.tiles.station_count()
        rent = self._get_rent(owned_stations)

        player.transfer(owner, rent)
