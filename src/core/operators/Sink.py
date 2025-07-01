from src.core.operators import BaseOperator


class Sink(BaseOperator):
    def __init__(self, operator_id: str):
        super().__init__(operator_id)
        self.upstream = []

    def __lshift__(self, other):
        # self << other
        return other.__rshift__(self)
