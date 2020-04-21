from PIL import Image
from matplotlib import image
from matplotlib import pyplot
import pytesseract
import numpy as np
import utils


if __name__ == '__main__':
    image_np_rgb=utils.load_image_as_np_array("testsImages/test2.png",True)
    image_np_bin=utils.load_image_as_np_array("testsImages/test2.png",False)
    utils.split_grid_of_letters_image_to_letters(image_np_bin,image_np_rgb)

    a=pytesseract.image_to_string(image_np_rgb, config="--psm 10")
    image2 = Image.fromarray(image_np_rgb)
    pyplot.imshow(image2)
    pyplot.show()


