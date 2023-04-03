#!/urs/bin/python3
#-*- coding: utf-8 -*-

from PyQt6 import QtWidgets
from calc import Ui_w_app
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_w_app()
        self.ui.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

application = mywindow()
application.show()

sys.exit(app.exec())