import sys
import language_tool_python
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from nltk.corpus import wordnet 
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QMainWindow, QTextEdit, QVBoxLayout,
                             QLabel, QHBoxLayout, QMenuBar,QTableWidget,
    QTableWidgetItem,)
from PyQt6.QtGui import (QAction,QPixmap,QColor,QPen,QPainter,QFont,QImage)

from PyQt6.QtCore import Qt

class WorkingWindow(QWidget):

    def __init__(self,mode):
        super().__init__()
        
        
        self.setGeometry(250, 150, 700, 400)
        
        # attributes
        self.grammar = Grammar(mode)
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()

        self.p_btn = []

        self.menu_bar = QMenuBar()
        self.action_gc = QAction("Grammar Correction", self)
        self.action_pos = QAction("POS Separation", self)
        self.action_es = QAction("Emotion Sensor", self)
        self.action_wm = QAction("Word Meaning",self)

        self.menu_bar.addAction(self.action_gc)
        self.menu_bar.addAction(self.action_pos)
        self.menu_bar.addAction(self.action_es)
        self.menu_bar.addAction(self.action_wm)

        self.action_gc.triggered.connect(self.action_of_menu)
        self.action_pos.triggered.connect(self.action_of_menu)
        self.action_es.triggered.connect(self.action_of_menu)
        self.action_wm.triggered.connect(self.action_of_menu)

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
        # methods
        self.initUI()

    def initUI(self):
        ''' Seting the UI for project'''
        # layout objects
        self.v_layout.addWidget(self.menu_bar)

        # adding layout
        self.v_layout.addWidget(self.menu_bar)

        self.label.setText("Select From Menu")

        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.area)
        self.v_layout.addWidget(self.r_action_btn)
        self.v_layout.addWidget(self.answer)

        # Set main layout for window
        self.setLayout(self.v_layout)

    def btn_submit(self):
        '''Performing the Action Submit Button'''
        mode = self.sender().text()  # type: ignore
        if mode == 'Submit':

            action = self.label.text()
            text = self.area.toPlainText()
            if action == 'Grammar Correction':
                corrected_text =''
                # self.grammar.grammar_correction(text)
                self.answer.setText(corrected_text)
            elif action == 'POS Separation':
                answer = self.grammar.pos_separator(text)
                self.answer.setText(str(answer))
            elif action =='Emotion Sensor':
                answer = ''
                # self.grammar.detect_emotion(text)
                print(answer)
                self.answer.setText(answer)
            else:
                answer = self.grammar.word_meaning(text)
                answer = f"Meaning:{answer[0].definition()}\nSentence:{answer[1].examples()[0]}"
                self.answer.setText(answer)
        
    def action_of_menu(self):
        '''Performing the required action from menu'''
        mode = self.sender().text()  # type: ignore
        print(mode)

        if mode == 'Grammar Correction':
            self.label.setText(mode)
            self.area.setText("Incorrct grammer")

        elif mode == 'POS Separation':
            self.label.setText(mode)
        elif mode=='Emotion Sensor':   
            self.label.setText(mode)
            self.area.setText('I broke my laptop yesterday')
        else:
            self.label.setText(mode)
            self.area.setText('Testing')
            


