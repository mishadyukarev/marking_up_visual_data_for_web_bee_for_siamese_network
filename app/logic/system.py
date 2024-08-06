from typing import Final

from data.scripts import *
from data.scripts.data_manager import DataManager


class System:
    def __init__(self, data_manager: DataManager):
        self.data: Final[CommonData] = data_manager.data
        self.paths: Final[CommonPaths] = data_manager.paths