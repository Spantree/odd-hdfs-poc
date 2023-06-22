from urllib.parse import urlparse
from oddrn_generator import Generator
from . import HDFSPathsModel, HDFSServerModel


class HDFSGenerator(Generator):
    source = "hdfs"
    paths_model = HDFSPathsModel
    server_model = HDFSServerModel

    @classmethod
    def from_url(cls, url: str):
        parsed = urlparse(url)
        generator = cls()
        generator.set_oddrn_paths(
            host=parsed.hostname, port=parsed.port, path=parsed.path
        )

        return generator
