import Answer
from PyQt5.QtWidgets import *


class Dropdown(Answer.Answer):

    def __init__(self):
        self.list = []
        self.Answer_Type = 'Dropdown'

    def add_obj(self, Option):
        super().add_obj(Option)
        if len(self.list) == 1:
            self.select_option_at(0)


    def select_option_at(self, index):
        for option in self.return_selected():
            option.select(bool(False))

        super().select_option_at(index)



    def load_UI(self):
        index = 0
        layout = QVBoxLayout()
        dropdown = QComboBox()
        for option in self.list:
            dropdown.addItem(option.get_Option_text())
            if option.Is_Selected():
                dropdown.setCurrentIndex(index)
            index += 1

        dropdown.currentIndexChanged.connect(self.select_option_at)
        layout.addWidget(dropdown)
        return layout