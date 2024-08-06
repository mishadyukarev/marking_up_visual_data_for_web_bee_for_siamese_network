import fnmatch
import os
import shutil
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from data.scripts import *
from logic import *
from data.scripts.data_manager import DataManager

data_manager: DataManager = DataManager()
paths: CommonPaths = data_manager.paths
data: CommonData = data_manager.data
first_plot: FirstPlot = data_manager.first_plot
second_plot: SecondPlot = data_manager.second_plot

first_stage: ExecutionFirstStage = ExecutionFirstStage(data_manager)
second_stage: ExecutionSecondStage = ExecutionSecondStage(data_manager)

if __name__ == '__main__':

    images = []

    if os.path.isdir(paths.street_images_folder) is False:
        os.mkdir(paths.street_images_folder)

        for file in os.listdir(paths.images_folder):
            if fnmatch.fnmatch(file, '*.jpg') or fnmatch.fnmatch(file, '*.png'):
                shutil.move(paths.images_folder / file, paths.street_images_folder)

        for file in os.listdir(paths.street_images_folder):
            if fnmatch.fnmatch(file, '*.jpg') or fnmatch.fnmatch(file, '*.png'):
                images.append(Image.open(paths.street_images_folder / file).convert('RGB'))

    data.images = images

    if os.path.isdir(paths.crop_images_folder) is False:
        os.mkdir(paths.crop_images_folder)

    street_image = images[data.current_street_image_index]
    data.current_opened_image = street_image
    street_image_array = np.array(street_image)
    first_plot.ax.imshow(street_image_array)
    cid = first_plot.fig.canvas.mpl_connect('button_press_event', first_stage.click)
    plt.show()

    second_plot.create_plot()
    second_stage.start()
    second_plot.fig.canvas.mpl_connect('button_press_event', second_stage.click)
    plt.show()
