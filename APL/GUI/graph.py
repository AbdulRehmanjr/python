import sys
from random import randint,choice
    
from PyQt6.QtWidgets import (
    QApplication,QMainWindow,QFormLayout,QLabel   )
from PyQt6.QtCore import (Qt,QRect)
from  PyQt6.QtGui import (QPixmap,QPainter,QPen,QColor,QBrush)

# class for window
class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        canvas = QPixmap(400, 300)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        # self.draw_something()
        #self.draw_points()
        self.draw_rec()
    def draw_rec(self):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor("#376F9F"))
        painter.setPen(pen)

        brush = QBrush()
        brush.setColor(QColor("#FFD141"))
        brush.setStyle(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)

        painter.drawRects(
        QRect(50, 50, 100, 100),
        QRect(60, 60, 150, 100),
        QRect(70, 70, 100, 150),
        QRect(80, 80, 150, 100),
        QRect(90, 90, 100, 150),
        )
        painter.end()
        self.label.setPixmap(canvas)
        
    def draw_points(self):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(3)
        colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']    
        for n in range(10000):
            pen.setColor(QColor(choice(colors)))    
            painter.setPen(pen)
            painter.drawPoint(
            200+randint(-100, 100),  # x
            150+randint(-100, 100)   # y
            )
        painter.end()
        self.label.setPixmap(canvas)

    def draw_something(self):
        canvas = self.label.pixmap()
        line = QPainter(canvas)
        line.drawLine(10, 10, 300, 200)
        line.end()
        point = QPainter(canvas)
        point.drawPoint(100,200)
        point.end()
        pendraw = QPainter(canvas)
        pen = QPen()
        pen.setWidth(40)
        pen.setColor(QColor('red'))
        pendraw.setPen(pen)
        pendraw.drawPoint(200, 150)
        pendraw.end()
        self.label.setPixmap(canvas)
class Qdesign(Qt):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
#start of main
if __name__ == '__main__':
    application = QApplication([])
    # object of MainWindow class
    window = MainWindow()    
    window.setWindowTitle("Simple Calculator")
    window.setGeometry(250,150,700,400)
    window.show()
    sys.exit(application.exec())
