from PySide6 import QtWidgets
from .input_area import InputArea
from .output_area import OutputArea
class ConversationArea(QtWidgets.QFrame):
    def __init__(self, MainWindow):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        
        
        self.output_area = OutputArea(MainWindow)
        self.input_area = InputArea(MainWindow)
        
        layout.addWidget(self.output_area, stretch=True)
        layout.addWidget(self.input_area)
    