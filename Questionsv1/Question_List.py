import Question
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Question_List:
    question_list = []



    def __init__(self, question_list = []):
        self.question_list = question_list

    def add_question(self, question):
        self.question_list.append(question)

    def remove_question(self, index):
        self.question_list.remove(index)

    def quesiton_at(self, index):
        return self.question_list[index]

    def load_UI(self):
        layout = QVBoxLayout()
        for question in self.question_list:
            layout.addLayout(question.load_UI())
        layout.addWidget(QWidget())
        return layout