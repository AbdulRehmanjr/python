import sys
from datetime import datetime

from PyQt6.QtWidgets import (
    QApplication,QWidget,
    QFormLayout,QPushButton,
    QLineEdit,QDateEdit,
    QComboBox,QMessageBox
    )

from PyQt6.QtGui import QAction

from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()

        # declaring the form items
        self.id = QLineEdit()
        self.title = QLineEdit()
        self.category = QComboBox()
        self.category.addItem('Programming')
        self.category.addItem('Novel')
        self.category.addItem('Mystery')
        self.publisher = QLineEdit()
        self.issn = QLineEdit()
        self.pubdate = QDateEdit()
        
        self.buttons = ['New','Update','Save','Close']
    
        self.f_layout = QFormLayout()
        
        
        # adding form
        self.f_layout.addRow("Id",self.id)
        self.f_layout.addRow("Title",self.title)
        self.f_layout.addRow("Category",self.category)
        self.f_layout.addRow("Publisher",self.publisher)
        self.f_layout.addRow("ISSN No.",self.issn)
        self.f_layout.addRow("Publish Date",self.pubdate)

        
        
        #validate 
        self.id.editingFinished.connect(self.validate_id)
        self.issn.editingFinished.connect(self.validate_id)

        self.setButtons()
        # setting buttons
        
        self.setLayout(self.f_layout)
        
    def setButtons(self):
        for button in self.buttons:
            btn = QPushButton(button)
            btn.clicked.connect(self.btn_action)
            self.f_layout.addWidget(btn)
    
    def btn_action(self):
        mode = self.sender().text() # type: ignore
        if mode =='Update':
            print('[*] UPDATE')
            _id = self.id.text()
            _title = self.title.text() 
            _category = self.category.currentText() 
            _publisher = self.publisher.text() 
            _issn = self.issn.text() 
            _pubdate = self.pubdate.text()
            
            if not _id or not _title or not _publisher or not _issn:
                message = QMessageBox()
                message.setIcon(QMessageBox.Icon.Warning) 
                message.setText("Please Enter all fields")
                message.exec()
                
            print(f"[*] Data: {_id},{_title},{_category},{_publisher},{_issn},{_pubdate}")  
        else:
            button = QMessageBox.warning(self, 'Warning','All Changed will be undo')
            
            if button == QMessageBox.StandardButton.Ok:
                print("[*] Undo Changes")

                self.id.setText('')
                self.title.setText('') 
                
                self.publisher.setText('')
                self.issn.setText('') 
        
                
    def validate_id(self):
        id_text = self.id.text()
        if not id_text.isdigit():
            message = QMessageBox()
            message.setIcon(QMessageBox.Icon.Warning) # set warning icon
            message.setText("Invalid ID. Please enter a valid integer.")
            message.exec()
            self.id.clear()          
                 

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MainWindow()    
    window.setWindowTitle("Form 1")
    window.setGeometry(400,100,500,600)
    window.show()
    sys.exit(application.exec())
