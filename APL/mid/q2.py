import sys
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication,QWidget,
    QFormLayout,QPushButton,
    QLineEdit,QMenuBar,
    QMainWindow,QLabel,
    QComboBox
    )
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt
# class for window
class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        #seti
        # ng form layout
        self.mainLayout = QFormLayout()
        #intializing the variables
        self.city_list = ['Ghakhar Mandi','Gujranwala','Gujrat','Sialkot','Wazirabad','Kharian','Islamabad']
        self.gender_list = ['Male','Female','Other']
        self.name = QLineEdit()
        self.roll_no = QLineEdit()
        self.gender = QComboBox()
        self.city = QComboBox()
        self.remarks = QLineEdit()
        self.label = QLabel()
        # adding list 
        self.city.addItems(self.city_list)    
        self.gender.addItems(self.gender_list)    
        # adding menubar
        self.menu_bar = QMenuBar()
        self.action_new = QAction("New",self)
        self.action_view = QAction("View",self)
        self.action_exit = QAction("Exit",self)
        # self.action_view.triggered.connect(self.view)
        self.menu_bar.addAction(self.action_new)
        self.menu_bar.addAction(self.action_view)
        self.menu_bar.addAction(self.action_exit)
        # adding menubar to layout
        self.mainLayout.addWidget(self.menu_bar)
        #setting the form
        self.mainLayout.addRow("Name",self.name)
        self.mainLayout.addRow("Roll No.",self.roll_no)
        self.mainLayout.addRow("Gender",self.gender)
        self.mainLayout.addRow("City",self.city)
        self.mainLayout.addRow("Remarks",self.remarks)
        # making button
        self.save_btn = QPushButton("Save")
        self.reset_btn = QPushButton("Reset")
        self.save_btn.setFixedSize(50,50)
        self.reset_btn.setFixedSize(50,50)
        #connect functions
        self.save_btn.clicked.connect(self.save_action)
        self.reset_btn.clicked.connect(self.reset_action)
        # adding button
        self.mainLayout.addWidget(self.save_btn)
        self.mainLayout.addWidget(self.reset_btn)
        self.mainLayout.addWidget(self.label)
        # aadding form layout
        self.setLayout(self.mainLayout)
    
    # funcations
    def view(self):
        print('clicked')
        self.read_from_file()
        
    def read_from_file(self):
        with open('./data.csv','r') as file:
            data = file.readlines()
        for d in data:
            self.label.setText(d)
            
    def save_in_file(self,data):
        with open('./data.csv','a') as file:
            file.write(str(data)+'\n')
            
    def save_action(self):
        name = self.name.text()
        roll = self.roll_no.text()
        gender = str(self.gender.currentText())
        city =  str(self.city.currentText())
        remark = self.remarks.text()
        print(f"{name},{roll},{gender},{city},{remark}")
        data = name,roll,gender,city,remark
        self.save_in_file(data)
        
    def reset_action(self):
        self.name.setText('')
        self.roll_no.setText('')
        self.remarks.setText('')
        
#start of main
if __name__ == '__main__':
    application = QApplication([])
    # object of MainWindow class
    window = MainWindow()    
    window.setWindowTitle("Survey")
    window.setGeometry(250,150,700,400)
    window.show()
    sys.exit(application.exec())
