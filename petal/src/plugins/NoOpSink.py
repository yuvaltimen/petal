from typing import Any

from petal.src.logger import logger
from petal.src.core.operators.Sink import Sink


class NoOpSink(Sink):

    def __init__(self, operator_id: str):
        super().__init__(operator_id)

    def process(self, data: Any) -> None:
        logger.info("NoOpSink: no-op")
