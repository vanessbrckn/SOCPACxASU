import Question
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Question_List:
    question_list = []

    def __init__(self, question_list = None):
        if question_list is None:
            question_list = []
        self.question_list = question_list

    def get_question_list(self):
        return self.question_list

    def add_question(self, question):
        question.set_index(len(self.question_list))
        self.question_list.append(question)

    def remove_question(self, question):
        if question.get_index() == len(self.question_list)-1:
            pass
        else:
            index = question.get_index()
            while index+1 < len(self.question_list):
                self.question_list[index+1].set_index(index)
                index+=1

        self.question_list.remove(question)


    def question_at(self, index):
        return self.question_list[index]

    def move_question(self, question, new_index):
        if new_index < 0 or new_index >= len(self.question_list):
            print("Fail to move question: index out of bounds")
        else:
            self.remove_question(question)
            self.insert_question(question, new_index)

    def insert_question(self, question, index):
        if index < 0 or index <= len(self.question_list):
            print("Fail to insert question: index out of bounds")

        self.question_list.insert(index, question)

        while index < len(self.question_list):
            self.question_list[index].set_index(index)
            index += 1







    def load_UI(self):
        layout = QVBoxLayout()
        for question in self.question_list:
            layout.addLayout(question.load_UI())
        layout.addWidget(QWidget())
        return layout