import Checkbox, Toggle, Dropdown, Answer
import list_func

from PyQt5.QtWidgets import *


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

        for option in self.Answer.get_list():
            new_answer.add_obj(option)

        self.Answer = new_answer


    def load_UI(self):
        layout = QVBoxLayout()
        question_text_UI = QLabel()
        question_text_UI.setText(self.Question_text)
        layout.addWidget(question_text_UI)
        layout.addLayout(self.Answer.load_UI())

        return layout


    def get_rem_items(self):
        rem_items = list_func.list_func()
        for option in self.Answer.return_selected():
            rem_items.list = rem_items.list + option.get_rem_items().get_list()

        return rem_items

    def get_pre_items(self):
        pre_items = list_func.list_func()
        for option in self.Answer.return_selected():
            pre_items.list = pre_items.list + option.get_pre_items().get_list()

        return pre_items

    def get_skipped_pages(self):
        skipped_pages = list_func.list_func()
        for option in self.Answer.return_selected():
            skipped_pages.list = skipped_pages.list + option.get_skipped_pages().get_list()

        return skipped_pages