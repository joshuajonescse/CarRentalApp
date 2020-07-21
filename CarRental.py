# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'one.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush,QPalette,QImage
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):

# the below 6 lines of code is to set the background picture
        background_img=QImage("image2.jpg")
        scaled_img = background_img.scaled(QSize(553, 554))

        palette = QPalette()
        palette.setBrush(10,QBrush(scaled_img))
        Dialog.setPalette(palette)

# the below line is to add the icon in the left top side corner
        Dialog.setWindowIcon(QtGui.QIcon("icon1.jpg"))

        Dialog.setObjectName("Dialog")
        Dialog.resize(553, 554)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 90, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{color:rgb(255, 255, 255)}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 160, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{color:rgb(255, 255, 255)}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(290, 250, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{color:rgb(255, 255, 255)}")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(430, 100, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 170, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 260, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 350, 131, 41))
        self.pushButton.setStyleSheet("QPushButton{background-color:rgb(255, 0, 0)}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 350, 131, 41))
        self.pushButton_2.setStyleSheet("QPushButton{background-color:rgb(255, 0, 0)}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(250, 410, 171, 111))
        self.plainTextEdit.setStyleSheet("QQPlainTextEdit{color:rgb(255, 255, 255);background-color:rgb(0, 0, 0);border: 3px solid yellow}")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.calculate_fee)
        self.pushButton_2.clicked.connect(self.clear_all)

    def invalid_input(self):
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Warning)
        infoBox.setText("Invalid Input")
        infoBox.setInformativeText("Invalid or Empty Input provided")
        infoBox.setWindowTitle("Warning")
        infoBox.exec_()


    def calculate_fee(self):
        days = self.lineEdit.text().strip()  # strip method here is to remov    e unwanted spaces if user has made
        startread = self.lineEdit_2.text().strip()
        endread= self.lineEdit_3.text().strip()

        if days == "" or startread == "" or endread == "":
            self.invalid_input()
        else:
            print (days, startread, endread)
            try:
                days = int(days)
                startread = float(startread)
                endread = float(endread)

                rental_fee = 0
                mileage_charge = 0

                driven_km = endread-startread
                dailycharge = days*60
                rental_fee += dailycharge
                avg_km = driven_km/days

                if avg_km > 80:
                    total_km = days*80
                    driven_above = driven_km-total_km
                    mileage_charge += (driven_above* 0.25)
                    rental_fee += mileage_charge


                output = "Daily Charge : ${} \n Mileage_charge : ${} \n Rental_fee : ${}".format(dailycharge,mileage_charge,
                                                                                                 rental_fee)
                self.plainTextEdit.setPlainText(output)
                # print(output)

            except Exception:
                self.invalid_input()


    def clear_all(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Days"))
        self.label_2.setText(_translate("Dialog", "Reading at Start"))
        self.label_3.setText(_translate("Dialog", "Reading at End "))
        self.pushButton.setText(_translate("Dialog", "Calculate Fee"))
        self.pushButton_2.setText(_translate("Dialog", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
