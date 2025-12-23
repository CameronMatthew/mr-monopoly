from typing import Annotated

from pydantic import BaseModel, Field

from mr_monopoly.config import STARTING_BALANCE
from mr_monopoly.exceptions import IllegalMoveError

from ._fields import MoneyField, PositionField
from .tiles import Tiles, OwnableTile


class InsufficientFundsError(IllegalMoveError):
    """Raised when a player attempts to perform an action without sufficient funds."""

    pass


class Player(BaseModel):
    name: str
    balance: Annotated[MoneyField, Field(default=STARTING_BALANCE)]
    position: PositionField
    tiles: Tiles[OwnableTile]

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        return self.name == other.name

    def _has_sufficient_funds(self, amount: MoneyField) -> bool:
        return self.balance > amount

    def _check_sufficient_funds(self, amount: MoneyField) -> None:
        if not self._has_sufficient_funds(amount):
            raise InsufficientFundsError(
                f"Player {self.name} has insufficient funds for this action."
            )

    def debit(self, amount: MoneyField) -> None:
        self._check_sufficient_funds(amount)
        self.balance -= amount

    def credit(self, amount: MoneyField) -> None:
        self.balance += amount

    def transfer(self, recipient: "Player", amount: MoneyField) -> None:
        self._check_sufficient_funds(amount)
        self.debit(amount)
        recipient.credit(amount)

    def teleport(self, new_position: PositionField) -> None:
        self.position = new_position
