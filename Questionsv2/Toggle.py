import Answer
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Toggle(Answer.Answer):
    togglegroup = None

    def __init__(self):
        self.Answer_Type = 'Toggle'
        self.Option_List = []

    def select_option_at(self, index):
        for option in self.return_selected():
            option.select(bool(False))

        self.Option_List[index].select(bool(True))

        return bool(True)

    def load_UI(self):
        layout = QVBoxLayout()
        self.togglegroup = QButtonGroup()
        id = 0
        for option in self.Option_List:
            button = QRadioButton(option.get_Option_text())
            self.togglegroup.addButton(button,id)
            layout.addWidget(button)
            id+=1


        self.togglegroup.idClicked.connect(lambda index: self.select_option_at(index))

        return layout