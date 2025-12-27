from typing import Annotated

from pydantic import Field


MoneyField = Annotated[int, Field(ge=0)]
CountField = Annotated[int, Field(ge=0)]
PositionField = Annotated[int, Field(ge=0, default=0)]
DisplacementField = int
