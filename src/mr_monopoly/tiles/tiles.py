from typing import Iterator, TypeVar, Generic

from ..colour import Colour
from .plot import Plot
from .utilities import Utilities
from .station import Station
from .._fields import CountField


ConcreteTile = TypeVar("ConcreteTile")
TileCategory = TypeVar("TileCategory")


class Tiles(Generic[TileCategory]):
    """
    A collection of tiles
    """

    def __init__(self, *args: TileCategory) -> None:
        self._tiles = list(args)

    @classmethod
    def default(cls) -> "Tiles[TileCategory]":
        return cls()

    def _type_filter(self, *args: type[ConcreteTile]) -> Iterator[ConcreteTile]:
        for tile in self._tiles:
            if isinstance(tile, args):
                yield tile

    def _type_count(self, *args: type[ConcreteTile]) -> int:
        tiles = self._type_filter(*args)
        return len(list(tiles))

    def __len__(self) -> int:
        return len(self._tiles)

    def __getitem__(self, index: int) -> TileCategory:
        return self._tiles[index]

    def __iter__(self) -> Iterator[TileCategory]:
        return iter(self._tiles)

    def count_by_colour(self) -> dict[Colour, CountField]:
        counts: dict[Colour, CountField] = {}
        for tile in self._type_filter(Plot):
            counts[tile.colour] = counts.get(tile.colour, 0) + 1

        return counts

    def utility_count(self) -> int:
        return self._type_count(Utilities)

    def station_count(self) -> int:
        return self._type_count(Station)
