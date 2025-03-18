from PySide6 import QtCore, QtGui, QtWidgets
import os
from .send_button import SendButton
class InputArea(QtWidgets.QFrame):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.setObjectName("InputArea")
        self.layout = QtWidgets.QHBoxLayout(self)
        
        self.user_input = QtWidgets.QTextEdit()
        self.user_input.setObjectName("user-input")
        self.user_input.setPlaceholderText("Type a message...")
        self.user_input.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        
        self.user_input.textChanged.connect(self.update_message)
        
        self.send_button = SendButton(MainWindow)
    
        self.layout.addWidget(self.user_input) 
        self.layout.addWidget(self.send_button)       
        
    def update_message(self):
        self.MainWindow.current_message = self.user_input.toPlainText().strip()
 
            
    def resizeEvent(self, event):
        window_height = self.MainWindow.height()
        self.setFixedHeight(int(window_height) * 0.2)
        return super().resizeEvent(event)