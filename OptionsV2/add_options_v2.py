import Answer
import Question_List
import Question
import Checkbox
import Dropdown
import Toggle
import Option

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import sip
import sys


def question_list_UI(question_list = None):
    if question_list == None:
        question_list = Question_List.Question_List()

    question_list_layout = QVBoxLayout()
    questions_layout = QVBoxLayout()

    for question in question_list.question_list:
        questions_layout.addLayout(inalize_question_UI(question_list, question))

    question_list_layout.addLayout(questions_layout)

    add_button_layout = QHBoxLayout()
    add_question_btn = QPushButton("Add Question")
    add_question_btn.setMaximumWidth(120)
    add_question_btn.clicked.connect(lambda : questions_layout.addLayout(add_question_UI(question_list)))

    space = QWidget()
    space.setMaximumWidth(600)
    space.setMinimumWidth(600)


    add_button_layout.addWidget(space)
    add_button_layout.addWidget(add_question_btn)
    add_button_layout.addWidget(QWidget())

    question_list_layout.addLayout(add_button_layout)
    question_list_layout.addWidget(QWidget())

    return question_list_layout


def update_questions_layout(questions_layout, question_list):
    delete_childern(questions_layout)

    for question in question_list.get_question_list():
        questions_layout.addLayout(inalize_question_UI(question_list, question))


def del_question_UI(question_layout, question_list, question):
    question_list.remove_question(question)
    update_questions_layout(question_layout.parent(), question_list)


def move_question_UI(question_layout, question_list, question, new_index):
    question_list.move_question(question,new_index)
    update_questions_layout(question_layout.parent(), question_list)


def inalize_question_UI(question_list, question):
    question_layout = QVBoxLayout()

    options = QHBoxLayout()
    remove_question_btn = QPushButton("X")
    remove_question_btn.setMaximumWidth(35)
    remove_question_btn.clicked.connect(lambda : del_question_UI(question_layout, question_list, question))

    move_up_btn = QPushButton("^")
    move_up_btn.setMaximumWidth(35)
    move_up_btn.clicked.connect(lambda: move_question_UI(question_layout, question_list, question, question.get_index() - 1))

    move_down_btn = QPushButton("v")
    move_down_btn.setMaximumWidth(35)
    move_down_btn.clicked.connect(lambda: move_question_UI(question_layout, question_list, question, question.get_index() + 1))

    space = QWidget()
    space.setMinimumWidth(600)
    space.setMaximumWidth(600)

    options.addWidget(move_up_btn)
    options.addWidget(move_down_btn)
    options.addWidget(space)
    options.addWidget(remove_question_btn)
    options.addWidget(QWidget())

    question_layout.addLayout(options)
    question_layout.addLayout(question_UI(question))

    return question_layout


def add_question_UI(question_list, question = None):
    if question == None:
        question = Question.Question("", Checkbox.Checkbox())

    question_list.add_question(question)

    return inalize_question_UI(question_list, question)


def question_UI(question = None):
    if question == None:
        question = Question.Question("", Checkbox.Checkbox())

    answer_layout = Answer_UI(question.get_answer())

    question_layout = QVBoxLayout()

    question_text = QLineEdit()
    question_text.setPlaceholderText('[Enter Question Text]')
    question_text.setText(question.get_question_text())
    question_text.setMaximumWidth(725)
    question_text.setMaximumHeight(50)
    question_text.textChanged.connect(question.set_question_text)

    dropdown = QComboBox()
    dropdown.setMaximumWidth(110)
    dropdown.addItem("Checkbox")
    dropdown.addItem("Dropdown")
    dropdown.addItem("Toggle")
    if question.Answer.get_Answer_Type() == 'Checkbox':
        dropdown.setCurrentIndex(0)
    elif question.Answer.get_Answer_Type() == 'Dropdown':
        dropdown.setCurrentIndex(1)
    elif question.Answer.get_Answer_Type() == 'Toggle':
        dropdown.setCurrentIndex(2)
    else:
        print('error invalid answer type')
    dropdown.currentIndexChanged.connect(lambda type: change_answer_type(type, question, answer_layout))

    question_layout.addWidget(question_text)
    question_layout.addWidget(dropdown)
    question_layout.addLayout(answer_layout)

    return question_layout


def change_answer_type(type, question, answer_layout):
    question.change_answer_type(type)
    delete_childern(answer_layout)

    answer_layout.addLayout(Answer_UI(question.get_answer()))


def Answer_UI(answer = None):

    if answer == None:
        answer = Answer.Answer()

    answer_layout = QVBoxLayout()
    option_list_layout = QVBoxLayout()

    if answer.get_option_list() == []:
        option_list_layout.addLayout(add_option_UI(answer))
    else:
        for option in answer.get_option_list():
            option_list_layout.addLayout(inalize_option_UI(answer, option))

    add_option_node = QHBoxLayout()
    add_option_btn = QPushButton("+")
    add_option_btn.setMaximumWidth(525)
    add_option_btn.setMinimumWidth(525)
    add_option_node.addWidget(add_option_btn)
    add_option_node.addWidget(QWidget())

    add_option_btn.clicked.connect(lambda: option_list_layout.addLayout(add_option_UI(answer)))

    answer_layout.addLayout(option_list_layout)
    answer_layout.addLayout(add_option_node)

    return answer_layout




def add_option_UI(answer, option = None):
    if option == None:
        option = Option.Option("")
    answer.add_option(option)

    return inalize_option_UI(answer, option)


def inalize_option_UI(answer, option):

    option_layout = QHBoxLayout()

    remove_Option_btn = QPushButton("X")
    remove_Option_btn.setMaximumWidth(35)
    remove_Option_btn.clicked.connect(lambda: del_option_UI(option_layout, answer, option))

    move_up_btn = QPushButton("^")
    move_up_btn.setMaximumWidth(35)
    move_up_btn.clicked.connect(lambda: move_option_UI(option_layout, answer, option, option.get_index()-1))

    move_down_btn = QPushButton("v")
    move_down_btn.setMaximumWidth(35)
    move_down_btn.clicked.connect(lambda: move_option_UI(option_layout, answer, option, option.get_index() + 1))

    space = QWidget()
    space.setMaximumWidth(100)
    space.setMinimumWidth(100)

    option_layout.addLayout(option_UI(option))
    option_layout.addWidget(space)
    option_layout.addWidget(move_up_btn)
    option_layout.addWidget(move_down_btn)
    option_layout.addWidget(remove_Option_btn)
    option_layout.addWidget(QWidget())

    return option_layout


def update_option_layout(option_list_layout, answer):
    delete_childern(option_list_layout)
    for options in answer.get_option_list():
        option_list_layout.addLayout(inalize_option_UI(answer, options))


def del_option_UI(option_layout, answer, option):
    answer.remove_option(option)

    update_option_layout(option_layout.parent(), answer)


def move_option_UI(option_layout, answer, option, new_index):
    answer.move_option(option, new_index)

    update_option_layout(option_layout.parent(), answer)


def option_UI(option):
    option_layout = QHBoxLayout()

    option_Text = QLineEdit()
    option_Text.setPlaceholderText('[Enter Option Text]')
    option_Text.setText(option.get_Option_text())
    option_Text.setMaximumWidth(300)
    option_Text.textChanged.connect(option.set_Option_text)


    option_layout.addWidget(option_Text)

    return option_layout








   # code from https://stackoverflow.com/questions/26212106/remove-everything-from-a-frame-in-pyqt
def deleteLayout(layout):
     if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                deleteLayout(item.layout())

        sip.delete(layout)

def delete_childern(layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                deleteLayout(item.layout())