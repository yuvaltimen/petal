import boto3
from botocore.exceptions import ClientError, BotoCoreError
from typing import List, Iterable, Any

from petal.src.core.operators.Writer import Writer

sqs_client = boto3.client("sqs")


def check_queue_exists(queue_name: str) -> bool:
    """
    Checks if the specified SQS queue exists and is writable.

    :param queue_name: Name of the SQS queue
    :return: True if the queue exists and is writable, False otherwise
    """
    try:
        # Get the queue URL (this checks that it exists)
        response = sqs_client.get_queue_url(QueueName=queue_name)
        return bool(response['QueueUrl'])
    except ClientError as e:
        print(f"ClientError: {e.response['Error']['Message']}")
    except BotoCoreError as e:
        print(f"BotoCoreError: {str(e)}")
    return False


def send_messages_to_queue(queue_name: str, messages: List[str], batch_size: int = 10) -> None:
    """
    Sends a list of messages to the specified SQS queue in batches of 10.

    :param batch_size:
    :param queue_name: Name of the SQS queue
    :param messages: List of messages to send
    """
    try:
        response = sqs_client.get_queue_url(QueueName=queue_name)
        queue_url = response['QueueUrl']

        # Batch messages in groups of 10 (SQS max)
        for i in range(0, len(messages), batch_size):
            batch = messages[i:i + batch_size]
            entries = [
                {
                    'Id': str(idx),
                    'MessageBody': msg
                } for idx, msg in enumerate(batch)
            ]
            sqs_client.send_message_batch(
                QueueUrl=queue_url,
                Entries=entries
            )
    except ClientError as e:
        print(f"ClientError while sending messages: {e.response['Error']['Message']}")
    except BotoCoreError as e:
        print(f"BotoCoreError while sending messages: {str(e)}")


class SqsWriter(Writer):
    def __init__(self, operator_id: str, queue_url: str):
        super().__init__(operator_id)
        self.queue_url = queue_url

    def process(self, data: Iterable[str]) -> None:

