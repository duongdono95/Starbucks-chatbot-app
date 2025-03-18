from PySide6 import QtCore, QtGui, QtWidgets
import json
class OutputArea(QtWidgets.QFrame):
    def __init__(self, MainWindow):
        super().__init__()
        self.setObjectName("OutputArea")
        self.MainWindow = MainWindow

        self.layout = QtWidgets.QVBoxLayout(self)
        
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        
        self.messages_container = QtWidgets.QWidget(self.scroll_area)
        

        self.messages_layout = QtWidgets.QVBoxLayout(self.messages_container)
        self.messages_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.scroll_area.setWidget(self.messages_container)
        
        self.displayed_message_count = 0
 
        self.layout.addWidget(self.scroll_area)
        
        self.update_messages()
        
    def update_messages(self):
        messages = self.MainWindow.conversation["messages"]

        if self.displayed_message_count < len(messages):
            for i in range(self.displayed_message_count, len(messages)):
                self.display_message(messages[i])

            self.displayed_message_count = len(messages)
            
    def display_message(self, message):
        message_container = QtWidgets.QWidget()
        message_layout = QtWidgets.QHBoxLayout(message_container)
        
        text = QtWidgets.QLabel(message["content"])
        text.setWordWrap(True)
        text.setMaximumWidth(int(self.width()) * 0.9)
        text.setSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        text.adjustSize()

        
        message_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft if message["role"] == "bot" else QtCore.Qt.AlignmentFlag.AlignRight )
        text.setObjectName("message_wrapper_bot" if message["role"] == "bot" else "message_wrapper_human")

        message_layout.addWidget(text)
        
        self.messages_layout.addWidget(message_container)
        QtCore.QTimer.singleShot(100, lambda: self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum()))
        self.displayed_message_count += 1

        

            
            