import Question
import list_func

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Question_List(list_func.list_func):

    def __init__(self):
        self.list = []


    def load_UI(self):
        layout = QVBoxLayout()
        for question in self.list:
            layout.addLayout(question.load_UI())
        layout.addWidget(QWidget())
        return layout



    def get_rem_items(self):
        rem_items = list_func.list_func()
        for question in self.list:
            rem_items.list = rem_items.list + question.get_rem_items().get_list()

        return rem_items

    def get_pre_items(self):
        pre_items = list_func.list_func()
        for question in self.list:
            pre_items.list = pre_items.list + question.get_pre_items().get_list()

        return pre_items

    def get_skipped_pages(self):
        skipped_pages = list_func.list_func()
        for question in self.list:
            skipped_pages.list = skipped_pages.list + question.get_skipped_pages().get_list()

        return skipped_pages