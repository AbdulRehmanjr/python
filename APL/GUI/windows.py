import sys
from PyQt6.QtWidgets import QApplication,QLabel,QWidget,QCheckBox

app = QApplication([])
window1 = QWidget()
# window2 = QWidget()
helloMsg = QLabel('<h1>Hello World</h1>',parent=window1)
# NameMsg = QLabel('<h1>Abdul Rehman</h1>',parent=window2)
RollMsg = QLabel('<h1>200215191-101</h1>',parent=window1)
checkBox = QCheckBox('hello',parent=window1)
print(type(helloMsg))
RollMsg.style()
helloMsg.move(0,0)
# NameMsg.move(0,50)
RollMsg.move(0,100)
window1.setWindowTitle("Abdul Rehman")
window1.setGeometry(250,250,500,300)
# window2.setWindowTitle("Abdul Rehman")
# window2.setGeometry(250,250,500,300)
#show screen
window1.show()
# window2.show()
sys.exit(app.exec())
