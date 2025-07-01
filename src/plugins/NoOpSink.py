from src.core.operators import Sink


class NoOpSink(Sink):

    def __init__(self, operator_id: str):
        super().__init__(operator_id)

    def process(self) -> None:
        print("NoOpSink: no-op")
