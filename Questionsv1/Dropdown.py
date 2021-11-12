import Answer
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Dropdown(Answer.Answer):

    def __init__(self, Option_List = []):
        self.add_option(Answer.Option.Option('[Default]'))
        self.select_option_at(0)
        self.Option_List = self.Option_List + Option_List
        self.Answer_Type = 'Dropdown'



    def select_option_at(self, index):
        for option in self.return_selected():
            option.select(bool(False))

        self.Option_List[index].select(bool(True))

        return bool(True)

    def load_UI(self):
        layout = QVBoxLayout()
        dropdown = QComboBox()
        dropdown.setMaximumWidth(100)
        for option in self.Option_List:
            dropdown.addItem(option.get_Option_text())

        dropdown.currentIndexChanged.connect(self.select_option_at)
        layout.addWidget(dropdown)
        return layout