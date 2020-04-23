import typing

from PyQt5.QtCore import QThread, pyqtSignal, QObject

import utils
from typing import List

from Letter import Letter


class TextRecognitionThread(QThread):
    progress = pyqtSignal(int)
    result_signal=pyqtSignal(list)

    def __init__(self, letters,progress_method,result_method,parent: typing.Optional[QObject] = None) -> None:
        super().__init__(parent)
        self.letters=letters
        self.progress_method=progress_method
        self.result_method=result_method

    def run(self) -> None:
        self.progress.connect(self.progress_method)
        tables=utils.convert_images_to_letters(self.letters,self.progress)
        self.result_signal.connect(self.result_method)
        self.result_signal.emit(tables)

