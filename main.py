import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import os

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main.ui', self)
        self.driverBtn.clicked.connect(self.run_driver)
        self.parserBtn.clicked.connect(self.run_parser)
        self.autoLaunchBtn.clicked.connect(self.run_auto_launcher)
        self.numberLineEdit.textChanged.connect(self.get_number)
        self.comboBox.currentIndexChanged.connect(self.get_type)

    def run_driver(self):
        os.system("ping www.google.com")

    def run_parser(self):
        os.system("ping www.google.com")

    def run_auto_launcher(self):
        os.system("ping www.google.com")

    def get_number(self):
        if not hasattr(self, 'value'):
            self.value = ''

        if self.numberLineEdit.text().isdigit():
            self.value = self.numberLineEdit.text()

        elif self.numberLineEdit.text() != self.value:
            if self.numberLineEdit.text() == '':
                self.value = ''
            self.numberLineEdit.setText(self.value)

    def get_type(self, index):
        print(self.comboBox.itemText(index))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
