from PySide6 import QtWidgets
from .input_area import InputArea
from .output_area import OutputArea
from .intent_suggestions import IntentSuggestions
class ConversationArea(QtWidgets.QFrame):
    def __init__(self, MainWindow):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        
        self.intent_suggestions = IntentSuggestions(MainWindow)
        self.output_area = OutputArea(MainWindow)
        self.input_area = InputArea(MainWindow)
        
        layout.addWidget(self.intent_suggestions)
        layout.addWidget(self.output_area, stretch=True)
        layout.addWidget(self.input_area)
    