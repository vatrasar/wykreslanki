import numpy as np
from PIL import Image
from matplotlib import pyplot
class Letter():
    def __init__(self,img_letter:np.ndarray,character:str) -> None:
        super().__init__()
        self.img_letter=img_letter
        self.character=character
        self.img_grey=img_letter[:,:,0]
    def show_image(self):
        image2 = Image.fromarray(self.img_letter)
        pyplot.imshow(image2)
        pyplot.show()