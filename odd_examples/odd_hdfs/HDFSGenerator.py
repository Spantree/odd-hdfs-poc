from urllib.parse import urlparse

from oddrn_generator import Generator
from oddrn_generator.server_models import HostnameModel

from .HDFSPathsModel import HDFSPathsModel
from .HDFSServerModel import HDFSServerModel


class HDFSGenerator(Generator):
    source = "hdfs"
    paths_model = HDFSPathsModel
    server_model = HostnameModel  # Here we cane use a HostnameModel if HDSF is deployed on a single hosts. Use HDFSServerModel if HDFS is deployed in other ways

    @classmethod
    def from_url(cls, url: str):
        parsed = urlparse(url)
        return cls(host_settings=parsed.hostname, path=parsed.path)
