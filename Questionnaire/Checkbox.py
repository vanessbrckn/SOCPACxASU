import Answer
from PyQt5.QtWidgets import *


class Checkbox(Answer.Answer):

    def __init__(self):
        self.Answer_Type = 'Checkbox'
        self.list = []

    def load_UI(self):
        layout = QVBoxLayout()
        for option in self.list:
            checkbox = QCheckBox()
            checkbox.setText(option.get_Option_text())
            checkbox.setGeometry(200, 150, 100, 30)
            if option.Is_Selected():
                checkbox.setChecked(True)
            checkbox.stateChanged.connect(option.select)
            layout.addWidget(checkbox)
        return layout
