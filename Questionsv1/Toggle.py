import Answer
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Toggle(Answer.Answer):

    def __init__(self, Option_List = []):
        self.Option_List = Option_List
        self.Answer_Type = 'Toggle'

    def select_option_at(self, index):
        for option in self.return_selected():
            option.select(bool(False))

        self.Option_List[index].select(bool(True))

        return bool(True)

    def load_UI(self):
        layout = QVBoxLayout()
        toggle = QButtonGroup()
        for option in self.Option_List:
            button = QRadioButton(option.get_Option_text())
            toggle.addButton(button)
            layout.addWidget(button)

        toggle.idClicked.connect(self.select_option_at)

        return layout