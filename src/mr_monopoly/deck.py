import random
from typing import TypeVar, Generic


T = TypeVar("T")


class Deck(Generic[T]):
    def __init__(self, items: list[T]):
        self._items = items

    def shuffle(self) -> None:
        random.shuffle(self._items)

    def take(self) -> T:
        return self._items.pop(0)

    def restore(self, item: T) -> None:
        self._items.append(item)

    def __repr__(self) -> str:
        return f"Deck({self._items})"
