import sys
from PyQt6.QtWidgets import QApplication,QLabel,QWidget,QHBoxLayout,QGridLayout,QVBoxLayout,QFormLayout,QPushButton
app = QApplication([])
window1 = QWidget()
helloMsg = QLabel('<h1>Hello World</h1>',parent=window1)
RollMsg = QLabel('<h5>200215191-101</h5>',parent=window1)
print(type(helloMsg))
# RollMsg.move(0,100)
window1.setWindowTitle("Abdul Rehman")
window1.setGeometry(250,250,500,300)
helloMsg.show()
RollMsg.show()
RollMsg.move(0,40)
horizontalLayout = QHBoxLayout()
gridLayout = QGridLayout()
verticalLayout = QVBoxLayout()
formLayout = QFormLayout()
for i in range(1,5):
    horizontalLayout.addWidget(QPushButton(str(i)))    
for i in range(1,5):
    verticalLayout.addWidget(QPushButton(str(i)))
window1.setLayout(horizontalLayout)
# window1.setLayout(gridLayout)
# window1.setLayout(verticalLayout)
#show screen
window1.show()
# window2.show()
sys.exit(app.exec())
