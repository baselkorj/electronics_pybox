from PyQt5 import QtCore, QtGui, QtWidgets

# Create Variables
# Color List: [black, brown, red, orange, yellow, green, blue, purple, grey, white, silver, gold]
colors = ["#000000", "#8B4513", "#B22222", "#FF8C00", "#FFD700", "#6B8E23", "#4682B4", "#800080", "#696969", "#F5F5F5", "#DAA520", "#C0C0C0"]
s1_color = 2
s2_color = 6
s3_color = 5
s4_color = 3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(391, 300)

        # 1st Up
        self.one_up = QtWidgets.QPushButton(Dialog)
        self.one_up.setGeometry(QtCore.QRect(140, 40, 21, 21))
        self.one_up.setObjectName("one_up")

        # 1st Band
        self.stripe_1 = QtWidgets.QFrame(Dialog)
        self.stripe_1.setGeometry(QtCore.QRect(140, 70, 21, 61))
        self.stripe_1.setStyleSheet("background-color: " + colors[s1_color] + ";")
        self.stripe_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stripe_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stripe_1.setObjectName("stripe_1")

        # 1st Down
        self.one_down = QtWidgets.QPushButton(Dialog)
        self.one_down.setGeometry(QtCore.QRect(140, 140, 21, 21))
        self.one_down.setObjectName("one_down")

        # 2nd Up
        self.two_up = QtWidgets.QPushButton(Dialog)
        self.two_up.setGeometry(QtCore.QRect(170, 40, 21, 21))
        self.two_up.setObjectName("two_up")

        # 2nd Band
        self.stripe_2 = QtWidgets.QFrame(Dialog)
        self.stripe_2.setGeometry(QtCore.QRect(170, 70, 21, 61))
        self.stripe_2.setStyleSheet("background-color: " + colors[s2_color] + ";")
        self.stripe_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stripe_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stripe_2.setObjectName("stripe_2")

        # 2nd Down
        self.two_down = QtWidgets.QPushButton(Dialog)
        self.two_down.setGeometry(QtCore.QRect(170, 140, 21, 21))
        self.two_down.setObjectName("two_down")

        # 3rd Up
        self.three_up = QtWidgets.QPushButton(Dialog)
        self.three_up.setGeometry(QtCore.QRect(200, 40, 21, 21))
        self.three_up.setObjectName("three_up")

        # 3rd Band
        self.stripe_3 = QtWidgets.QFrame(Dialog)
        self.stripe_3.setGeometry(QtCore.QRect(200, 70, 21, 61))
        self.stripe_3.setStyleSheet("background-color: " + colors[s3_color] + ";")
        self.stripe_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stripe_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stripe_3.setObjectName("stripe_3")

        # 3rd Down
        self.three_down = QtWidgets.QPushButton(Dialog)
        self.three_down.setGeometry(QtCore.QRect(200, 140, 21, 21))
        self.three_down.setObjectName("three_down")

        # 4th Up
        self.four_up = QtWidgets.QPushButton(Dialog)
        self.four_up.setGeometry(QtCore.QRect(230, 40, 21, 21))
        self.four_up.setObjectName("four_up")

        # 4th Band
        self.stripe_4 = QtWidgets.QFrame(Dialog)
        self.stripe_4.setGeometry(QtCore.QRect(230, 70, 21, 61))
        self.stripe_4.setStyleSheet("background-color: " + colors[s4_color] + ";")
        self.stripe_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stripe_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stripe_4.setObjectName("stripe_4")

        # 4th Down
        self.four_down = QtWidgets.QPushButton(Dialog)
        self.four_down.setGeometry(QtCore.QRect(230, 140, 21, 21))
        self.four_down.setObjectName("four_down")

        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.four_down.setFont(font)
        

        # Calculate Button
        self.calculate = QtWidgets.QPushButton(Dialog)
        self.calculate.setGeometry(QtCore.QRect(150, 250, 86, 32))
        self.calculate.setObjectName("calculate")
        
        # Resistor Value Label
        self.res_value = QtWidgets.QLabel(Dialog)
        self.res_value.setGeometry(QtCore.QRect(0, 190, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.res_value.setFont(font)
        self.res_value.setAlignment(QtCore.Qt.AlignCenter)
        self.res_value.setObjectName("res_value")

        # Resistor Body
        self.res_background = QtWidgets.QFrame(Dialog)
        self.res_background.setGeometry(QtCore.QRect(120, 70, 151, 61))
        self.res_background.setStyleSheet("background-color: rgb(159, 159, 159);")
        self.res_background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.res_background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.res_background.setObjectName("res_background")

        # Left Lead
        self.lead_left = QtWidgets.QFrame(Dialog)
        self.lead_left.setGeometry(QtCore.QRect(80, 90, 41, 21))
        self.lead_left.setStyleSheet("background-color: rgb(194, 129, 0);")
        self.lead_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lead_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lead_left.setObjectName("lead_left")

        # Right Lead
        self.lead_right = QtWidgets.QFrame(Dialog)
        self.lead_right.setGeometry(QtCore.QRect(270, 90, 41, 21))
        self.lead_right.setStyleSheet("background-color: rgb(194, 129, 0);")
        self.lead_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lead_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lead_right.setObjectName("lead_right")

        # Combo Box
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 250, 87, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        # Exit Button
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(280, 250, 86, 32))
        self.exit.setObjectName("exit")

        # Raise Functions
        self.res_background.raise_()
        self.one_up.raise_()
        self.one_down.raise_()
        self.two_up.raise_()
        self.three_up.raise_()
        self.four_up.raise_()
        self.two_down.raise_()
        self.three_down.raise_()
        self.four_down.raise_()
        self.calculate.raise_()
        self.res_value.raise_()
        self.stripe_2.raise_()
        self.stripe_1.raise_()
        self.stripe_3.raise_()
        self.stripe_4.raise_()
        self.lead_left.raise_()
        self.lead_right.raise_()
        self.comboBox.raise_()
        self.exit.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Add Text to Widgets
    # Created in a separate function to allow for Translations
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Electronics PyBox"))
        self.one_up.setText(_translate("Dialog", "▲"))
        self.one_down.setText(_translate("Dialog", "▼"))
        self.two_up.setText(_translate("Dialog", "▲"))
        self.three_up.setText(_translate("Dialog", "▲"))
        self.four_up.setText(_translate("Dialog", "▲"))
        self.two_down.setText(_translate("Dialog", "▼"))
        self.three_down.setText(_translate("Dialog", "▼"))
        self.four_down.setText(_translate("Dialog", "▼"))
        self.calculate.setText(_translate("Dialog", "Calculate"))
        self.res_value.setText(_translate("Dialog", "220kΩ"))
        self.comboBox.setItemText(0, _translate("Dialog", "Four"))
        self.comboBox.setItemText(1, _translate("Dialog", "Five"))
        self.comboBox.setItemText(2, _translate("Dialog", "Six"))
        self.exit.setText(_translate("Dialog", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
