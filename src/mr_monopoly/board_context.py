from pydantic import BaseModel

from .colour import Colour


class BoardContext(BaseModel):
    jail_locations: list[int]
    colour_counts: dict[Colour, int]

    def next_jail_location(self, position: int) -> int:
        for jail_pos in self.jail_locations:
            if jail_pos > position:
                return jail_pos
        return self.jail_locations[0]
