from typing import Annotated

from pydantic import Field

from mr_monopoly.exceptions import IllegalMoveError, GameError

from .ownable_tile import OwnableTile
from ..player import Player
from ..property import Property, PropertyType
from ..colour import Colour
from ..board_context import BoardContext
from .._fields import MoneyField
from ..config import MAX_HOUSES_PER_PROPERTY, MAX_HOTELS_PER_PROPERTY


class NoMonopolyError(IllegalMoveError):
    pass


class ImpossibleBoardContextError(GameError):
    pass


class Plot(OwnableTile):
    name: str
    colour: Colour
    rent: MoneyField
    rent_with_monopoly: MoneyField
    rent_with_houses: Annotated[
        list[MoneyField],
        Field(min_length=MAX_HOUSES_PER_PROPERTY, max_length=MAX_HOUSES_PER_PROPERTY),
    ]
    rent_with_hotels: Annotated[
        list[MoneyField],
        Field(min_length=MAX_HOTELS_PER_PROPERTY, max_length=MAX_HOTELS_PER_PROPERTY),
    ]
    house_price: MoneyField
    hotel_price: MoneyField

    def __post_init__(self) -> None:
        self.property = Property()

    def _owns_monopoly(self, player: Player, board_context: BoardContext) -> bool:
        player_ownerships = player.colour_counts().get(self.colour, 0)
        on_board = board_context.colour_counts.get(self.colour)

        if on_board is None:
            raise ImpossibleBoardContextError(
                "This tile has a colour that isn't on the board"
            )

        if player_ownerships > on_board:
            raise ImpossibleBoardContextError(
                "Somehow a player has more ownerships than tiles on the board"
            )

        return player_ownerships == on_board

    def _check_monopoly(self, player: Player, board_context: BoardContext) -> None:
        if not self._owns_monopoly(player, board_context):
            raise NoMonopolyError("This action requires a monopoly")

    def build_property(self, player: Player, board_context: BoardContext) -> None:
        self._check_monopoly(player, board_context)
        self.check_ownership(player)
        property_type = self.property.build_property()
        match property_type:
            case PropertyType.HOUSE:
                player.debit(self.house_price)
            case PropertyType.HOTEL:
                player.debit(self.hotel_price)

    def visit_side_effect(self, player: Player, board_context: BoardContext) -> None:
        _ = board_context  # Unused parameter
        if self.is_available():
            return

        if not self.is_owner(player):
            if self.property.hotels > 0:
                rent = self.rent_with_hotels[self.property.hotels - 1]
            elif self.property.houses > 0:
                rent = self.rent_with_houses[self.property.houses - 1]
            elif self._owns_monopoly(self.fetch_owner(), board_context):
                rent = self.rent_with_monopoly
            else:
                rent = self.rent

            owner = self.fetch_owner()
            player.transfer(owner, rent)
