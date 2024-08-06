from dataclasses import dataclass

from matplotlib import pyplot as plt
from matplotlib.figure import Figure


@dataclass
class SecondPlot:
    def __init__(self):
        self.ax2 = None
        self.ax1 = None
        self.fig: Figure

    def create_plot(self):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

        self.fig: Figure = fig
        self.ax1 = ax1
        self.ax2 = ax2

        ax1.set_xticklabels([])
        ax1.set_yticklabels([])
        ax2.set_xticklabels([])
        ax2.set_yticklabels([])
