from typing import Optional

from oddrn_generator.path_models import BasePathsModel


# Let's say we can uniquely identify HDFS datasets by their path
class HDFSPathsModel(BasePathsModel):
    path: Optional[str]

    class Config:
        dependencies_map = {
            "path": ("path",),
        }
