from PIL import Image
from matplotlib import image
from matplotlib import pyplot
import utils
if __name__ == '__main__':
    image_np_rgb=utils.load_image_as_np_array("test2.png",True)
    image_np_bin=utils.load_image_as_np_array("test2.png",False)
    print(image_np_rgb)


