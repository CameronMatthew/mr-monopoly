from typing import Annotated

from pydantic import Field


MoneyField = Annotated[int, Field(ge=0)]
