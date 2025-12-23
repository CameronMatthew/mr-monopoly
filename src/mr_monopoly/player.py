from typing import Annotated, Iterator, TypeVar

from pydantic import BaseModel, Field

from mr_monopoly.config import STARTING_BALANCE
from mr_monopoly.exceptions import IllegalMoveError

from ._fields import MoneyField
from .tiles import OwnableTile, Plot, Utilities, Station
from .colour import Colour


class InsufficientFundsError(IllegalMoveError):
    """Raised when a player attempts to perform an action without sufficient funds."""

    pass


TileType = TypeVar("TileType", bound=OwnableTile)


class Player(BaseModel):
    name: str
    balance: Annotated[MoneyField, Field(default=STARTING_BALANCE)]
    position: int = 0
    tiles: list[OwnableTile] = []

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        return self.name == other.name

    def _has_sufficient_funds(self, amount: int) -> bool:
        return self.balance > amount

    def _check_sufficient_funds(self, amount: int) -> None:
        if not self._has_sufficient_funds(amount):
            raise InsufficientFundsError(
                f"Player {self.name} has insufficient funds for this action."
            )

    def debit(self, amount: int) -> None:
        self._check_sufficient_funds(amount)
        self.balance -= amount

    def credit(self, amount: int) -> None:
        self.balance += amount

    def transfer(self, recipient: "Player", amount: int) -> None:
        self._check_sufficient_funds(amount)
        self.debit(amount)
        recipient.credit(amount)

    def _tile_filter(self, tile_type: type[TileType]) -> Iterator[TileType]:
        for tile in self.tiles:
            if isinstance(tile, tile_type):
                yield tile

    def colour_counts(self) -> dict[Colour, int]:
        counts: dict[Colour, int] = {}
        for tile in self._tile_filter(Plot):
            colour = tile.colour
            counts[colour] = counts.get(colour, 0) + 1
        return counts

    def utility_count(self) -> int:
        utilities = list(self._tile_filter(Utilities))
        return len(utilities)

    def station_count(self) -> int:
        stations = list(self._tile_filter(Station))
        return len(stations)

    def teleport(self, new_position: int) -> None:
        self.position = new_position
