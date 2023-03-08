import sys
from PyQt6 import QtCore,QtGui,QtWidgets,uic
from PyQt6.QtCore import Qt
from random import randint

class graphic(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.last_x, self.last_y = None, None
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(500,400)
        canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        # self.draw_triangle()        
        # self.draw_pentagon()
        # self.draw_rand_points()
        # self.draw_rectangle()
        # self.draw_circle()
        self.quiz()
        
    def quiz(self):
        canvas = self.label.pixmap()
        
        
        painter = QtGui.QPainter(canvas)
        
        pen = QtGui.QPen()
        pen.setWidth(2)
        painter.setPen(pen)
        
        painter.drawRect(50,100,100,75)
        painter.drawLine(100,50,50,100)
        painter.drawLine(100,50,150,100)
        painter.drawLine(150,100,200,90)
        painter.drawLine(150,175,200,165)
        painter.drawLine(200,165,200,90)
        painter.drawLine(100,50,175,50)
        painter.drawLine(200,90,175,50)
        
        painter.drawEllipse(80,125,30,30)
        
        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(40)
        painter.setFont(font)

        painter.drawText(200, 250, 'Happy Quiz')


        painter.end()
        self.label.setPixmap(canvas)
        
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
        pen.setColor(QtGui.QColor(204,0,0))
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
    
    def draw_rectangle(self):
    
        canvas = self.label.pixmap()
        # rect
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#376F9F"))
        painter.setPen(pen)
        painter.drawRect(40,40,100,100)
        painter.end()
        # rounded
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#3FF89F"))
        painter.setPen(pen)
        painter.drawRoundedRect(200, 40, 100, 100, 10, 10)
        painter.end()
        self.label.setPixmap(canvas)
    def draw_circle(self):
        canvas = self.label.pixmap()
        # circle
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor("#65c5c4"))
        painter.setPen(pen)
        painter.drawEllipse(QtCore.QPoint(250,250),100,100)
        painter.end()
        
        painter = QtGui.QPainter(canvas)

        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor('#4f5a5b'))
        painter.setPen(pen)

        font = QtGui.QFont()
        font.setFamily('Seriaf')
        font.setBold(True)
        font.setPointSize(20)
        painter.setFont(font)

        painter.drawText(180, 250, 'BY SPY101')
        painter.end()
        self.label.setPixmap(canvas)

    
    # def mouseMoveEvent(self, e):
    #     canvas = self.label.pixmap()
    #     painter = QtGui.QPainter(canvas)
    #     painter.drawPoint(int(e.position().x()), int(e.position().y()))
    #     painter.end()
    #     self.label.setPixmap(canvas)
     

    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = int(e.position().x())
            self.last_y = int(e.position().y())
            return # Ignore the first time.

        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        painter.drawLine(int(self.last_x), int(self.last_y), int(e.position().x()), int(e.position().y())) #type: ignore
        painter.end()
        self.label.setPixmap(canvas)

        # Update the origin for next time.
        self.last_x = e.position().x()
        self.last_y = e.position().y()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None
    
if __name__ =='__main__':
    application = QtWidgets.QApplication(sys.argv)
    window = graphic()
    window.show()
    sys.exit(application.exec())