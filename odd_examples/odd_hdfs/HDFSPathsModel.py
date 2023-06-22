from typing import Optional

from oddrn_generator.path_models import BasePathsModel


class S3PathsModel(BasePathsModel):
    host: Optional[str]
    owner: Optional[str]
    path: Optional[str]

    class Config:
        dependencies_map = {
            "host": ("host",),
            "path": ("host", "path"),
            "owner": ("host", "path", "owner"),
        }
