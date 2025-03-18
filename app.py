import sys
from PySide6.QtWidgets import QApplication
from app_components.main_window import MainWindow
import os

app = QApplication(sys.argv)

css_file = os.path.join(os.path.dirname(__file__), "app_components/style.css")  # Get absolute path
if os.path.exists(css_file):  # Check if file exists
    print("CSS is loaded Successfully")
    with open(css_file, "r") as f:
        app.setStyleSheet(f.read())  # Apply CSS
window = MainWindow(app)
window.show()
app.exec()
