from random import choice

from pydantic import BaseModel, Field


class Die(BaseModel):
    value: int = Field(ge=1, le=6)

    @classmethod
    def roll(cls) -> "Die":
        choices = list(range(1, 7, 1))
        value = choice(choices)
        return cls(value=value)


class RollResult:
    def __init__(self, *args: Die):
        self._results = args

    def __getitem__(self, index: int) -> Die:
        return self._results[index]

    def total(self) -> int:
        return sum((die.value for die in self._results))


def roll() -> RollResult:
    d1 = Die.roll()
    d2 = Die.roll()
    return RollResult(d1, d2)
