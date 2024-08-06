import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class CommonData:

    def __init__(self, image_folder_path: Path):
        self.is_first_click = True
        self.picture_is_zoomed = False
        self.is_first_stage_of_script: bool = True

        self.current_crop_coordinates: dict[str: int] = {key: -1 for key in ['x1', 'y1', 'x2', 'y2']}
        self.coordinate_boxes: list[dict[str: int]] = []

        self.current_street_image_index = 0
        self.current_crop_image_index = 0

        self.images: list = []

        self.how_many_images = len([entry for entry in os.scandir(image_folder_path) if entry.is_file()])

        # self.current_opened_image = None
