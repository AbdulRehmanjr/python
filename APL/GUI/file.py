import sys
from PyQt6.QtWidgets import (
    QApplication,QWidget,
    QGridLayout,QVBoxLayout,
    QFormLayout,QHBoxLayout,
    QPushButton,QLineEdit,
    QTableWidget
    )
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
# class for window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.formLayout= QFormLayout()
        self.sr = QLineEdit()
        self.name = QLineEdit()
        self.roll = QLineEdit()
        self.table = QTableWidget()
        self.setLayout(self.formLayout)
        self.addSection()
        self.addButton = QPushButton("Add")
        self.addButton.clicked.connect(self.actionButton)# type: ignore   
        self.showButton = QPushButton("Show")
        self.showButton.clicked.connect(self.displayData)# type: ignore   
        self.formLayout.addRow(self.addButton)
    def addSection(self):
        self.formLayout.addRow("Enter Sr",self.sr)
        self.formLayout.addRow("Enter Name",self.name)
        self.formLayout.addRow("Enter Roll",self.roll)
    def actionButton(self):
        sr = self.sr.text()
        name = self.name.text()
        roll = self.roll.text()
        file = open('../files/info1.txt','a')
        file.write(str(sr+" "+" "+name+" "+roll+"\n"))
        file.close()
    def display(self):

        pass
#start of main
if __name__ == '__main__':
    application = QApplication([])
    # object of MainWindow class
    window = MainWindow()    
    window.setWindowTitle("Simple Calculator")
    window.setGeometry(250,150,700,400)
    window.show()
    sys.exit(application.exec())
