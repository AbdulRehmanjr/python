'''
@AUTHOR SPYDEV_101 
'''
import sys
from PyQt6.QtWidgets import (
    QApplication,QWidget,QVBoxLayout,QLabel,
    QFormLayout,QLineEdit,QPushButton,
    QGridLayout,QDialog,QListWidget,
    QTableWidget,QTableWidgetItem
                             )

class mainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # main layout
        self.mainlayout = QVBoxLayout()
        #label 1-2 
        self.label = QLabel()
        self.label.setText('Hello I am Abdul Rehman')
        self.label1 = QLabel()
        self.label1.setText('Hello I am Abdul Rehman 101')
        #line input box
        self.inputLine = QLineEdit()
        #formlayout for form inputs
        self.formlayout = QFormLayout()
        self.formlayout.addRow('hello input ',self.inputLine)
        
        #adding button 
        self.button = QPushButton('click me ')
        self.button.clicked.connect(self.action)
        self.button1 = QPushButton('show window ')
        self.button1.clicked.connect(self.childWindow)
        # grid layout for buttons
        self.grid = QGridLayout()
        self.grid.setColumnStretch(1,1)
        self.grid.setColumnStretch(2,2)
        self.grid.addWidget(self.button)
        self.grid.addWidget(self.button1)
        # adding things and layout to main vBox layout 
        self.mainlayout.addWidget(self.label)
        self.mainlayout.addWidget(self.label1)
        self.mainlayout.addLayout(self.formlayout)
        self.mainlayout.addLayout(self.grid)
        # setting layout of classs as it import QWidgets if not then make a onject and import in it
        self.setLayout(self.mainlayout)
        
    def childWindow(self):
        self.second_window = QWidget()
        self.second_window.setWindowTitle("Second Window")
        self.second_window.show()
        self.second_window_layout = QVBoxLayout()
        self.list = QTableWidget()
        self.list.setHorizontalHeaderLabels(['name','age','address'])
        
        self.list.setItem(0,0,QTableWidgetItem('Abdul Rehman') )
        self.list.setItem(0,1,QTableWidgetItem('22') )
        self.list.setItem(0,2,QTableWidgetItem('ghakhar'))
        self.list.setShowGrid(True)
        # self.list.setHorizontalHeader() # type: ignore
        self.second_window_layout.addWidget(self.list)
        self.second_window.setLayout(self.second_window_layout)
        
    def action(self):
        print(self.inputLine.text())
if __name__ =='__main__':
    
    application = QApplication(sys.argv) # you can pass [] or agrv like sys
    
    window = mainWindow()
    window.setGeometry(300,100,400,400)
    window.setWindowTitle('Mid term practice')
    window.show()
    print(sys.argv)
    # print(application.arguments.__str__)
    sys.exit(application.exec())
    