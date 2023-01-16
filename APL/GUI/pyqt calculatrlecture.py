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
'''
def findSum():
    sum = int(num1)+int(num2)
    print("Sum is ",sum)

'''

def testClick():
    print("Button Clicked")
    print(num1.text())
    print(num2.text())
    
    a = int(num1.text())
    b = int(num2.text())
    sum = a + b
    print("Sum is ",sum)
    text = str(sum) + " = " + str(a) +" + " + str(b)
    answer.setText(text)
    #calc.setText("Press to clear")
    
    
    
    
application = QApplication([])
mainWindwo = QWidget()
mainWindwo.setWindowTitle("My Calculator")

layout = QFormLayout()

#layout.addRow("Roll #", QLineEdit())
#layout.addRow("Name #", QLineEdit())
#layout.addRow("Remarks #", QPlainTextEdit())
#layout.addRow( QPushButton("Save"))

#num1 = input("Enter number 1:")
#num2 = input("Enter number 1:")

num1 = QLineEdit()
num2 = QLineEdit()
answer = QLabel()
answer.setText("")

calc = QPushButton("Calculate")

calc.setToolTip('This is a <b>QPushButton</b> widget. <br>Click Here to Calculate')


layout.addRow("Number 1",num1)
layout.addRow("Number 2",num2)
layout.addRow(answer)

layout.addRow(calc)

#findSum()

calc.clicked.connect(testClick)

mainWindwo.setLayout(layout)
mainWindwo.show()
application.exec()


