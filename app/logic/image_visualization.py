import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from matplotlib.axes import Axes


def visualize_image(image: Image, ax: Axes, coordinate_boxes: list[dict[str: int]] = None, ):
    image_ar = np.array(image)

    if coordinate_boxes is not None and len(coordinate_boxes) > 0:
        for coordinates in coordinate_boxes:
            # print(coordinates)

            x1, y1, x2, y2 = list(coordinates.values())
            image_ar[y1: y2, x1: x2, :] = 0

    ax.imshow(image_ar)
    plt.draw()
