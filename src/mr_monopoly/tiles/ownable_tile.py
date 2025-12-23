from mr_monopoly.exceptions import IllegalMoveError

from .tile import Tile
from ..player import Player
from .._fields import MoneyField


class NotOwnerError(IllegalMoveError):
    pass


class AlreadyOwnedError(IllegalMoveError):
    pass


class OwnableTile(Tile):
    purchase_price: MoneyField
    owner: Player | None = None

    def has_owner(self) -> bool:
        return self.owner is not None

    def is_available(self) -> bool:
        return not self.has_owner()

    def fetch_owner(self) -> Player:
        if self.is_available():
            raise NotOwnerError(f"{self} is not owned by any player.")

        assert self.owner is not None  # for mypy
        return self.owner

    def check_available(self) -> None:
        if not self.is_available():
            raise AlreadyOwnedError(
                f"{self} is already owned by {self.fetch_owner().name}."
            )

    def is_owner(self, player: Player) -> bool:
        if self.is_available():
            return False
        return self.owner == player

    def check_ownership(self, player: Player) -> None:
        if not self.is_owner(player):
            raise NotOwnerError(f"Player {player.name} does not own {self}.")

    def buy(self, player: Player) -> None:
        self.check_available()
        player.debit(self.purchase_price)
        self.owner = player

    def sell(self, buyer: Player, price: int) -> None:
        self.check_ownership(buyer)
        buyer.transfer(self.fetch_owner(), price)
        self.owner = buyer
