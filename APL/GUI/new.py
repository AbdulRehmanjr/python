import sys
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication,QWidget,
    QGridLayout,QVBoxLayout,
    QFormLayout,QHBoxLayout,
    QPushButton,QLineEdit,
    QMenuBar,QMenu,QTextEdit
    )
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        # intializing the required Objects`s
        self.formLayout = QFormLayout()
        self.mainGridLayout = QHBoxLayout()
        self.mainLayout = QVBoxLayout()
        self.numericGrid = QGridLayout()
        self.actionGrid = QGridLayout()
        self.menu= self.menuBar()
        #input box
        self.inputBox = self.SetInputBox(650,60,30)
        # buttons list
        self.numericButtons = [1,2,3,4,5,6,7,8,9,0]
        self.operationButtons = ['/','*','+','-','(',')','=','DEL','CLR']
        self.actionedButtons = []
        #======setting layouts
        self.formLayout.addWidget(self.menu)
        self.formLayout.addWidget(self.inputBox)
        self.setButtonGrid(self.operationButtons)
        self.setButtonGrid(self.numericButtons)
        self.addAction(self.actionedButtons)
        self.mainLayout.addLayout(self.formLayout)
        self.mainGridLayout.addLayout(self.numericGrid)
        self.mainGridLayout.addLayout(self.actionGrid)
        self.mainLayout.addLayout(self.mainGridLayout)
        self.setLayout(self.mainLayout)
        self.text = QTextEdit()
        self.text.toPlainText()
    # history saving
    def history(self,data):
        currentDate = str(datetime.now())
        file = open('../files/history.txt','a')
        file.write(data+" "+currentDate+"\n")
        file.close()
    # setting menuBar
    def menuBar(self) -> QMenuBar:
        menu = QMenuBar()
        menu.addMenu("History")
        menu.show()
        return menu
    # setting input box
    def SetInputBox(self,width,height,fontSize)->QLineEdit:
        '''Set the Input Box with given width height fontsize'''
        inputBox = QLineEdit()
        inputBox.setReadOnly(True)
        inputBox.setAlignment(Qt.AlignmentFlag.AlignRight)
        inputBox.setStyleSheet(f"width:{width};height:{height};color:black;font-size:30px;border:2px solid black;")
        inputBox.setText("")
        return inputBox
    #set the buttons
    def setButtonGrid(self,buttonList):
        
        ''' Set the buttons'''
        if '/' in buttonList:
            self.actionGrid.setColumnStretch(2,0)
            for button in buttonList:
                addButton = QPushButton(str(button),self)
                addButton.setStyleSheet('color:white;background-color:black;font-size:25px;font-weight:bold;border:2px solid black;border-radius:35px;')
                addButton.setFixedWidth(70)
                addButton.setFixedHeight(70)
                self.actionedButtons.append(addButton)
                self.actionGrid.addWidget(addButton)
        else:
            self.numericGrid.setColumnStretch(2,0)
            for button in self.numericButtons: 
                addButton = QPushButton(str(button),self)
                addButton.setStyleSheet('font-size:25px;font-weight:bold;border:2px solid black;border-radius:35px;')
                addButton.setFixedWidth(70)
                addButton.setFixedHeight(70)
                self.actionedButtons.append(addButton)
                self.numericGrid.addWidget(addButton)
                
    def addAction(self,allButtons):
    
        '''Adding action to buttons'''
        for action in allButtons:
            action.clicked.connect(self.actionButton)
            
    #action for button
    def actionButton(self):
        
        '''Add Action to buttons'''
        prevInput = self.inputBox.text()
        newInput = self.sender().text() # type: ignore
        if newInput == '=':
            try:
                calculation = str(eval(prevInput))
                data = prevInput + " = "+ calculation
                self.inputBox.setText(calculation)
                self.history(data)
            except SyntaxError:
                self.inputBox.setText("Error")
            except ZeroDivisionError:
                self.inputBox.setText("Error")
        elif newInput == 'DEL':
            self.inputBox.setText("")
        elif newInput == 'CLR':
            try:
                prevInput = prevInput.removesuffix(prevInput[-1])
                self.inputBox.setText(prevInput)
            except IndexError as error:
                print(error)
        else:    
            self.inputBox.setText(prevInput+newInput)        
            
if __name__ == '__main__':
    application = QApplication([])
    # object of MainWindow class
    window = MainWindow()    
    window.setWindowTitle("Age Calculator")
    window.setGeometry(250,250,500,300)
    window.show()
    sys.exit(application.exec())