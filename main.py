#!/urs/bin/python3
#-*- coding: utf-8 -*-

import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic


class App(QWidget):
    def __init__(self):
        self.start()

    def start(self):
        self.ui = uic.loadUi('calc.ui')
        self.ui.show()












if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()