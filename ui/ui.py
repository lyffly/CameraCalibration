# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cameraCali.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1192, 748)
        self.open_camera_button = QtWidgets.QPushButton(Dialog)
        self.open_camera_button.setGeometry(QtCore.QRect(860, 30, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.open_camera_button.setFont(font)
        self.open_camera_button.setObjectName("open_camera_button")
        self.image_label = QtWidgets.QLabel(Dialog)
        self.image_label.setGeometry(QtCore.QRect(10, 120, 800, 600))
        self.image_label.setFrameShape(QtWidgets.QFrame.Box)
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.capture_button = QtWidgets.QPushButton(Dialog)
        self.capture_button.setGeometry(QtCore.QRect(860, 130, 121, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.capture_button.setFont(font)
        self.capture_button.setObjectName("capture_button")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 720, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.close_camera_button = QtWidgets.QPushButton(Dialog)
        self.close_camera_button.setGeometry(QtCore.QRect(1000, 30, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.close_camera_button.setFont(font)
        self.close_camera_button.setObjectName("close_camera_button")
        self.cali_button = QtWidgets.QPushButton(Dialog)
        self.cali_button.setGeometry(QtCore.QRect(860, 220, 121, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.cali_button.setFont(font)
        self.cali_button.setObjectName("cali_button")
        self.label_result = QtWidgets.QLabel(Dialog)
        self.label_result.setGeometry(QtCore.QRect(820, 400, 361, 261))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_result.setObjectName("label_result")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(820, 350, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit1.setGeometry(QtCore.QRect(110, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit1.setFont(font)
        self.lineEdit1.setObjectName("lineEdit1")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(170, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit2.setGeometry(QtCore.QRect(220, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit2.setFont(font)
        self.lineEdit2.setObjectName("lineEdit2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(300, 20, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit3.setGeometry(QtCore.QRect(360, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit3.setFont(font)
        self.lineEdit3.setObjectName("lineEdit3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit4.setGeometry(QtCore.QRect(130, 70, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit4.setFont(font)
        self.lineEdit4.setObjectName("lineEdit4")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(180, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit5.setGeometry(QtCore.QRect(240, 70, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lineEdit5.setFont(font)
        self.lineEdit5.setObjectName("lineEdit5")
        self.set_button = QtWidgets.QPushButton(Dialog)
        self.set_button.setGeometry(QtCore.QRect(710, 30, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.set_button.setFont(font)
        self.set_button.setObjectName("set_button")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(780, 10, 51, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.open_camera_button.setText(_translate("Dialog", "Open Camera"))
        self.capture_button.setText(_translate("Dialog", "Capture"))
        self.label.setText(_translate("Dialog", "liuyunfei.1314@163.com "))
        self.close_camera_button.setText(_translate("Dialog", "Close Camera"))
        self.cali_button.setText(_translate("Dialog", "Calibration"))
        self.label_3.setText(_translate("Dialog", "-  Result - "))
        self.lineEdit1.setText(_translate("Dialog", "0"))
        self.label_4.setText(_translate("Dialog", "Camera No:"))
        self.label_5.setText(_translate("Dialog", "Width:"))
        self.lineEdit2.setText(_translate("Dialog", "960"))
        self.label_6.setText(_translate("Dialog", "Height:"))
        self.lineEdit3.setText(_translate("Dialog", "720"))
        self.label_7.setText(_translate("Dialog", "ChAruco Width:"))
        self.lineEdit4.setText(_translate("Dialog", "9"))
        self.label_8.setText(_translate("Dialog", "Height:"))
        self.lineEdit5.setText(_translate("Dialog", "7"))
        self.set_button.setText(_translate("Dialog", "Set"))
