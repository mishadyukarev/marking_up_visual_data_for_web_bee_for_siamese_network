import os
import re
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

from logic.image_visualization import visualize_image
from data.scripts.data_manager import DataManager


def is_left_mouse_click(button):
    return button == 1


def is_center_mouse_click(button):
    return button == 2


def print_which_mouse_click(button):
    if button == 1:
        print('Left click')
    elif button == 2:
        print('Center click')
    elif button == 3:
        print('Right click')


class ExecutionFirstStage:
    def __init__(self, data_manager: DataManager):

        self.common_data = data_manager.data
        self.paths = data_manager.paths
        self.first_plot = data_manager.first_plot

        # super().__init__(data_manager)

    def click(self, event):

        print_which_mouse_click(event.button)

        if not self.common_data.is_first_stage_of_script:
            return

        if self.common_data.picture_is_zoomed:
            self.common_data.picture_is_zoomed = False

            if is_left_mouse_click(event.button):
                self.common_data.current_opened_image.save(
                    self.paths.crop_images_folder / f'image{self.common_data.current_street_image_index}_crop{self.common_data.current_crop_image_index}.jpg')
                self.common_data.current_crop_image_index += 1

                self.common_data.coordinate_boxes.append(self.common_data.current_crop_coordinates.copy())

            self.common_data.current_opened_image = self.common_data.images[self.common_data.current_street_image_index]

            visualize_image(self.common_data.current_opened_image, self.first_plot.ax,
                            self.common_data.coordinate_boxes)

        else:
            if is_left_mouse_click(event.button):  # Left mouse button

                x_coordinate_during_click = int(event.xdata)
                y_coordinate_during_click = int(event.ydata)

                # print(f'Clicked at pixel coordinates ({x_coordinate_during_click}, {y_coordinate_during_click})')

                if self.common_data.is_first_click:
                    self.common_data.current_crop_coordinates['x1'] = x_coordinate_during_click
                    self.common_data.current_crop_coordinates['y1'] = y_coordinate_during_click

                    self.common_data.is_first_click = False
                else:
                    if x_coordinate_during_click > self.common_data.current_crop_coordinates[
                        'x1'] and y_coordinate_during_click > \
                            self.common_data.current_crop_coordinates['y1']:
                        self.common_data.current_crop_coordinates['x2'] = x_coordinate_during_click
                        self.common_data.current_crop_coordinates['y2'] = y_coordinate_during_click

                        # print(list(self.common_data.current_crop_coordinates.values()))

                        self.common_data.current_opened_image = self.common_data.current_opened_image.crop(
                            tuple(self.common_data.current_crop_coordinates.values()))

                        visualize_image(self.common_data.current_opened_image, self.first_plot.ax)

                        self.common_data.picture_is_zoomed = True
                        self.common_data.is_first_click = True

                    else:
                        self.common_data.current_crop_coordinates['x1'] = x_coordinate_during_click
                        self.common_data.current_crop_coordinates['y1'] = y_coordinate_during_click

            elif is_center_mouse_click(event.button):

                # print(self.common_data.current_street_image_index + 1, self.common_data.how_many_images)

                if self.common_data.current_street_image_index + 1 >= self.common_data.how_many_images:
                    plt.close(self.first_plot.fig)
                    self.common_data.is_first_stage_of_script = False

                else:
                    self.common_data.current_street_image_index += 1
                    self.common_data.current_crop_image_index = 0

                    self.common_data.coordinate_boxes = []

                    self.common_data.current_opened_image = self.common_data.images[self.common_data.current_street_image_index]

                    visualize_image(self.common_data.current_opened_image, self.first_plot.ax)

            else:
                pass


class ExecutionSecondStage:
    __result_df: pd.DataFrame

    def __init__(self, data_manager: DataManager):
        # super().__init__(data_manager)

        self.data = data_manager.data
        self.second_plot = data_manager.second_plot
        self.paths = data_manager.paths

        self.__current_image_index = 0
        self.__result: Final[dict[str: list]] = {'street_image_name': [],
                                                 'crop_name': [],
                                                 'target': []}

        # self.__result_df: pd.DataFrame = pd.DataFrame()

    def start(self):
        entities_in_street = [entry for entry in os.scandir(self.paths.street_images_folder) if entry.is_file()]
        entities_in_crop = [entry for entry in os.scandir(self.paths.crop_images_folder) if entry.is_file()]

        for street_image_index, image_entity in enumerate(entities_in_street):
            # print(street_image_index, image_entity)

            for crop_index, crop_entity in enumerate(entities_in_crop):
                self.__result['street_image_name'].append(image_entity.name)
                self.__result['crop_name'].append(crop_entity.name)

                if len(re.findall(f'image{street_image_index}', crop_entity.name)) > 0:
                    self.__result['target'].append(1)

                else:
                    self.__result['target'].append(None)

        self.__result_df = pd.DataFrame(self.__result)

        for i, row in self.__result_df.iterrows():
            if pd.isna(row['target']):
                street_image = Image.open(self.paths.street_images_folder / row['street_image_name']).convert('RGB')
                self.second_plot.ax1.imshow(np.array(street_image))

                crop_image = Image.open(self.paths.crop_images_folder / row['crop_name']).convert('RGB')
                self.second_plot.ax2.imshow(np.array(crop_image))

                plt.draw()

                self.__current_image_index = i

                break

        print(self.__result_df)
        # print(self.__indexes_need_to_go)

    def click(self, event):
        if is_left_mouse_click(event.button):
            self.__result_df.loc[self.__current_image_index, 'target'] = 1
        else:
            self.__result_df.loc[self.__current_image_index, 'target'] = 0

        for i, row in self.__result_df.iterrows():
            if i > self.__current_image_index:
                if pd.isna(row['target']):
                    street_image = Image.open(self.paths.street_images_folder / row['street_image_name']).convert('RGB')
                    self.second_plot.ax1.imshow(np.array(street_image))

                    crop_image = Image.open(self.paths.crop_images_folder / row['crop_name']).convert('RGB')
                    self.second_plot.ax2.imshow(np.array(crop_image))

                    plt.draw()

                    self.__current_image_index = i

                    break

            if i == self.__result_df.index.max():
                plt.close(self.second_plot.fig)

        self.__result_df.to_csv(self.paths.images_folder / 'result.csv', index=False)

        print(self.__result_df)


