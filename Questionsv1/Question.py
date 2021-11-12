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

    def __init__(self, new_Question_text, Answer):
        self.Question_text = new_Question_text
        self.Answer = Answer

    def get_question_text(self):
        return self.Question_text

    def set_question_text(self, question_text):
        self.Question_text = question_text

    def get_answer(self):
        return self.Answer

    def load_UI(self):

        layout = QVBoxLayout()
        question_text_UI = QLabel()
        question_text_UI.setMaximumHeight(25)
        question_text_UI.setText(self.Question_text)
        layout.addWidget(question_text_UI)
        layout.addLayout(self.Answer.load_UI())

        return layout
