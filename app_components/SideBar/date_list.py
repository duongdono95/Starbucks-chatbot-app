from PySide6 import QtCore, QtGui, QtWidgets

class DateList(QtWidgets.QFrame):
    def __init__(self, date_arr):
        super().__init__()
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        date_list_wrapper = QtWidgets.QScrollArea()
        date_list_wrapper.setWidgetResizable(True)
        
        self.date_list = QtWidgets.QWidget()
        self.date_list.setObjectName("date_list")
        self.date_list_layout = QtWidgets.QVBoxLayout(self.date_list)
        self.date_list_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        
        for date in date_arr:
            self.add_date_widget(date)
        
        date_list_wrapper.setWidget(self.date_list)
        layout.addWidget(date_list_wrapper)
        
        
    
    def add_date_widget(self, date_label):
        label = QtWidgets.QLabel(date_label)
        label.setObjectName("date_label")
        label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        label.setFixedHeight(30)
        self.date_list_layout.addWidget(label)