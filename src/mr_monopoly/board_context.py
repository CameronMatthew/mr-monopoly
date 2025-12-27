from pydantic import BaseModel

from .colour import Colour
from ._fields import CountField


class BoardContext(BaseModel):
    colour_counts: dict[Colour, CountField]
    utility_count: CountField
    station_count: CountField
