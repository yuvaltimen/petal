from plugins.SimplePipeline import SimplePipeline
from plugins.FileReader import FileReader
from plugins.FileWriter import FileWriter
from plugins.IdentityTransformer import IdentityTransformer


def main():
    pl = SimplePipeline(
        reader=FileReader(
            file_path="./data/example_input.txt"
        ),
        transformer=IdentityTransformer(),
        writer=FileWriter(
            file_path="./data/output_file.txt"
        )
    )

    pl.run()


if __name__ == '__main__':
    main()