class Grammar:

    def __init__(self,mode):
        self.set_tool(mode)

    def set_tool(self,mode):
        if mode =='English':
            self.tool = language_tool_python.LanguageTool('en-US')

    def word_meaning(self,word)->list:
        return wordnet.synsets(word)
    def pos_separator(self,data):
        
        tokens = nltk.word_tokenize(data)
        tagged = nltk.pos_tag(tokens)

        # Define a dictionary to map POS tags to their names
        pos_names = {
            'CC': 'Coordinating conjunction',
            'CD': 'Cardinal number',
            'DT': 'Determiner',
            'EX': 'Existential there',
            'FW': 'Foreign word',
            'IN': 'Preposition or subordinating conjunction',
            'JJ': 'Adjective',
            'JJR': 'Adjective, comparative',
            'JJS': 'Adjective, superlative',
            'LS': 'List item marker',
            'MD': 'Modal',
            'NN': 'Noun, singular or mass',
            'NNS': 'Noun, plural',
            'NNP': 'Proper noun, singular',
            'NNPS': 'Proper noun, plural',
            'PDT': 'Predeterminer',
            'POS': 'Possessive ending',
            'PRP': 'Personal pronoun',
            'PRP$': 'Possessive pronoun',
            'RB': 'Adverb',
            'RBR': 'Adverb, comparative',
            'RBS': 'Adverb, superlative',
            'RP': 'Particle',
            'SYM': 'Symbol',
            'TO': 'to',
            'UH': 'Interjection',
            'VB': 'Verb, base form',
            'VBD': 'Verb, past tense',
            'VBG': 'Verb, gerund or present participle',
            'VBN': 'Verb, past participle',
            'VBP': 'Verb, non-3rd person singular present',
            'VBZ': 'Verb, 3rd person singular present',
            'WDT': 'Wh-determiner',
            'WP': 'Wh-pronoun',
            'WP$': 'Possessive wh-pronoun',
            'WRB': 'Wh-adverb'
        }
        pos = {}
        for word, tag in tagged:
            
            pos[word] = pos_names.get(tag, tag)
        
        return pos # type:ignore
            
    def detect_emotion(self, sentence):

        analyzer = SentimentIntensityAnalyzer()

        scores = analyzer.polarity_scores(sentence)

        if scores['compound'] >= 0.05:
            return 'happy'
        elif scores['compound'] <= -0.05:
            return 'sad'
        else:
            return 'neutral'

    def grammar_correction(self, text) -> str:

        matches = self.tool.check(text)

        corrections = []
        mistakes = []
        errorStartPosition = []
        errorEndPosition = []

        for match in matches:

            if len(match.replacements) > 0:
                errorStartPosition.append(match.offset)
                errorEndPosition.append(match.offset + match.errorLength)
                mistakes.append(
                    text[match.offset: match.offset + match.errorLength])
                corrections.append(match.replacements[0])

        newText = list(text)

        for i in range(len(errorStartPosition)):
            for j in range(len(text)):
                newText[errorStartPosition[i]] = corrections[i]
                if j > errorStartPosition[i] and j < errorEndPosition[i]:
                    newText[j] = ""

        newText = "".join(newText)

        return newText




class MainWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()    
        
        # style_sheet = '''
        #     QWidget{
        #     background-color:#ffffff;
        #     background-image:url(./background.png);
        #     background-position: center;
        #     background-repeat: no-repeat;
        #     }
        # '''
        

        
        self.central_widget = QWidget()
        
        
        # self.central_widget.setStyleSheet(style_sheet)
        self.setCentralWidget(self.central_widget)
        
        self.e_button = QPushButton('English', self)
        self.e_button.setFixedWidth(100)
        self.e_button.setStyleSheet("background-color:#DEE2FF;color:black;font-weight:900;font-size:20px;border:1px solid;border-radius:20px;")
        self.e_button.setGeometry(300,325,100,50)
        
        # self.u_button = QPushButton('Urdu', self)
        # self.u_button.setFixedWidth(100)
        # self.u_button.setStyleSheet("background-color:#DEE2FF; color:black;font-weight:bold;")
        # self.u_button.setGeometry(200,325,100,50)
        
        self.e_button.clicked.connect(self.switch_window)
        # self.u_button.clicked.connect(self.switch_window)
        
        
        self.label = QLabel("English grammar checker by 101,110,125",parent=self.central_widget)
        
        self.label.move(60,10)
        style_sheet_label = '''
            font-size:30px;
            font-family:Time New Roman;
            '''
        self.label.setStyleSheet(style_sheet_label)
        
        pixmap = QPixmap('background.png')

        pix_label = QLabel("",parent=self.central_widget)
        pix_label.setPixmap(pixmap)
        pix_label.move(200,100)
        
        
        
        

        self.current_window = self
    
    def switch_window(self):
        self.current_window.close()
        mode = str(self.sender().text()) # type:ignore
        
        self.current_window = WorkingWindow(mode)    
        
        self.current_window.show()


if __name__ == '__main__':
    application = QApplication(sys.argv)
    # object of MainWindow class
    window = MainWindow()
    window.setWindowTitle("Grammar Correction")
    window.setGeometry(250, 150, 700, 400)
    window.show()
    sys.exit(application.exec())
