import click
from .odd_hdfs import HDFSArtifact

from odd_models.api_client.v2.odd_api_client import Client
from odd_models.discovery import DataSource

client = Client(host="http://localhost:8080")
client.auth(name="dev_aws_token", description="Token for dev AWS account data sources")


@click.command()
def main():
    # Your CLI logic goes here
    click.echo("Running add-entities command!")
    with DataSource("//mycompany/hdfs") as ds:
        hdfs_artifact = HDFSArtifact.from_url(
            "http://10.77.101.155:9870/sparkapps/spark-resources/spark/submit_test/cat_report.zip"
        )
        ds.add_data_asset(hdfs_artifact)


if __name__ == "__main__":
    main()
