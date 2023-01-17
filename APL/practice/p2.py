import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a button to open the second window
        self.button = QPushButton("Open Second Window", self)
        self.button.clicked.connect(self.open_second_window)

        # Set the layout and show the main window
        self.setCentralWidget(self.button)
        self.show()
        
    def open_second_window(self):
        self.second_window = QDialog()
        self.second_window.setWindowTitle("Second Window")
        self.second_window.show()
        
    def open_third_window(self):
        self.third_window = QDialog()
        self.third_window.setWindowTitle("Third Window")
        self.third_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
