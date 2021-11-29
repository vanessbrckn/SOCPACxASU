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
        self.list = []

    def select_option_at(self, index):
        for option in self.return_selected():
            option.select(bool(False))

        super().select_option_at(index)

    def load_UI(self):
        layout = QVBoxLayout()
        self.togglegroup = QButtonGroup()
        id = 0
        for option in self.list:
            button = QRadioButton(option.get_Option_text())
            self.togglegroup.addButton(button,id)
            layout.addWidget(button)
            if option.Is_Selected():
                button.setChecked(True)
            id+=1


        self.togglegroup.idClicked.connect(lambda index: self.select_option_at(index))

        return layout