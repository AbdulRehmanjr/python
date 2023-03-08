import sys
import time
import language_tool_python
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from nltk.corpus import wordnet 
from PyQt6.QtWidgets import (QApplication, QMainWindow,QWidget,
                             QSplashScreen
                              )
from PyQt6 import uic
from PyQt6.QtGui import QColor,QFont,QPixmap


class Grammar:
    
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('en-US')

    def word_meaning(self,word)->list:
        
        '''Returning the meaning and sentence from word'''
        
        return wordnet.synsets(word)
    
    def pos_separator(self,data):
        
        '''Separating the parts of speech'''
        
        tokens = nltk.word_tokenize(data)
        tagged = nltk.pos_tag(tokens)

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

'''
Widget class
'''
class WorkingWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('widget_UI.ui',self) # type:ignore

        # grammar 
        self.grammar = Grammar()
        # buttons
        self.g_correction.clicked.connect(self.button_action)# type:ignore
        self.emotion_sen.clicked.connect(self.button_action)# type:ignore
        self.w_meaning.clicked.connect(self.button_action)# type:ignore
        self.pos_sep.clicked.connect(self.button_action)# type:ignore
        self.submit.clicked.connect(self.button_submit)    # type:ignore
        
        # others
        self.current_mode = ''

    def button_submit(self):
        '''Action performing according to given signal'''
        
        text = self.input_area.toPlainText()# type:ignore
        
        if self.current_mode == 'Grammar Correction':
            answer = self.grammar.grammar_correction(text)
            self.answer_area.setPlainText(answer)# type:ignore

        elif self.current_mode == 'Pos Separation':
            answer= self.grammar.pos_separator(text)
            self.answer_area.setPlainText(str(answer))# type:ignore
            
        elif self.current_mode=='Emotion Sensor':   
            answer = self.grammar.detect_emotion(text)
            self.answer_area.setPlainText(answer)# type:ignore
            
        elif self.current_mode =='Meaning':
            answer = self.grammar.word_meaning(text)
            print(answer)
            if isinstance(answer,list):
                answer = f"Meaning:\n{answer[0].definition()}\nSentence:\n{answer[1].examples()[0]}"
            else:
                answer = f"Word is not valid"
            
            self.answer_area.setPlainText(answer)# type:ignore
        
        
    
    def button_action(self):
        
        '''Performing the required action from menu'''
        
        mode = self.sender().text() # type:ignore
        self.current_mode = mode
        print(mode)

        if mode == 'Grammar Correction':
            self.mode.setText(mode)# type:ignore
            self.input_area.setPlainText("Incorrct grammer")# type:ignore

        elif mode == 'Pos Separation':
            
            self.mode.setText(mode)# type:ignore
            self.input_area.setPlainText("I am a student")# type:ignore
        elif mode=='Emotion Sensor':   
            self.mode.setText(mode)# type:ignore
            self.input_area.setPlainText('I broke my laptop yesterday')# type:ignore
        elif mode =='Meaning':
            self.mode.setText(mode)# type:ignore
            self.input_area.setPlainText('Testing')# type:ignore
            
            
        

class grammarcorrection(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('form.ui',self)# type:ignore

        self.current_window = self

        self.startBtn.clicked.connect(self.start_action)# type:ignore

    def start_action(self):
        '''Change the window'''
        self.current_window.close()

        self.current_window = WorkingWindow()

        self.current_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = grammarcorrection()
    
    splash = QSplashScreen()
    splash.show()
 
    splash.setFixedSize(400, 200)
    splash.setGeometry(400,300,400,200)
    splash.setFont(QFont('Times',20,900,True))
    splash.setPixmap(QPixmap('./logo.png'))
    splash.showMessage("Grammar Correction\nGroup 10 \n101,110,125", 5, 
                    color=QColor("Blue"))
    
    time.sleep(2)
    
    app.processEvents()    
    
    widget.show()
    splash.finish(widget)
    
    sys.exit(app.exec())
