from odd_models import DataEntity, DataEntityType, DataSet
from odd_models.discovery.data_assets.data_asset import DataAsset, HasUpstream

from .HDFSGenerator import HDFSGenerator


class HDFSArtifact(DataAsset):
    def __init__(self, oddrn, name=None):
        self.oddrn = oddrn
        self.name = name

    def __rshift__(self, data_asset: HasUpstream) -> DataAsset:
        data_asset.add_upstream(self)
        return data_asset

    def __repr__(self):
        return f"{self.name}"

    @classmethod
    def from_url(cls, url: str, name=None):
        oddrn = HDFSGenerator.from_url(url).get_oddrn_by_path("path")
        return cls(oddrn, name or oddrn.split("/")[-1])

    def to_data_entity(self) -> DataEntity:
        return DataEntity(
            oddrn=self.oddrn,
            name=self.name,
            type=DataEntityType.TABLE,
            owner=None,
            dataset=DataSet(field_list=[]),
        )
