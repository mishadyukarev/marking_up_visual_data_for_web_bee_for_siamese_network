from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure


#@dataclass
class FirstPlot:
    def __init__(self):
        fig, ax = plt.subplots(figsize=(7, 7))

        self.fig: Figure = fig
        self.ax: Axes = ax
