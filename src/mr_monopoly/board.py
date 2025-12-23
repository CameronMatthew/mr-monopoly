from .tiles import Tile, Go, Plot, Jail, Tax
from .property import Property
from .colour import Colour
from .board_context import BoardContext


class Board:
    def __init__(self, tiles: list[Tile]) -> None:
        self._tiles = tiles

    def __len__(self) -> int:
        return len(self._tiles)

    def __getitem__(self, index: int) -> Tile:
        return self._tiles[index]

    def _jail_locations(self) -> list[int]:
        return [i for i, tile in enumerate(self._tiles) if isinstance(tile, Jail)]

    def _colour_counts(self) -> dict[Colour, int]:
        counts: dict[Colour, int] = {}
        for tile in self._tiles:
            if isinstance(tile, Plot):
                counts[tile.colour] = counts.get(tile.colour, 0) + 1

        return counts

    def board_context(self) -> BoardContext:
        return BoardContext(
            jail_locations=self._jail_locations(), colour_counts=self._colour_counts()
        )


CLASSIC = Board(
    tiles=[
        Go(),
        Plot(
            name="Old Kent Road",
            colour=Colour.BROWN,
            property=Property(
                house_price=10,
                hotel_price=100,
                base_rent=20,
                hotel_rent=[60],
                house_rent=[20, 30],
            ),
            purchase_price=60,
        ),
        Jail(),
        Tax(),
    ]
)
