from typing import Final

from data.scripts import *


class DataManager:
    def __init__(self):
        self.paths: Final[CommonPaths] = CommonPaths()
        self.data: Final[CommonData] = CommonData(self.paths.images_folder)

        self.first_plot: Final[FirstPlot] = FirstPlot()
        self.second_plot: Final[SecondPlot] = SecondPlot()


