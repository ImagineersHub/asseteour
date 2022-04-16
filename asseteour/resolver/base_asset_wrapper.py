from abc import ABCMeta, abstractmethod
from typing import Dict


class BaseAssetWrapper(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def parse(cls, payload: Dict):
        pass

    @classmethod
    @abstractmethod
    def schema_json(cls, indent=4):
        pass
