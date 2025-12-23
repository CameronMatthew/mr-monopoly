from pydantic import BaseModel

from .colour import Colour
from ._fields import CountField


class BoardContext(BaseModel):
    jail_locations: list[int]
    colour_counts: dict[Colour, CountField]
    utility_count: CountField
    station_count: CountField

    def next_jail_location(self, position: int) -> int:
        for jail_pos in self.jail_locations:
            if jail_pos > position:
                return jail_pos
        return self.jail_locations[0]
