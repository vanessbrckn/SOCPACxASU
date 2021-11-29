import Page
import list_func
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import sip

class Page_List(list_func.list_func):
    current_page_index = 0

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


    def remove_current_page(self):
        self.del_obj(self.list[self.current_page_index])

    def current_page(self):
        return self.list[self.current_page_index]


    def move_to_page(self, index):
        if index < 0 or index >= len(self.list):
            print("Fail to find page: index out of bounds")
        else:
            self.current_page_index = index



    def next_page_skip(self, index):
        if index < 0 or index >= len(self.list):
            print("Fail to find page: index out of bounds")
            return self.list[self.current_page_index]
        self.update_skiped_pages()
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
        self.update_skiped_pages()
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

        footer_layout = QHBoxLayout()

        prev_page_btn = QPushButton('previous page')
        prev_page_btn.clicked.connect(lambda : self.go_to_prev_page_UI(current_page))

        next_page_btn = QPushButton('next page')
        next_page_btn.clicked.connect(lambda : self.go_to_next_page_UI(current_page))

        footer_layout.addWidget(prev_page_btn)
        footer_layout.addWidget(next_page_btn)


        layout.addLayout(footer_layout)

        return layout

    def go_to_prev_page_UI(self, layout):
        self.delete_childern(layout)
        print (1)
        layout.addLayout(self.prev_page_skip(self.current_page_index).load_UI())


    def go_to_next_page_UI(self, layout):
        self.delete_childern(layout)
        print(2)
        layout.addLayout(self.next_page_skip(self.current_page_index).load_UI())


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

    def update_skiped_pages(self):
        for page in self.list:
            page.set_IsSkipped(bool(False))
        for i in self.get_skipped_pages().get_list():
            self.list[i].set_IsSkipped(bool(True))


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


