from typing import Annotated

from pydantic import BaseModel, Field

from mr_monopoly.exceptions import IllegalMoveError
from mr_monopoly.config import MAX_HOUSES_PER_PROPERTY, MAX_HOTELS_PER_PROPERTY

from .player import Player
from .property_type import PropertyType
from ._fields import MoneyField


class TooManyPropertiesError(IllegalMoveError):
    pass


class Property(BaseModel):
    house_price: MoneyField
    hotel_price: MoneyField
    base_rent: MoneyField
    hotel_rent: Annotated[
        list[MoneyField],
        Field(min_length=MAX_HOTELS_PER_PROPERTY, max_length=MAX_HOTELS_PER_PROPERTY),
    ]
    house_rent: Annotated[
        list[MoneyField],
        Field(min_length=MAX_HOUSES_PER_PROPERTY, max_length=MAX_HOUSES_PER_PROPERTY),
    ]

    def __post__init__(self) -> None:
        self._houses = 0
        self._hotels = 0

    def build_property(self, player: Player) -> None:
        match self.next_property_type():
            case PropertyType.HOUSE:
                player.debit(self.house_price)
                self._houses += 1
                self._hotels = 0
            case PropertyType.HOTEL:
                player.debit(self.hotel_price)
                self._hotels += 1
                self._houses = 0
            case None:
                raise TooManyPropertiesError(
                    "Cannot build more properties on this plot"
                )

    def next_property_type(self) -> PropertyType | None:
        if self._hotels >= MAX_HOTELS_PER_PROPERTY:
            return None

        if self._houses < MAX_HOUSES_PER_PROPERTY and self._hotels == 0:
            return PropertyType.HOUSE

        if self._houses >= MAX_HOUSES_PER_PROPERTY:
            return PropertyType.HOTEL

        return PropertyType.HOTEL

    def rent(self) -> int:
        if self._hotels > 0:
            return self.hotel_rent[self._hotels - 1]
        if self._houses > 0:
            return self.house_rent[self._houses - 1]
        return self.base_rent
