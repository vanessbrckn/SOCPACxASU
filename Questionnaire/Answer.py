import Option
import list_func
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Answer(list_func.list_func):
    Answer_Type = ""

    def __init__(self):
        self.list = []


    def select_option_at(self, index):
        self.list[index].select(bool(True))

    def get_Answer_Type(self):
        return self.Answer_Type

    def return_selected(self):
        selected_options = []
        for option in self.list:
            if option.Is_Selected():
               selected_options.append(option)

        return selected_options


    def load_UI(self):
        layout = QVBoxLayout()
        return layout

