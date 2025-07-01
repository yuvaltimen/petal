from typing import Iterable, Any
from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def write(self, data: Iterable[Any]) -> None:
        pass
