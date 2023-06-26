import click
from odd_models.api_client.v2.odd_api_client import Client
from odd_models.discovery import DataSource

from odd_examples.odd_hdfs.HDFSArtifact import HDFSArtifact

PLATFORM_HOST = "http://localhost:8080"
DATASOURCE_ODDRN = "//mycompany/hdfs"
COLLECTOR_NAME = "HdfsCollector"  # This name is used to identify the collector in the platform, for them we create a tokens.

# 1. Create a token
client = Client(host=PLATFORM_HOST)
MY_TOKEN = client.create_token(name=COLLECTOR_NAME, description="")
print(MY_TOKEN)  # Do not forget to save this token somewhere. You will need it later.

# 2. Create a data source. This is required only once.
client = Client(host=PLATFORM_HOST, token=MY_TOKEN)
client.create_data_source(
    data_source_oddrn=DATASOURCE_ODDRN,
    data_source_name="HDFS",
)
# Important
# Two steps above are required only once, to create a data source and a token,
# we can do it manually in the platform UI or using the API from above.
# After that, you can use the token to create a client instance and use it to add entities to the data source.

# 3. Create a client instance that we will use as many times as we want with already created data source and token
client = Client(host=PLATFORM_HOST, token=MY_TOKEN)


@click.command()
def main():
    # Your CLI logic goes here
    click.echo("Running add-entities command!")

    with DataSource(DATASOURCE_ODDRN, client=client) as ds:
        hdfs_artifact = HDFSArtifact.from_url(
            "http://myhost:9870/sparkapps/test/test_spark_job.py"
        )
        ds.add_data_asset(hdfs_artifact)


if __name__ == "__main__":
    main()
