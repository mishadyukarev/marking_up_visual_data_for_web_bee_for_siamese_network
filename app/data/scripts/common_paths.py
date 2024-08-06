from dataclasses import dataclass
from pathlib import Path


@dataclass
class CommonPaths:
    def __init__(self):
        self.data_folder = Path('data')
        self.images_folder = self.data_folder / Path('images')
        
        self.street_images_folder = self.images_folder / Path('street')
        self.crop_images_folder = self.images_folder / Path('crop')
