import Option
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Answer:
    Option_List = []
    Answer_Type = ""

    def __init__(self):
        self.Option_List = []


    def add_option(self, Option):
        Option.set_index(len(self.Option_List))
        self.Option_List.append(Option)
        return bool(True)

    def remove_option_at(self, index):
        del self.Option_List[index]

        if index == len(self.Option_List) - 1:
            print("moved: None")
            pass
        else:
            while index < len(self.Option_List):
                print("moved: " + self.Option_List[index].get_Option_text())
                self.Option_List[index].set_index(index)
                index += 1

        return bool(True)

    def remove_option(self, option):
        print(option.get_Option_text() + " removed.")
        if option.get_index() == len(self.Option_List)-1:
            pass
        else:

            index = option.get_index()
            while index+1 < len(self.Option_List):
                self.Option_List[index+1].set_index(index)
                index+=1

        self.Option_List.remove(option)

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


    def move_option(self, option, new_index):
        if new_index < 0 or new_index >= len(self.Option_List):
            print(option.get_Option_text() + "can't move out of bounds")
        else:
            self.remove_option(option)
            self.insert_option(option, new_index)

    def insert_option(self, option, index):
        if index < 0 or index <= len(self.Option_List):
            print("Fail to insert option: index out of bounds")

        self.Option_List.insert(index, option)

        while index < len(self.Option_List):
            self.Option_List[index].set_index(index)
            index += 1


    def load_UI(self):
        layout = QVBoxLayout()
        return layout