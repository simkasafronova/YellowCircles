import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from UI import Ui_MainWindow
from random import randrange, choice

COLORS = [(194, 50, 37), (245, 130, 7), (247, 223, 5), (67, 191, 10),
          (33, 150, 49), (55, 204, 154), (31, 81, 181), (98, 23, 163)]


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start_drawing)
        self.paint_flag = False

    def paintEvent(self, event):
        if self.paint_flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def start_drawing(self):
        self.paint_flag = True
        self.repaint()

    def draw_circle(self, qp):
        width = randrange(10, 100, 10)
        x, y = randrange(100, 400, 20), randrange(100, 300, 20)
        color = choice(COLORS)
        qp.setBrush(QColor(color[0], color[1], color[2]))
        qp.drawEllipse(x, y, width, width)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())