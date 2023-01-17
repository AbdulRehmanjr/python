# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:48:19 2022

@author: Najeeb Ur Rehmab, Assistant Porfessor, University of Gujrat
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:10:01 2022

@author: Najeeb Ur Rehmab, Assistant Porfessor, University of Gujrat
"""

from PyQt6.QtWidgets import (
    QGroupBox,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QRadioButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QApplication,
    QFormLayout,
    QDateEdit,
    QPushButton,
    #QPlainTextDocumentLayout,
    #QTextDocument,
)

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit,QFormLayout



class MyMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout()
        self.num1 = QLineEdit()
        self.num2 = QLineEdit()
        self.answer = QLabel()
        self.answer.setText("")
        self.calc = QPushButton("Calculate")
        self.calc.setToolTip('This is a <b>QPushButton</b> widget. <br>Click Here to Calculate')
        
        self.layout.addRow("Number 1",self.num1)
        self.layout.addRow("Number 2",self.num2)
        self.layout.addRow(self.answer)
        
        self.layout.addRow(self.calc)
        
        self.calc.clicked.connect(self.testClick)
        self.setLayout(self.layout)
        
    def testClick(self):
            print("Button Clicked")
            print(self.num1.text())
            print(self.num2.text())

            a = int(self.num1.text())
            b = int(self.num2.text())
            sum = a + b
            print("Sum is ",sum)
            text = str(sum) + " = " + str(a) +" + " + str(b)
            self.answer.setText(text)
            #calc.setText("Press to clear")

application = QApplication([])
mainWindwo = MyMainWindow()


mainWindwo.show()
application.exec()