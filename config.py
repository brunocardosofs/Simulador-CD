import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QIcon

import resources.resources

from styles.style import globalStyle

current_path = sys.argv[0].replace("main.py", "")

class Config(QtWidgets.QMainWindow):
    def __init__(self, parent: None):
        super().__init__()

        self.isDarkMode = parent.isDarkMode
        
        self.setWindowTitle("Configurações")
        self.setMinimumWidth(500)
        self.setMinimumHeight(300)
        self.setWindowIcon(QIcon(":/images/icons/icon.ico"))

        container = QtWidgets.QWidget()
        container.setObjectName("teste")

        self.text = QtWidgets.QLabel("Config", alignment=QtCore.Qt.AlignCenter)
        self.button = QtWidgets.QPushButton("Print")
        self.buttonClose = QtWidgets.QPushButton("Fechar")
        self.input = QtWidgets.QLineEdit()
        
        self.buttonClose.setStyleSheet("background: red;color:#fff;border-radius:5px;border:none;padding:5px")

        container.setStyleSheet(globalStyle(self))
        
        container.setObjectName("centralwidget")
        
        self.button.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonClose.setCursor(QtCore.Qt.PointingHandCursor)

        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(self.text)
        # layout.addWidget(self.input)
        # layout.addWidget(self.button)
        layout.addWidget(self.buttonClose)

        container.setLayout(layout)
        self.setCentralWidget(container)

        self.button.clicked.connect(self.magic)
        self.buttonClose.clicked.connect(self.close)

    def closeEvent(self, event):
        pass

    def magic(self):
        text = self.input.text()
        print(text)