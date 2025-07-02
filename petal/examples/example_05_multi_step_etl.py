from petal.src.core.pipeline import Pipeline
from petal.src.plugins.FileReader import FileReader
from petal.src.plugins.FileWriter import FileWriter
from petal.src.plugins.StreamJoiner import StreamJoiner


def main():
    # We're now ready to compose a complex multi-stage ETL.
    with Pipeline("example_05_multi_step_etl") as dag:
        # Let's start our Sources
        log_file = FileReader("log_file", file_path="../data/app_logs.txt")
        events_file = FileReader("events_file", file_path="../data/vm_events.txt")

        # Then our Sinks
        write_to_file = FileWriter("write_to_file", file_path="../data/detected_pings.txt")
        write_to_sqs = SqsWriter("write_to_sqs", queue_url="https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue")


    dag.run()


if __name__ == '__main__':
    main()
