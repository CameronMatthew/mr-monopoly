from typing import Iterator, TypeVar, Generic

from ..colour import Colour
from .plot import Plot
from .utilities import Utilities
from .station import Station
from .._fields import CountField, PositionField


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

    def type_filter(
        self, *args: type[ConcreteTile]
    ) -> Iterator[tuple[PositionField, ConcreteTile]]:
        for position, tile in self:
            if isinstance(tile, args):
                yield position, tile

    def _type_count(self, *args: type[ConcreteTile]) -> int:
        tiles = self.type_filter(*args)
        return len(list(tiles))

    def __len__(self) -> int:
        return len(self._tiles)

    def __getitem__(self, index: int) -> TileCategory:
        return self._tiles[index]

    def __iter__(self) -> Iterator[tuple[PositionField, TileCategory]]:
        return enumerate(iter(self._tiles))

    def count_by_colour(self) -> dict[Colour, CountField]:
        counts: dict[Colour, CountField] = {}
        for _, tile in self.type_filter(Plot):
            counts[tile.colour] = counts.get(tile.colour, 0) + 1

        return counts

    def utility_count(self) -> int:
        return self._type_count(Utilities)

    def station_count(self) -> int:
        return self._type_count(Station)
