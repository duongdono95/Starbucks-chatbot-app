from PySide6 import QtWidgets, QtGui, QtCore
from .date_list import DateList
class MenuBar(QtWidgets.QFrame):
    def __init__(self, MainWindow):
        super().__init__()
        self.setObjectName("menu_bar")
        # self.setFixedWidth(200)
        layout = QtWidgets.QVBoxLayout(self)

        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(3, 3)
        shadow.setColor(QtGui.QColor(0, 0, 0, 20))
        self.setGraphicsEffect(shadow)

        self.date_arr = ["March 10, 2025", "March 12, 2025", "March 14, 2025", "March 10, 2025", "March 12, 2025", "March 14, 2025", "March 10, 2025", "March 12, 2025", "March 14, 2025", "March 10, 2025", "March 12, 2025", "March 14, 2025", "March 10, 2025", "March 12, 2025", "March 14, 2025"]
        
        # ====== Logo ====== #
        logo_container = QtWidgets.QWidget()
        logo_layout = QtWidgets.QHBoxLayout(logo_container)
        logo_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        
        logo = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap("./images/logo.webp")
        logo.setMaximumSize(80, 80)
        logo.setPixmap(pixmap)
        logo.setScaledContents(True)
        logo.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        logo_layout.addWidget(logo)
        
        # ====== Date List Header ====== #
        date_list_header_container = QtWidgets.QWidget()
        date_list_header_container.setObjectName("date_list_header_container")
        date_list_header_container.setFixedHeight(50)
        date_list_container_layout = QtWidgets.QHBoxLayout(date_list_header_container)
        
        date_list_title = QtWidgets.QLabel("Your Conversation")
        date_list_title.setObjectName("date_list_title")
        
        clear_all_button = QtWidgets.QPushButton("Clear All")
        clear_all_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))  # Change cursor on hover
        clear_all_button.setObjectName("text-btn")
        
        
        date_list_container_layout.addWidget(date_list_title)
        date_list_container_layout.addWidget(clear_all_button)
        
        # ====== Date List ====== #
        date_list = DateList(self.date_arr)
        
        layout.addWidget(logo_container)
        layout.addWidget(date_list_header_container)
        layout.addWidget(date_list, stretch=True)
        
