from typing import Iterable, Any
from abc import ABC, abstractmethod


class Reader(ABC):
    @abstractmethod
    def read(self) -> Iterable[Any]:  # or AsyncIterable
        pass
