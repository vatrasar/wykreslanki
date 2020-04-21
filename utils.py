from typing import List
import numpy as np
from PIL import Image
from numpy import asarray
from numpy import ndarray

def split_grid_of_letters_image_for_letters(image)->list:
    """
    split one image of grid of latters for collection of images of letters
:return list of numpy arrays which includes images of latters
    """
    pass



def load_image_as_np_array(image_name:str, is_rgb)->ndarray:
    """

    :param image_name: string
    :return: returns image as numpy array
    """
    image = Image.open(image_name)
    if not(is_rgb):
        image=image.convert('1')
    image_np=asarray(image)

    return image_np


