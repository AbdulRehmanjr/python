import sys
from PyQt6 import QtCore,QtGui,QtWidgets,uic
from PyQt6.QtCore import Qt


class graphic(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(600,400)
        canvas.fill(Qt.GlobalColor.yellow)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        # self.draw_triangle()        
        self.draw_pentagon()
        # self.draw_rand_points()
    def draw_triangle(self):
        canvas = self.label.pixmap()
        # simple
        painter = QtGui.QPainter(canvas)
        painter.drawLine(50,10,500,200)
        painter.end()
        # QLine
        painter = QtGui.QPainter(canvas)
        line = QtCore.QLine(50,10,50,200)
        painter.drawLine(line)
        painter.end()
        # points
        painter = QtGui.QPainter(canvas)
        p1,p2 = QtCore.QPoint(50,200),QtCore.QPoint(500,200)
        painter.drawLine(p1,p2)
        painter.end()
        self.label.setPixmap(canvas)
        
    def draw_rand_points(self):
        from random import randint, choice
        colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        painter.setPen(pen)

        for _ in range(10000):
            # pen = painter.pen() you could get the active pen here
            pen.setColor(QtGui.QColor(choice(colors)))
            painter.setPen(pen)
            painter.drawPoint(
                200+randint(-100, 100),  # x
                150+randint(-100, 100)   # y
                )
        painter.end()
        self.label.setPixmap(canvas)
    
    def draw_pentagon(self):
        '''By SPY101'''
        canvas = self.label.pixmap()
        # line 1
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        painter.setPen(pen)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)
        p1,p2 = QtCore.QPoint(100,160),QtCore.QPoint(300,60)
        painter.drawLine(p1,p2)
        painter.end()
        #line 2 
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        painter.setPen(pen)
        pen.setColor(QtGui.QColor('blue'))
        painter.setPen(pen)
        p1,p2 = QtCore.QPoint(300,60),QtCore.QPoint(500,160)
        painter.drawLine(p1,p2)
        painter.end()
        #line 3 
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        painter.setPen(pen)
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)
        p1,p2 = QtCore.QPoint(100,160),QtCore.QPoint(100,350)
        painter.drawLine(p1,p2)
        painter.end()
        #line 4 
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        painter.setPen(pen)
        pen.setColor(QtGui.QColor('orange'))
        painter.setPen(pen)
        p1,p2 = QtCore.QPoint(100,350),QtCore.QPoint(500,350)
        painter.drawLine(p1,p2)
        painter.end()
        #line 5 
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        painter.setPen(pen)
        pen.setColor(QtGui.QColor('#54f4e4'))
        painter.setPen(pen)
        p1,p2 = QtCore.QPoint(500,350),QtCore.QPoint(500,160)
        painter.drawLine(p1,p2)
        painter.end()
        
        # text 
        painter = QtGui.QPainter(canvas)

        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(200, 250, 'BY SPY101')
        painter.end()
        self.label.setPixmap(canvas)
        
        
if __name__ =='__main__':
    application = QtWidgets.QApplication([])
    window = graphic()
    window.show()
    sys.exit(application.exec())