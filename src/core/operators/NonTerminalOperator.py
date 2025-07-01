from src.core.operators.Sink import Sink
from src.core.operators.Source import Source


class NonTerminalOperator(Source, Sink):
    def __init__(self, operator_id: str):
        super().__init__(operator_id)
