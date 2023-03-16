import sys

from  PyQt6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QWidget,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
)

from PyQt6 import QtCore, QtGui, QtWidgets


class TableMain(QMainWindow):
    mytable=""
    data = [
            ["20021519-050","Ali","2.3"],
            ["20021519-150","Hassan","3.3"],
            ["20021519-070","Aslam Ali","2.5"],
            ["20021519-080","Akram Ali Cheema","3.3"]
            ]
    dataDic = {'Sessionals':['15','20','17','21'],
        'Midterm':['20','22','18','19'],
        'Final':['35','45','31','48']}

    def __init__(self):
        super().__init__()
        

        self.setWindowTitle("Table Practice")
        self.setFixedSize(500,400)
        
        self.mytable = QTableWidget()

        self.mytable.setRowCount(5)
        self.mytable.setColumnCount(3)
        self.mytable.setHorizontalHeaderLabels(["Roll #", "Name", "GPA"])
        

        #mytable.setItem(0,0,["20021519-001","Ali Hassan",3.9])
        
        #mytable.setItem()
        #self.mytable.setItem(1, 1, ["Test"])
        

        self.mytable.setItem(0, 0, QTableWidgetItem('20021519-001'))
        self.mytable.setItem(0, 1, QTableWidgetItem('Ali Hassan Cheema Gujjar Jutt'))
        self.mytable.setItem(0, 2, QTableWidgetItem("3.5"))
        
        
        for row in range(1,5):
            print(row)
            for col in range(1,3):
                self.mytable.setItem(row, col, QTableWidgetItem("-"))
        
        self.setData()
        self.setDataDict()
        
        self.mytable.setAlternatingRowColors(1)
        self.mytable.resizeColumnsToContents()

        self.setCentralWidget(self.mytable)
        self.mytable.show()
        win = self.frameGeometry()
        pos=QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        win.moveCenter(pos)
        self.move(win.topLeft())
        self.show()
        

    def setData(self):
        for i in self.data:
             print(i[0], i[1], i[2])
        
        row = 1
        for i in self.data:
            self.mytable.setItem(row,0,QTableWidgetItem(i[0]))
            self.mytable.setItem(row,1,QTableWidgetItem(i[1]))
            self.mytable.setItem(row,2,QTableWidgetItem(i[2]))
            row=row+1
        
    def setDataDict(self): 
        horHeaders = []
        for n, key in enumerate(sorted(self.dataDic.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.dataDic[key]):
                newitem = QTableWidgetItem(item)
                self.mytable.setItem(m, n, newitem)
        self.mytable.setHorizontalHeaderLabels(horHeaders)
        


app = QApplication(sys.argv)
window = TableMain()
window.show()
app.exec()
