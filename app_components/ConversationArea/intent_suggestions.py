from PySide6 import QtWidgets, QtCore, QtGui
import json

class IntentSuggestions(QtWidgets.QFrame):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.layout = QtWidgets.QGridLayout(self) 
        self.layout.setSpacing(10)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.display_suggestions()
            
    def display_suggestions(self):
        with open("./datasets/suggest_intents.json", "r") as f:
            self.intents = json.load(f)

        row, col = 0, 0
        max_cols = 6

        for index, intent in enumerate(self.intents):
            self.create_suggestion_widget(intent, row, col)
            col += 1
            if col >= max_cols: 
                col = 0
                row += 1

    def create_suggestion_widget(self, intent, row, col):
        button = QtWidgets.QPushButton(intent["text"])
        
        button.setObjectName("suggestion_intent")
        button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        
        
        button.clicked.connect(lambda: self.MainWindow.send_message(is_human = True, message = intent["text"]))

        self.layout.addWidget(button, row, col)  
