from PIL import Image
from matplotlib import image
from matplotlib import pyplot
import pytesseract
import numpy as np
import utils


if __name__ == '__main__':
    image_np_rgb=utils.load_image_as_np_array("testsImages/test6.png",True)
    image_np_bin=utils.load_image_as_np_array("testsImages/test6.png",False)
    img_letters=utils.split_image_to_images_of_letters(image_np_bin,image_np_rgb)
    grid_of_letters=utils.convert_images_to_letters(img_letters)
    # a=pytesseract.image_to_string(image_np_rgb, config="--psm 10")
    # image2 = Image.fromarray(image_np_rgb)
    # pyplot.imshow(image2)
    # pyplot.show()
    grid_of_letters[0][0].show_image()



