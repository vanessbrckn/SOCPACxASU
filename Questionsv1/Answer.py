import Option
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Answer:
    Option_List = []
    Answer_Type = ""

    def __init__(self, Option_List = []):
        self.Option_List = Option_List

    def add_option(self, Option):
        self.Option_List.append(Option)
        return bool(True)

    def remove_option(self, index):
        self.Option_List.remove(index)
        return bool(True)

    def get_option_at(self, index):
        return self.Option_List[index]

    def get_option_list(self):
        return self.Option_List

    def select_option_at(self, index):
        self.Option_List[index].select()
        return bool(True)

    def get_Answer_Type(self):
        return self.Answer_Type

    def return_selected(self):
        selected_options = []
        for option in self.Option_List:
            if option.Is_Selected():
               selected_options.append(option)

        return selected_options

    def load_UI(self):
        layout = QVBoxLayout()
        return layout