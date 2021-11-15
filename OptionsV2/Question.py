import Answer
import Checkbox
import Toggle
import Dropdown
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Question:
    Answer = None
    Question_text = ""
    index = 0

    def __init__(self, new_Question_text, Answer, index = 0):
        self.Question_text = new_Question_text
        self.Answer = Answer
        self.index = index

    def get_question_text(self):
        return self.Question_text

    def set_question_text(self, question_text):
        self.Question_text = question_text

    def get_answer(self):
        return self.Answer

    def change_answer_type(self, type):
        new_answer = None
        if type == 0:
            new_answer = Checkbox.Checkbox()
        elif type == 1:
            new_answer = Dropdown.Dropdown()
        elif type == 2:
            new_answer = Toggle.Toggle()
        else:
           print("type of answer is invalid")

        for option in self.Answer.get_option_list():
            new_answer.add_option(option)

        self.Answer = new_answer

    def get_index(self):
        return self.index

    def set_index(self, index):
        print(self.Question_text + " | index change: " + str(self.index) + " to " + str(index))
        self.index = index

    def load_UI(self):
        layout = QVBoxLayout()
        question_text_UI = QLabel()
        question_text_UI.setText(self.Question_text)
        layout.addWidget(question_text_UI)
        layout.addLayout(self.Answer.load_UI())

        return layout
