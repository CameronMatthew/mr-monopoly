from .tiles import Tile, Tiles, Jail
from .board_context import BoardContext
from ._fields import PositionField


class Board:
    def __init__(self, tiles: Tiles[Tile]) -> None:
        self._tiles = tiles

    def __len__(self) -> int:
        return len(self._tiles)

    def __getitem__(self, index: PositionField) -> Tile:
        return self._tiles[index]

    def _jail_locations(self) -> list[PositionField]:
        return [i for i, tile in enumerate(self._tiles) if isinstance(tile, Jail)]

    def board_context(self) -> BoardContext:
        return BoardContext(
            jail_locations=self._jail_locations(),
            colour_counts=self._tiles.count_by_colour(),
            utility_count=self._tiles.utility_count(),
            station_count=self._tiles.station_count(),
        )
