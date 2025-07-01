from typing import Any
from abc import ABC, abstractmethod


class Transformer(ABC):
    @abstractmethod
    def transform(self, data: Any) -> Any:
        pass
