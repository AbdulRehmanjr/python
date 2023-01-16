import sys
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication,QWidget,
    QFormLayout,QDateEdit,
    QPushButton,QLabel
                             )


# class for window
class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        # intializing the required Objects
        self.layout = QFormLayout()  # type: ignore
        self.date = QDateEdit()
        self.result = QLabel()
        self.result.setText("")
        self.calc = QPushButton("Calculate")
        
        self.layout.addRow("Enter the DOB",self.date)
        self.layout.addRow(self.result)
        self.layout.addRow(self.calc)
        self.calc.clicked.connect(self.calAge)
        #set layout
        self.setLayout(self.layout)
    def calAge(self):
        print(self.date.text())
        userInput = datetime.strptime(self.date.text(),"%d/%m/%Y")        
        currentTime = datetime.today()
        age = int(str(currentTime - userInput).split(" ")[0])//365
        format = f"<b>Your Age is {age}</b>"
        self.result.setText(format)
        
    



#start of main
if __name__ == '__main__':
    application = QApplication([])
    # object of MainWindow class
    window = MainWindow()    
    window.setWindowTitle("Age Calculator")
    window.setGeometry(250,250,500,300)
    window.show()
    sys.exit(application.exec())
