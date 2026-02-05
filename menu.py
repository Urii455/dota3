import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLabel, QLineEdit
from main import main
from main2 import main2


A = None

class menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.i = True

    def initUI(self):
        self.setGeometry(100, 100, 330, 400)
        self.setWindowTitle('главное меню')

        self.map1 = QPushButton('1 карта', self)
        self.map1.move(100, 10)
        self.map1.resize(60, 40)
        self.map1.clicked.connect(self.game1)

        self.map2 = QPushButton('2 карта', self)
        self.map2.move(170, 10)
        self.map2.resize(60, 40)
        self.map2.clicked.connect(self.game2)

        self.first_value = QLineEdit(self)
        self.first_value.move(145, 60)
        self.first_value.resize(self.first_value.sizeHint())
        self.first_value.resize(50, 20)
        self.first_value.setText('20')



    def game1(self):
        main()
        exit()

    def game2(self):
        main2()
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = menu()
    ex.show()
    sys.exit(app.exec())