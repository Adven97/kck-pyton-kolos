import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_widget = App()
        self.setCentralWidget(self.form_widget)

        self.setWindowTitle('Kolokwium')
        self.setGeometry(1, 1, 1600, 1200)
        # self.setWindowIcon(QIcon('tc.png'))


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def selectionchange(self):
        self.pic.setPixmap(QPixmap("img/"+self.combobox.currentText()).scaled(1100, 1100, Qt.KeepAspectRatio))
        # self.pic.setAlignment(Qt.AlignCenter.scaled(500, 600, Qt.KeepAspectRatio))

    def initUI(self):

        accepted_extensions = ["jpg", "png"]
        filenames = [fn for fn in os.listdir("./img/") if fn.split(".")[-1] in accepted_extensions]

        vmain = QGridLayout()

        upbar = QHBoxLayout()
        self.pic = QLabel(self)
        self.pic.setPixmap(QPixmap("img/1.jpg").scaled(1100, 1100, Qt.KeepAspectRatio))
        self.pic.setAlignment(Qt.AlignCenter)
        upbar.addWidget(self.pic)



        self.model = QFileSystemModel()
        self.model.setRootPath('')


        vlayout = QHBoxLayout()
        self.combobox = QComboBox()
        for ff in filenames:
            self.combobox.addItem(ff)
        # self.combobox.addItem("10")
        # self.combobox.addItem("11")
        # self.combobox.addItem("12")
        # self.combobox.addItem("14")
        # self.combobox.addItem("16")
        # self.combobox.addItem("18")
        # self.combobox.addItem("20")
        # self.combobox.addItem("22")
        # self.combobox.addItem("24")
        # self.combobox.addItem("26")
        # self.combobox.addItem("28")
        # self.combobox.addItem("30")
        self.combobox.currentIndexChanged.connect(self.selectionchange)
        vlayout.addWidget(self.combobox)

        vmain.addLayout(upbar,0,0)
        vmain.addLayout(vlayout,1,0)

        self.setLayout(vmain)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    ex.show()
    sys.exit(app.exec_())
