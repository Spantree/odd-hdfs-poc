from oddrn_generator.server_models import AbstractServerModel
from pydantic import BaseModel


class HDFSServerModel(AbstractServerModel, BaseModel):
    def __str__(self) -> str:
        return "mycompany/hdfs"

    @classmethod
    def create(cls, config):
        return cls()
