import sys
import language_tool_python
from nltk.sentiment.vader import SentimentIntensityAnalyzer


from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QGridLayout, QTextEdit,QVBoxLayout,
                             QLabel,QHBoxLayout,QMenuBar)
from PyQt6.QtGui import (QAction)

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        
        # attributes
        
        self.grammar = Grammar()
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        
        self.p_btn = []
        
        self.menu_bar = QMenuBar()
        self.action_gc = QAction("Grammar Correction",self)
        self.action_pos = QAction("POS Separation",self)
        self.action_es = QAction("Emotion Sensor",self)
        
        self.menu_bar.addAction(self.action_gc)
        self.menu_bar.addAction(self.action_pos)
        self.menu_bar.addAction(self.action_es)
        
        self.action_gc.triggered.connect(self.action_of_menu)
        self.action_pos.triggered.connect(self.action_of_menu)
        self.action_es.triggered.connect(self.action_of_menu)
        
        
        
        self.label = QLabel()
        
        self.area = QTextEdit()
        self.area.setStyleSheet(f"font-size:20px")
        self.area.wordWrapMode()
        
        self.answer = QTextEdit()
        self.answer.setReadOnly(True)
        self.answer.setStyleSheet(f"font-size:20px")
        
        
        self.r_action_btn = QPushButton("Submit")
        self.r_action_btn.setFixedWidth(120)
        self.r_action_btn.clicked.connect(self.btn_submit)
        #methods
        self.initUI()
        

    def initUI(self):
        ''' Seting the UI for project'''
        # layout objects
        self.v_layout.addWidget(self.menu_bar)
        
        
        # adding layout
        self.v_layout.addWidget(self.menu_bar)
        
        self.label.setText("")
        
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.area)
        self.v_layout.addWidget(self.r_action_btn)
        self.v_layout.addWidget(self.answer)
        
        # Set main layout for window
        self.setLayout(self.v_layout)

    
    def btn_submit(self):
        '''Performing the Action Submit Button'''
        mode = self.sender().text() # type: ignore
        print(mode)
        if mode == 'Submit':
            
            action = self.label.text()        
            text = self.area.toPlainText()
            if action =='Grammar Correction':
                corrected_text = self.grammar.grammar_correction(text)
                self.answer.setText(corrected_text)
                # pass
            elif action == 'POS Separation':
                self.label.setText(mode)

            else:
                answer = self.grammar.detect_emotion(text)
                print(answer)
                self.answer.setText(answer)
                # pass
        
    
    def action_of_menu(self):
        
        '''Performing the required action from menu'''
        mode = self.sender().text() # type: ignore
        print(mode)
                    
        if mode =='Grammar Correction':
            self.label.setText(mode)        
    
        elif mode == 'POS Separation':
            self.label.setText(mode)
        else:
            self.label.setText('Emotion Sensor')     
                        

        
        
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
