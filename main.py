from random import randint
import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic

class Example(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.count = 0
        self.btn = self.pushButton
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.count == 1:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(randint(1, 250), randint(1, 250), randint(1, 250), randint(1, 250))
            qp.end()
        

    def paint(self):
        self.count = 1
        self.update()

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
