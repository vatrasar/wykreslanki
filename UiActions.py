from PyQt5.QtGui import QPixmap, QColor

from MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel, QProgressBar, QSizePolicy
import utils
from PIL import Image
import numpy as np

class UiActions():
    def __init__(self,window:Ui_MainWindow) -> None:
        super().__init__()
        window.btnAddWord.clicked.connect(self.on_add_word)
        self.window=window
        self.modelListView = QtGui.QStandardItemModel()
        self.window.wordListView.setModel(self.modelListView)
        self.window.wordListView.doubleClicked.connect(self.delete_item)
        self.window.btnLoadImage.clicked.connect(self.set_image)
        self.window.loadWordsList.clicked.connect(self.on_load_words_list)
        self.item_image_list=[]
        self.progressBar=QProgressBar()


        self.progressBar.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.progressBar.setMinimumHeight(60)
        self.progressBar.setStyleSheet("#progressBar{\nheight:red;\n}")


    def on_load_words_list(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*.png);;Obrazki (*.png);;jpg (*.jpg)", options=options)
        if fileName:
            image_np_rgb = utils.load_image_as_np_array(fileName, True)
            image_np_bin = utils.load_image_as_np_array(fileName, False)
            words = utils.split_image_to_images_of_words(image_np_bin, image_np_rgb)
            for word in words:
                self.add_new_word(word)
            self.update_image()


    def on_add_word(self):
        new_item=self.window.txtWord.text()
        if len(new_item)==0:
            return
        self.window.txtWord.setText("")
        self.add_new_word(new_item)
        self.update_image()

    def add_new_word(self, word_to_add):
        item = QtGui.QStandardItem(word_to_add)
        self.modelListView.appendRow(item)
        result = self.look_for_word(word_to_add)
        if len(result) != 0:
            self.item_image_list.append(result)
            for letter in result:
                utils.mark_letter(letter)
        else:
            item.setBackground(QColor(200, 0, 0))

    def delete_item(self,index):
        self.modelListView.removeRow(index.row())
        self.un_mark_word(self.item_image_list[index.row()])
        self.update_image()

    def set_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        fileName, _ =QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()","", "All Files (*.png);;Obrazki (*.png);;jpg (*.jpg)",options=options)
        if fileName:

            self.window.resultView.setParent(None)

            self.image_np_rgb = utils.load_image_as_np_array(fileName, True)
            image_np_bin = utils.load_image_as_np_array(fileName, False)
            img_letters = utils.split_image_to_images_of_letters(image_np_bin, self.image_np_rgb)

            self.set_progress_bar()
            self.grid_of_letters = utils.convert_images_to_letters(img_letters)
            self.update_image()


    def update_image(self):

        image2 = Image.fromarray(self.image_np_rgb)
        image2.save("temp.png")
        pixmap = QPixmap("temp.png")
        self.window.resultView.setPixmap(pixmap)

    def look_for_word(self,word:str):
        for r_index,row in enumerate(self.grid_of_letters):
            for c_index, letter in enumerate(row):
                if word[0]==letter.character:
                   result=self.check_letter(word,r_index,c_index)
                   if len(result)!=0:
                        return result
        return []

    def check_letter(self, word, r_index, c_index)->list:
        # letters=[]
        #
        # letters.append(self.grid_of_letters[r_index][c_index])

        test_list=[(1,1),(-1,1),(-1,-1),(1,-1),(0,1),(1,0),(0,-1),(-1,0)]
        for test in test_list:
            result=self.check_direction(word,r_index,c_index,test[0],test[1])
            if len(result)!=0:
                result.append(self.grid_of_letters[r_index][c_index])
                return result
        return []






    def check_direction(self,word,r_index, c_index,r_progres,c_progres):

        letters=[]
        r=r_index
        c=c_index
        index=1
        while True:
           r+=r_progres
           c+=c_progres
           try:
               if r>= len(self.grid_of_letters) or c>= len(self.grid_of_letters[r]) or c<0 or r<0:
                   return []
               if self.grid_of_letters[r][c].character==word[index]:

                   letters.append(self.grid_of_letters[r][c])
                   index+=1
                   if index== len(word):
                       return letters

               else:
                   return []
           except IndexError:
               print("cos")


    def un_mark_word(self, letters):
        for letter in letters:
            image = letter.img_letter
            np.apply_along_axis(self.un_mark, 2, image)
    def un_mark(self,x: np.ndarray):
        x[0] += 100
        x[2] += 100

    def set_progress_bar(self):
        self.window.result_widget.layout().setContentsMargins(50, 1, 50, 1)
        self.window.result_widget.layout().addWidget(self.progressBar)


