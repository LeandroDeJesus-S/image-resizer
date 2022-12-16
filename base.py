# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 320)
        MainWindow.setMinimumSize(QtCore.QSize(540, 320))
        MainWindow.setStyleSheet("background: #1ce6b7;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.inputFilePath = QtWidgets.QLineEdit(self.centralwidget)
        self.inputFilePath.setEnabled(False)
        self.inputFilePath.setStyleSheet("background: #62efce")
        self.inputFilePath.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputFilePath.setObjectName("inputFilePath")
        self.gridLayout.addWidget(self.inputFilePath, 2, 0, 1, 2)
        self.resizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.resizeButton.setMinimumSize(QtCore.QSize(0, 25))
        self.resizeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resizeButton.setStyleSheet("background: #25937a;")
        self.resizeButton.setObjectName("resizeButton")
        self.gridLayout.addWidget(self.resizeButton, 3, 2, 1, 1)
        self.searchFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchFileButton.setMinimumSize(QtCore.QSize(0, 25))
        self.searchFileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchFileButton.setStyleSheet("background: #25937a;")
        self.searchFileButton.setObjectName("searchFileButton")
        self.gridLayout.addWidget(self.searchFileButton, 2, 2, 1, 1)
        self.inputHeight = QtWidgets.QLineEdit(self.centralwidget)
        self.inputHeight.setEnabled(True)
        self.inputHeight.setStyleSheet("background: #62efce")
        self.inputHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.inputHeight.setObjectName("inputHeight")
        self.gridLayout.addWidget(self.inputHeight, 3, 1, 1, 1)
        self.inputWidth = QtWidgets.QLineEdit(self.centralwidget)
        self.inputWidth.setEnabled(True)
        self.inputWidth.setStyleSheet("background: #62efce")
        self.inputWidth.setAlignment(QtCore.Qt.AlignCenter)
        self.inputWidth.setObjectName("inputWidth")
        self.gridLayout.addWidget(self.inputWidth, 3, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("background: #62efce")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 520, 207))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mainLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.mainLabel.setEnabled(False)
        self.mainLabel.setStyleSheet("background: #62efce; font-size: 20px;")
        self.mainLabel.setText("")
        self.mainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLabel.setObjectName("mainLabel")
        self.gridLayout_2.addWidget(self.mainLabel, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 3)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setMinimumSize(QtCore.QSize(79, 25))
        self.saveButton.setMaximumSize(QtCore.QSize(55, 24))
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveButton.setStyleSheet("background: #25937a;")
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 4, 2, 1, 1)
        self.warnings = QtWidgets.QLabel(self.centralwidget)
        self.warnings.setEnabled(False)
        self.warnings.setStyleSheet("color: red; font-size: 13px; background: #1ce6b7;")
        self.warnings.setText("")
        self.warnings.setAlignment(QtCore.Qt.AlignCenter)
        self.warnings.setObjectName("warnings")
        self.gridLayout.addWidget(self.warnings, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Resizer"))
        self.inputFilePath.setPlaceholderText(_translate("MainWindow", "..."))
        self.resizeButton.setText(_translate("MainWindow", "Redimensionar"))
        self.searchFileButton.setText(_translate("MainWindow", "Buscar imagem"))
        self.inputHeight.setPlaceholderText(_translate("MainWindow", "Y"))
        self.inputWidth.setPlaceholderText(_translate("MainWindow", "X"))
        self.saveButton.setText(_translate("MainWindow", "Salvar"))
