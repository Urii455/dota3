import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLabel, QLineEdit
from main import main
from main2 import main2

class Arifmometr(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.i = True

    def initUI(self):
        self.setGeometry(100, 100, 330, 400)
        self.setWindowTitle('главное меню')

        self.add_button = QPushButton('1 карта', self)
        self.add_button.move(100, 10)
        self.add_button.resize(60, 40)
        self.add_button.clicked.connect(self.game1)

        self.substract_button = QPushButton('2 карта', self)
        self.substract_button.move(170, 10)
        self.substract_button.resize(60, 40)
        self.substract_button.clicked.connect(self.game2)



    def game1(self):
        main()
        exit()

    def game2(self):
        main2()
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Arifmometr()
    ex.show()
    sys.exit(app.exec())