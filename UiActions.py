from PyQt5.QtGui import QPixmap

from MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import utils
from PIL import Image

class UiActions():
    def __init__(self,window:Ui_MainWindow) -> None:
        super().__init__()
        window.btnAddWord.clicked.connect(self.on_add_word)
        self.window=window
        self.modelListView = QtGui.QStandardItemModel()
        self.window.wordListView.setModel(self.modelListView)
        self.window.wordListView.doubleClicked.connect(self.delete_item)
        self.window.btnLoadImage.clicked.connect(self.set_image)

    def on_add_word(self):
        new_item=self.window.txtWord.text()
        self.window.txtWord.setText("")
        item = QtGui.QStandardItem(new_item)

        self.modelListView.appendRow(item)
    def delete_item(self,index):
        self.modelListView.removeRow(index.row())

    def set_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        fileName, _ =QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()","", "All Files (*.png);;Obrazki (*.png);;jpg (*.jpg)",options=options)
        if fileName:
            self.image_np_rgb = utils.load_image_as_np_array(fileName, True)
            image_np_bin = utils.load_image_as_np_array(fileName, False)
            img_letters = utils.split_image_to_images_of_letters(image_np_bin, self.image_np_rgb)
            self.grid_of_letters = utils.convert_images_to_letters(img_letters)
            self.update_image()


    def update_image(self):

        image2 = Image.fromarray(self.image_np_rgb)
        image2.save("temp.png")
        pixmap = QPixmap("temp.png")
        self.window.resultView.setPixmap(pixmap)
        
