from core.pipeline import Pipeline
from core.reader import Reader
from core.transformer import Transformer
from core.writer import Writer

"""
Sequence of transformations to be applied to an input file and written to output destination."""


class SimplePipeline(Pipeline):

    def __init__(self,
                 reader: Reader = None,
                 transformer: Transformer = None,
                 writer: Writer = None):
        self.reader = reader
        self.transformer = transformer
        self.writer = writer

    def run(self) -> None:
        for line in self.reader.read():
            self.writer.write(
                self.transformer.transform(line)
            )
