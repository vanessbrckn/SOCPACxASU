import Page
import list_func
import run_Questionnaire
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import sip

class Page_List(list_func.list_func):
    current_page_index = 0
    id_count = 0

    def __init__(self):
        self.list = []


    def del_obj(self, page):
        if len(self.list) == 1:
            self.add_obj(Page.Page())
            self.current_page_index = 0
        else:
            if self.current_page_index == self.find_indexof(page):
                if self.find_indexof(page) == len(self.list) - 1:
                    self.move_to_page(self.current_page_index -1)
        super().del_obj(page)

    def add_obj(self, page):
        page.set_id(self.id_count)
        self.id_count+= 1
        super().add_obj(page)

    def remove_current_page(self):
        self.del_obj(self.list[self.current_page_index])

    def current_page(self):
        return self.list[self.current_page_index]

    def get_index_from_id(self, id):
        for page in self.list:
            if page.get_id() == id:
                return self.find_indexof(page)
        return -1

    def move_to_page(self, index):
        if index < 0 or index >= len(self.list):
            print("Fail to find page: index out of bounds")
        else:
            self.current_page_index = index



    def next_page_skip(self, index):
        if index < 0 or index >= len(self.list):
            print("Fail to find page: index out of bounds")
            return self.list[self.current_page_index]
        self.update_skipped_pages()
        while index != len(self.list) - 1:
            index += 1
            if not self.list[index].IsSkipped():
                self.current_page_index = index
                return self.list[index]

        print("End of list")
        return self.list[self.current_page_index]

    def prev_page_skip(self, index):
        if index < 0 or index >= len(self.list):
            print("Fail to find page: index out of bounds")
            return self.list[self.current_page_index]
        self.update_skipped_pages()
        while index != 0:
            index -= 1
            if not self.list[index].IsSkipped():
                self.current_page_index = index
                return self.list[index]

        print("Beginning of list")
        return self.list[self.current_page_index]

    def load_UI(self):
        layout = QVBoxLayout()

        current_page = QVBoxLayout()
        current_page.addLayout(self.list[self.current_page_index].load_UI())

        layout.addLayout(current_page)

        layout.addWidget(QWidget())


        if self.current_page_index == 0:
            footer_layout = self.load_UI_first_page_footer(layout)
        elif self.current_page_index == self.len()-1:
            footer_layout = self.load_UI_last_page_footer(layout)
        else:
            footer_layout = QHBoxLayout()
            prev_page_btn = QPushButton('previous page')
            prev_page_btn.clicked.connect(lambda : self.go_to_prev_page_UI(layout))

            next_page_btn = QPushButton('next page')
            next_page_btn.clicked.connect(lambda : self.go_to_next_page_UI(layout))

            footer_layout.addWidget(prev_page_btn)
            footer_layout.addWidget(next_page_btn)


        layout.addLayout(footer_layout)

        return layout

    def load_UI_last_page_footer(self, layout):
        footer_layout = QHBoxLayout()

        prev_page_btn = QPushButton('previous page')
        prev_page_btn.clicked.connect(lambda : self.go_to_prev_page_UI(layout))

        submit_btn = QPushButton('Submit')
        submit_btn.clicked.connect(lambda: run_Questionnaire.popupwindow(run_Questionnaire.Final_location_UI(self), 300, 50))

        footer_layout.addWidget(prev_page_btn)
        footer_layout.addWidget(submit_btn)

        return footer_layout

    def load_UI_first_page_footer(self, layout):
        footer_layout = QHBoxLayout()

        next_page_btn = QPushButton('next page')
        next_page_btn.clicked.connect(lambda : self.go_to_next_page_UI(layout))

        footer_layout.addWidget(QWidget())
        footer_layout.addWidget(next_page_btn)

        return footer_layout

    def go_to_prev_page_UI(self, layout):
        self.delete_childern(layout)
        self.prev_page_skip(self.current_page_index)
        layout.addLayout(self.load_UI())


    def go_to_next_page_UI(self, layout):
        self.delete_childern(layout)
        self.next_page_skip(self.current_page_index)
        layout.addLayout(self.load_UI())


    def get_skipped_pages(self):
        skipped_pages = list_func.list_func()
        for page in self.list:
            skipped_pages.list = skipped_pages.list + page.get_skipped_pages().get_list()

        return skipped_pages




    def get_pre_items(self):
        pre_items = list_func.list_func()
        for item in self.list:
            pre_items.list = pre_items.list + item.get_pre_items().get_list()

        return pre_items

    def get_rem_items(self):
        rem_items = list_func.list_func()
        for item in self.list:
            rem_items.list = rem_items.list + item.get_rem_items().get_list()

        return rem_items

    def update_skipped_pages(self):
        for page in self.list:
            page.set_IsSkipped(bool(False))
        for id in self.get_skipped_pages().get_list():
            index = self.get_index_from_id(id)
            if index != -1:
                self.list[index].set_IsSkipped(bool(True))


   # code from https://stackoverflow.com/questions/26212106/remove-everything-from-a-frame-in-pyqt
    def deleteLayout(self, layout):
         if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())

            sip.delete(layout)

    def delete_childern(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())


