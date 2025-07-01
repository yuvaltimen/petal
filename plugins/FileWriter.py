from collections.abc import Iterable

from core.writer import Writer


class FileWriter(Writer):

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, data: Iterable[str]) -> None:
        print(f"FileWriter: writing to file {self.file_path}.")
        with open(self.file_path, 'w') as f:
            ctr = 0
            print(f"FileWriter: writing line {ctr}...")
            f.writelines(data)
        print(f"FileWriter: done writing.")

