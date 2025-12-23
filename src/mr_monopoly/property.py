from mr_monopoly.exceptions import IllegalMoveError
from mr_monopoly.config import MAX_HOUSES_PER_PROPERTY, MAX_HOTELS_PER_PROPERTY

from .property_type import PropertyType


class TooManyPropertiesError(IllegalMoveError):
    pass


class Property:
    def __init__(self) -> None:
        self._houses = 0
        self._hotels = 0

    def build_property(self) -> PropertyType:
        property_type = self._next_property_type()
        match property_type:
            case PropertyType.HOUSE:
                self._houses += 1
                self._hotels = 0
            case PropertyType.HOTEL:
                self._hotels += 1
                self._houses = 0
            case None:
                raise TooManyPropertiesError(
                    "Cannot build more properties on this plot"
                )
            
        return property_type

    def _next_property_type(self) -> PropertyType | None:
        if self._hotels >= MAX_HOTELS_PER_PROPERTY:
            return None

        if self._houses < MAX_HOUSES_PER_PROPERTY and self._hotels == 0:
            return PropertyType.HOUSE

        if self._houses >= MAX_HOUSES_PER_PROPERTY:
            return PropertyType.HOTEL

        return PropertyType.HOTEL
    
    @property
    def houses(self) -> int:
        return self._houses
    
    @property
    def hotels(self) -> int:
        return self._hotels
