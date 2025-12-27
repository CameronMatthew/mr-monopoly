from .tiles import Tile, Tiles
from .board_context import BoardContext
from ._fields import PositionField


class Board:
    def __init__(self, tiles: Tiles[Tile]) -> None:
        self._tiles = tiles

    def __len__(self) -> int:
        return len(self._tiles)

    def __getitem__(self, index: PositionField) -> Tile:
        return self._tiles[index]

    @property
    def tiles(self) -> Tiles[Tile]:
        return self._tiles

    def board_context(self) -> BoardContext:
        return BoardContext(
            colour_counts=self._tiles.count_by_colour(),
            utility_count=self._tiles.utility_count(),
            station_count=self._tiles.station_count(),
        )
