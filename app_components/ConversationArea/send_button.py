from PySide6 import QtWidgets, QtGui, QtCore
import sys

class SendButton(QtWidgets.QFrame):
    def __init__(self, MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.setWindowTitle("Send Button with Icon")

        layout = QtWidgets.QHBoxLayout(self)

        # Create the button
        self.send_button = QtWidgets.QPushButton()
        self.send_button.setFixedSize(40, 40)
        self.send_button.setObjectName("send_button")
        # Set the icon
        icon = QtGui.QIcon("./images/flight_icon.webp")
        self.send_button.setIcon(icon)
        self.send_button.setIconSize(self.send_button.size())
        self.send_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        
        self.shadow_effect = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow_effect.setBlurRadius(10)
        self.shadow_effect.setXOffset(1)
        self.shadow_effect.setYOffset(1)
        self.shadow_effect.setColor(QtGui.QColor(50, 50, 50, 150))  # Gray semi-transparent shadow

        self.send_button.setGraphicsEffect(self.shadow_effect)

        # Connect press/release events to change shadow
        self.send_button.pressed.connect(self.on_button_pressed)
        self.send_button.released.connect(self.on_button_released)

        
        self.send_button.clicked.connect(lambda: self.MainWindow.send_message(is_human = True))
        
        layout.addWidget(self.send_button)

        self.setLayout(layout)

    def on_button_pressed(self):
        """Reduce shadow effect when button is pressed (simulate depth effect)."""
        self.shadow_effect.setBlurRadius(10)
        self.shadow_effect.setXOffset(-1)
        self.shadow_effect.setYOffset(-1)
        self.shadow_effect.setColor(QtGui.QColor(50, 50, 50, 100))  # Lighter shadow

    def on_button_released(self):
        self.shadow_effect.setBlurRadius(10)
        self.shadow_effect.setXOffset(1)
        self.shadow_effect.setYOffset(1)
        self.shadow_effect.setColor(QtGui.QColor(50, 50, 50, 150))