from PIL import Image
from PyQt5.QtWidgets import QApplication
from matplotlib import image
from matplotlib import pyplot
import pytesseract
import numpy as np
import utils
from  MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from UiActions import UiActions

if __name__ == '__main__':
    image_np_rgb=utils.load_image_as_np_array("testsImages/test6.png",True)
    image_np_bin=utils.load_image_as_np_array("testsImages/test6.png",False)
    img_letters=utils.split_image_to_images_of_letters(image_np_bin,image_np_rgb)
    grid_of_letters=utils.convert_images_to_letters(img_letters)

    grid_of_letters[0][0].show_image()

    app = QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(window)
    actions=UiActions(ui)
    window.show()
    sys.exit(app.exec_())



