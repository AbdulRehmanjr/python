import sys

from PyQt6.QtWidgets import (QWidget,QApplication,QFileDialog,QVBoxLayout
,QPushButton
                             )
from PyQt6.QtCore import Qt,QFile,QTextStream
from random import randint


class graphic(QWidget):
    def __init__(self):
        super().__init__()
        self.v_layout = QVBoxLayout()
        self.setGeometry(200,300,800,300) 
        

        # Add a button to open the file dialog
        self.button = QPushButton("Select File", self)
        self.button.clicked.connect(self.open_file_dialog)
        self.v_layout.addWidget(self.button)

    
    def open_file_dialog(self):
        # Open the file dialog
        filename, _ = QFileDialog.getOpenFileName(self, "Select File")
        print('filename',filename)
        if filename:
            # Read the contents of the file
            file = QFile(filename)
            file.open(open,'r')

            stream = QTextStream(file)
            content = stream.readAll()        
            file.close()
if __name__ =='__main__':
    application = QApplication(sys.argv)
    window = graphic()
    window.show()
    sys.exit(application.exec())