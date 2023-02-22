import sys
import random
from PyQt6 import QtGui
from PyQt6.QtWidgets import (QWidget,QHBoxLayout,
                             QApplication,QLabel,
                             QVBoxLayout,
                             QPushButton
                             )
from PyQt6.QtGui import (QColor)
from PyQt6.QtCore import Qt
from random import randint

class graphic(QWidget):
    def __init__(self):
        super().__init__()
    
        # attributes 
        self.pen_color = QColor()
        self.pen_size = 0
        self.pen_shape = ''
    
    
    
    
        #setting windows
        self.setWindowTitle("Paint App By SPYDEV")
        self.setGeometry(250,150,700,400)
        
        self.last_x, self.last_y = None, None
        self.canvas_label = QLabel()
        self.canvas = QtGui.QPixmap(600,400)
        self.canvas.fill(Qt.GlobalColor.white)
        self.canvas_label.setPixmap(self.canvas)
        
        self.colors = self.generate_hex_colors(10)
        
        self.pen_width = QVBoxLayout()
        self.main_box = QVBoxLayout()
        self.color_list = QVBoxLayout()
        
        self.h_layout = QHBoxLayout()
        
        
        
        # methods
        self.setColorList()
        self.setPenBlock()
        self.UI()
    
    
        
    
    #seting pen size
    def setPenBlock(self):
        size = [10,20,30,40]
        
        pen = QLabel("Size")
        self.pen_width.addWidget(pen)
        for s in size:

            button = QPushButton(str(s))
            button.setFixedHeight(20)
            button.setStyleSheet(f"color:black;")
            button.clicked.connect(self.getSize)
            
            self.pen_width.addWidget(button)    
            
        shape = QLabel("Shapes")
        shapes = ['Circle','Rectangle']
        self.pen_width.addWidget(shape)
        
        for s in shapes:
            button = QPushButton(s)
            button.setFixedHeight(20)
            button.setStyleSheet(f"color:black;")
            button.clicked.connect(self.getShape)

            self.pen_width.addWidget(button)
            
    def getSize(self):
        self.pen_size = int(self.sender().text()) # type: ignore
        print(self.pen_size)
        
    def getShape(self):
        self.pen_shape = self.sender().text() # type: ignore   
        print(self.pen_shape)
    # generate hexa values for color
    def generate_hex_colors(self,num_colors):
        
        hex_colors = []
        
        for _ in range(num_colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
            hex_colors.append(hex_color)
            
        return hex_colors
    
    #color list 
    def setColorList(self):
        '''Seting the list for colors'''    
        
        for color in self.colors:
            
            button = QPushButton(color)
            button.setFixedHeight(20)
            button.setStyleSheet(f"background-color:{color};color:white;")

            button.clicked.connect(self.getColor)
            
            self.color_list.addWidget(button)

    def getColor(self):
        self.pen_color = self.sender().text() # type: ignore
        print(self.pen_color)
        
    # main UI function
    def UI(self):
        
        '''Setting the main Layout'''
        self.h_layout.addLayout(self.color_list)
        
        self.h_layout.addLayout(self.main_box)
        
        self.h_layout.addLayout(self.pen_width)
        
        # Set main layout for window
        self.setLayout(self.h_layout)

    # mouse Move Event
    def mouseMoveEvent(self, e):
        if self.last_x is None: # First event.
            self.last_x = int(e.position().x())
            self.last_y = int(e.position().y())
            return # Ignore the first time.

        canvas = self.canvas_label.pixmap()
        
        painter = QtGui.QPainter(canvas)
        
        pen = QtGui.QPen()
        pen.setWidth(self.pen_size)
        pen.setColor(QtGui.QColor(self.pen_color))
        
        painter.setPen(pen)
        
        painter.drawLine(int(self.last_x), int(self.last_y), int(e.position().x()), int(e.position().y())) #type: ignore
        painter.end()
        
        self.canvas_label.setPixmap(canvas)

        # Update the origin for next time.
        self.last_x = int(e.position().x())
        self.last_y = int(e.position().y())

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None
    
    
    
    
if __name__ =='__main__':
    application = QApplication(sys.argv)
    window = graphic()
    window.show()
    sys.exit(application.exec())