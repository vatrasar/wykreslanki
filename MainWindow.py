# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"margin:20%;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.result_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.result_widget.sizePolicy().hasHeightForWidth())
        self.result_widget.setSizePolicy(sizePolicy)
        self.result_widget.setMinimumSize(QtCore.QSize(0, 500))
        self.result_widget.setObjectName("result_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.result_widget)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.resultView = QtWidgets.QLabel(self.result_widget)
        self.resultView.setText("")
        self.resultView.setObjectName("resultView")
        self.verticalLayout_5.addWidget(self.resultView)
        self.verticalLayout_4.addWidget(self.result_widget)
        self.btnLoadImage = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.btnLoadImage.sizePolicy().hasHeightForWidth())
        self.btnLoadImage.setSizePolicy(sizePolicy)
        self.btnLoadImage.setMinimumSize(QtCore.QSize(30, 50))
        self.btnLoadImage.setMouseTracking(False)
        self.btnLoadImage.setAutoFillBackground(False)
        self.btnLoadImage.setObjectName("btnLoadImage")
        self.verticalLayout_4.addWidget(self.btnLoadImage)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setMinimumSize(QtCore.QSize(148, 412))
        self.dockWidget_2.setMaximumSize(QtCore.QSize(148, 524287))
        self.dockWidget_2.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 100))
        self.label_2.setMaximumSize(QtCore.QSize(130, 100))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.btnAddWord = QtWidgets.QPushButton(self.dockWidgetContents_3)
        self.btnAddWord.setObjectName("btnAddWord")
        self.verticalLayout_2.addWidget(self.btnAddWord)
        self.txtWord = QtWidgets.QLineEdit(self.dockWidgetContents_3)
        self.txtWord.setObjectName("txtWord")
        self.verticalLayout_2.addWidget(self.txtWord)
        self.wordListView = QtWidgets.QListView(self.dockWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.wordListView.sizePolicy().hasHeightForWidth())
        self.wordListView.setSizePolicy(sizePolicy)
        self.wordListView.setMinimumSize(QtCore.QSize(0, 50))
        self.wordListView.setObjectName("wordListView")
        self.verticalLayout_2.addWidget(self.wordListView)
        self.loadWordsList = QtWidgets.QPushButton(self.dockWidgetContents_3)
        self.loadWordsList.setObjectName("loadWordsList")
        self.verticalLayout_2.addWidget(self.loadWordsList)
        self.dockWidget_2.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wykreślak"))
        self.btnLoadImage.setText(_translate("MainWindow", "Wczytaj zdjęcie"))
        self.btnAddWord.setText(_translate("MainWindow", "Dodaj słowo"))
        self.loadWordsList.setText(_translate("MainWindow", "Wczytaj liste słów"))
