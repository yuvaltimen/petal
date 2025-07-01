from abc import ABC, abstractmethod
from typing import Any


class BaseOperator(ABC):
    def __init__(self, operator_id: str):
        self.operator_id = operator_id

    def __rshift__(self, other):
        raise NotImplementedError

    def __lshift__(self, other):
        raise NotImplementedError

    @abstractmethod
    def process(self, *inputs: Any) -> Any:
        pass

