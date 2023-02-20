import sys
import language_tool_python
from nltk.sentiment.vader import SentimentIntensityAnalyzer


from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QGridLayout, QTextEdit,
                             QLabel,QHBoxLayout,QVBoxLayout)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        
        # attributes
        
        self.grammar = Grammar()
        
        self.grid_left  =QGridLayout()
        self.grid_right  =QGridLayout()
        self.h_layout = QHBoxLayout()
        
        self.b_list = ['Grammar Correction','POS Separation','Emotion Sensor']
        self.p_btn = []
        
        self.label = QLabel()
        
        self.area = QTextEdit()
        self.area.setStyleSheet(f"font-size:20px")
        
        self.answer = QTextEdit()
        self.answer.setReadOnly(True)
        self.answer.setStyleSheet(f"font-size:20px")
        
        
        self.r_action_btn = QPushButton("Submit")
        self.r_action_btn.setFixedWidth(120)
        self.r_action_btn.clicked.connect(self.action_of_btn)
        
        #methods
        self.initUI()
        
        self.addButtons()
        
        self.addRightSide()

    def initUI(self):
        # layout objects
        
        self.grid_left.setColumnStretch(0, 1)
        
        self.grid_right.setColumnStretch(0, 3)
        
        # adding layout
        self.h_layout.addLayout(self.grid_left)
        self.h_layout.addLayout(self.grid_right)
        
        # Set main layout for window
        self.setLayout(self.h_layout)

    def addButtons(self):
        
        for btn in self.b_list:
            
            n_btn = QPushButton(btn)
            n_btn.setFixedWidth(120)
            n_btn.clicked.connect(self.action_of_btn)
            
            self.p_btn.append(n_btn)
            
            self.grid_left.addWidget(n_btn)
            
    def action_of_btn(self):
        
        mode = self.sender().text() # type: ignore
        
        if mode == 'Submit':
            
            action = self.label.text()        
            text = self.area.toPlainText()
            if action =='Grammar Correction':
                answer = self.grammar.grammar_correction(text)
                print(answer)
                self.answer.setText(answer)

            elif action == 'POS Separation':
                self.label.setText(mode)
            
            else:
                answer = self.grammar.detect_emotion(text)
                print(answer)
                self.answer.setText(answer)
            
        elif mode =='Grammar Correction':
            self.label.setText(mode)        
    
        elif mode == 'POS Separation':
            self.label.setText(mode)
        else:
            self.label.setText('Emotion Sensor')     
            
            
        print(mode)

    def addRightSide(self):
        
        self.label.setText("")
        
        self.grid_right.addWidget(self.label)
        
        self.grid_right.addWidget(self.area)
        
        self.grid_right.addWidget(self.r_action_btn)
    
        self.grid_right.addWidget(self.answer)
        
        
class Grammar:
    
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('en-US')
        

    
    def detect_emotion(self,sentence):
        
        analyzer = SentimentIntensityAnalyzer()
        
        scores = analyzer.polarity_scores(sentence)
        
        if scores['compound'] >= 0.05:
            return 'happy'
        elif scores['compound'] <= -0.05:
            return 'sad'
        else:
            return 'neutral'
    
    def grammar_correction(self,text)->str:
        
        matches = self.tool.check(text)

        corrections = []
        mistakes = []
        errorStartPosition = []
        errorEndPosition = []

        for match in matches:
            if len(match.replacements) > 0:
                errorStartPosition.append(match.offset)
                errorEndPosition.append(match.offset + match.errorLength)
                mistakes.append(text[match.offset : match.offset + match.errorLength])
                corrections.append(match.replacements[0])

        newText = list(text)

        for i in range(len(errorStartPosition)):
            for j in range(len(text)):
                newText[errorStartPosition[i]] = corrections[i]
                if j > errorStartPosition[i] and j < errorEndPosition[i]:
                    newText[j] = ""

        newText = "".join(newText)

        return newText
    
if __name__ == '__main__':
    application = QApplication(sys.argv)
    # object of MainWindow class
    window = MainWindow()
    window.setWindowTitle("Grammar Correction")
    window.setGeometry(250, 150, 700, 400)
    window.show()
    sys.exit(application.exec())
