import Answer
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Checkbox(Answer.Answer):

    def __init__(self, Option_List = []):
        self.Option_List = Option_List
        self.Answer_Type = 'Checkbox'


    def load_UI(self):
        layout = QVBoxLayout()
        for option in self.Option_List:
            checkbox = QCheckBox()
            checkbox.setText(option.get_Option_text())
            checkbox.setGeometry(200, 150, 100, 30)
            if option.Is_Selected():
                checkbox.setChecked(True)
            checkbox.stateChanged.connect(option.select)
            layout.addWidget(checkbox)
        return layout
