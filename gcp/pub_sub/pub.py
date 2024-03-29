import os

from google.cloud import pubsub_v1

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "kissflow-dev-public-0e749d3e1ac3.json"


def pub(project_id: str, topic_id: str) -> None:
    """Publishes a message to a Pub/Sub topic."""
    # Initialize a Publisher client.
    client = pubsub_v1.PublisherClient()
    # Create a fully qualified identifier of form `projects/{project_id}/topics/{topic_id}`
    topic_path = client.topic_path(project_id, topic_id)

    # Data sent to Cloud Pub/Sub must be a bytestring.
    data = b"Hello, World!"

    # When you publish a message, the client returns a future.
    api_future = client.publish(topic_path, data)
    message_id = api_future.result()

    print(f"Published {data.decode()} to {topic_path}: {message_id}")


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(
    #     description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    # )
    # parser.add_argument("project_id", help="Google Cloud project ID")
    # parser.add_argument("topic_id", help="Pub/Sub topic ID")
    #
    # args = parser.parse_args()
    #
    # _project_id = args.project_id
    # _topic_id = args.topic_id

    _project_id = "kissflow-dev-public"
    _topic_id = "test-gcm-topic"

    pub(_project_id, _topic_id)
