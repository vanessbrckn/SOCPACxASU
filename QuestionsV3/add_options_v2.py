import Answer
import Question_List
import Question
import Checkbox
import Dropdown
import Toggle
import Option
import Item_List
import main_item_list
import Page
import Page_List
from difflib import SequenceMatcher
import run_Questionnaire

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import sip
import sys

All_Items = main_item_list.main_item_list()

pop_up = []
page_list = Page_List.Page_List()

def run(items, Page_list):
    for page in Page_list.get_list():
        page_list.add_obj(page)
    All_Items.clear()
    for item in items.list:
        #print(item.get_text())
        All_Items.add_obj(item)

    layout = QVBoxLayout()

    show_btn = QPushButton('show')
    show_btn.clicked.connect(lambda : run_Questionnaire.show(page_list))

    page_list_UI = initalize_page_UI(page_list)

    layout.addLayout(page_list_UI)
    layout.addWidget(show_btn)


    return layout



def page_list_UI(page_list = None):
    if page_list is None:
        page_list = Page_List.Page_List()
        page_list.add_obj(Page.Page())

    initalize_page_UI(page_list)


def add_page_UI(page_list, page = None):
    if page is None:
        page = Page.Page()

    page_list.add_obj(page)

    return initalize_page_UI(page_list, page)


def initalize_page_UI(page_list):
    layout = QVBoxLayout()

    header = QHBoxLayout()

    current_page_layout = QVBoxLayout()


    page_index_label = QLabel("Page #: " + str(page_list.current_page_index))
    current_page_layout.addWidget(page_index_label)

    current_page_layout.addLayout(page_UI(page_list.obj_at(page_list.current_page_index)))

    move_left_btn = QPushButton('< move page order')
    move_left_btn.clicked.connect(lambda : move_page_UI(current_page_layout, page_list.current_page_index-1, page_list))

    move_right_btn = QPushButton('move page order >')
    move_right_btn.clicked.connect(lambda : move_page_UI(current_page_layout, page_list.current_page_index+1, page_list))

    add_page_button = QPushButton('add page')
    add_page_button.clicked.connect(lambda: insert_page_UI(current_page_layout, page_list))

    prev_page_btn = QPushButton('previous page')
    prev_page_btn.clicked.connect(lambda: prev_page_UI(current_page_layout, page_list))

    next_page_btn = QPushButton('next page')
    next_page_btn.clicked.connect(lambda: next_page_UI(current_page_layout, page_list))

    remove_page_btn = QPushButton('remove_page')
    remove_page_btn.clicked.connect(lambda: remove_page_UI(current_page_layout, page_list))

    header.addWidget(move_left_btn)
    header.addWidget(add_page_button)
    header.addWidget(prev_page_btn)
    header.addWidget(next_page_btn)
    header.addWidget(remove_page_btn)
    header.addWidget(move_right_btn)

    layout.addLayout(header)
    layout.addLayout(current_page_layout)

    return layout

def insert_page_UI(layout, page_list):
    page_list.insert_obj(page_list.current_page_index, Page.Page())
    update_page(layout, page_list)

def move_page_UI(layout, index, page_list):
    page_list.move_obj(index, page_list.current_page())
    page_list.move_to_page(index)
    update_page(layout, page_list)

def remove_page_UI(layout, page_list):
    page_list.remove_current_page()
    update_page(layout, page_list)

def next_page_UI(layout, page_list):
    page_list.move_to_page(page_list.current_page_index +1)
    update_page(layout, page_list)


def prev_page_UI(layout, page_list):
    page_list.move_to_page(page_list.current_page_index -1)
    update_page(layout, page_list)


def update_page(layout, page_list):
    delete_childern(layout)

    page_index_label = QLabel("Page #: " + str(page_list.current_page_index))
    layout.addWidget(page_index_label)

    layout.addLayout(page_UI(page_list.current_page()))


def page_UI(page = None):
    if page is None:
        page = Page.Page()
    return question_list_UI(page.question_list)

def question_list_UI(question_list = None):

    if question_list == None:
        question_list = Question_List.Question_List()

    question_list_layout = QVBoxLayout()
    questions_layout = QVBoxLayout()

    for question in question_list.get_list():
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

    for question in question_list.get_list():
        questions_layout.addLayout(inalize_question_UI(question_list, question))


def del_question_UI(question_layout, question_list, question):
    question_list.del_obj(question)
    update_questions_layout(question_layout.parent(), question_list)


def move_question_UI(question_layout, question_list, question, new_index):
    question_list.move_obj(new_index, question)
    update_questions_layout(question_layout.parent(), question_list)


def inalize_question_UI(question_list, question):
    question_layout = QVBoxLayout()

    options = QHBoxLayout()
    remove_question_btn = QPushButton("X")
    remove_question_btn.setMaximumWidth(35)
    remove_question_btn.clicked.connect(lambda : del_question_UI(question_layout, question_list, question))

    move_up_btn = QPushButton("^")
    move_up_btn.setMaximumWidth(35)
    move_up_btn.clicked.connect(lambda: move_question_UI(question_layout, question_list, question, question_list.find_indexof(question) - 1))

    move_down_btn = QPushButton("v")
    move_down_btn.setMaximumWidth(35)
    move_down_btn.clicked.connect(lambda: move_question_UI(question_layout, question_list, question, question_list.find_indexof(question) + 1))

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

    question_list.add_obj(question)

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

    if answer.get_list() == []:
        option_list_layout.addLayout(add_option_UI(answer))
    else:
        for option in answer.get_list():
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
    answer.add_obj(option)

    return inalize_option_UI(answer, option)


def inalize_option_UI(answer, option):

    option_layout = QHBoxLayout()

    remove_Option_btn = QPushButton("X")
    remove_Option_btn.setMaximumWidth(35)
    remove_Option_btn.clicked.connect(lambda: del_option_UI(option_layout, answer, option))

    move_up_btn = QPushButton("^")
    move_up_btn.setMaximumWidth(35)
    move_up_btn.clicked.connect(lambda: move_option_UI(option_layout, answer, option, answer.find_indexof(option)-1))

    move_down_btn = QPushButton("v")
    move_down_btn.setMaximumWidth(35)
    move_down_btn.clicked.connect(lambda: move_option_UI(option_layout, answer, option, answer.find_indexof(option) + 1))

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
    for options in answer.get_list():
        option_list_layout.addLayout(inalize_option_UI(answer, options))


def del_option_UI(option_layout, answer, option):
    answer.del_obj(option)

    update_option_layout(option_layout.parent(), answer)


def move_option_UI(option_layout, answer, option, new_index):
    answer.move_obj(new_index, option)

    update_option_layout(option_layout.parent(), answer)


def option_UI(option):
    option_layout = QHBoxLayout()

    option_Text = QLineEdit()
    option_Text.setPlaceholderText('[Enter Option Text]')
    option_Text.setText(option.get_Option_text())
    option_Text.setMaximumWidth(300)
    option_Text.textChanged.connect(option.set_Option_text)

    item_list_btn = QPushButton("edit items")
    item_list_btn.clicked.connect(lambda: popupwindow(edit_item_list_UI(option), 600, 300))

    skip_pages_btn = QPushButton("skip pages")
    skip_pages_btn.clicked.connect(lambda: popupwindow(edit_skip_list_UI(option), 300, 300))

    option_layout.addWidget(option_Text)
    option_layout.addWidget(skip_pages_btn)
    option_layout.addWidget(item_list_btn)

    return option_layout

def edit_item_list_UI(option):
    layout = QHBoxLayout()
    layout.addLayout(edit_rem_list_UI(option))
    layout.addLayout(edit_pre_list_UI(option))
    return layout

def edit_pre_list_UI(option):
    layout = QVBoxLayout()
    list_layout = item_list_UI()
    list = list_layout.itemAt(2).widget()
    layout.addLayout(list_layout)
    select_in_list(list, option.get_pre_items())

    add_pre_btn = QPushButton("prefer items")
    add_pre_btn.clicked.connect(lambda: edit_to_pre_list(list.selectedItems(), option))

    layout.addWidget(add_pre_btn)
    return layout


def edit_to_pre_list(selected_list, option):
    option.preferred_items.clear()
    for label in selected_list:
        option.preferred_items.add_obj(All_Items.find_obj(label.text()))


def edit_rem_list_UI(option):
    layout = QVBoxLayout()
    list_layout = item_list_UI()
    list = list_layout.itemAt(2).widget()
    layout.addLayout(list_layout)
    select_in_list(list, option.get_rem_items())

    add_rem_btn = QPushButton("remove items")
    add_rem_btn.clicked.connect(lambda: edit_to_rem_list(list.selectedItems(), option))

    layout.addWidget(add_rem_btn)
    return layout


def edit_to_rem_list(selected_list, option):
    option.remove_items.clear()
    for label in selected_list:
        option.remove_items.add_obj(All_Items.find_obj(label.text()))


def edit_skip_list_UI(option):
    layout = QVBoxLayout()
    list_layout = skip_page_UI()
    list = list_layout.itemAt(1).widget()
    layout.addLayout(list_layout)
    select_pages(list, option.get_skipped_pages())

    add_skip_btn = QPushButton("Skip Pages")
    add_skip_btn.clicked.connect(lambda: edit_to_skip_list(list.selectedItems(), option))

    layout.addWidget(add_skip_btn)
    return layout


def edit_to_skip_list(selected_list, option):
    option.skip_pages.clear()
    for label in selected_list:
        option.skip_pages.add_obj(int(label.text()))

def select_pages(select_these, skip_pages):
    for page in skip_pages.list:
        select_these.item(page).setSelected(bool(True))




def select_in_list(select_these, item_list):
   for item in item_list.list:
       select_these.item(All_Items.find_indexof(item)).setSelected(bool(True))

def item_list_UI():
    layout = QVBoxLayout()

    list = QListWidget()

    search_bar = QLineEdit()
    search_bar.setPlaceholderText('search..')
    search_bar.textChanged.connect(lambda text: search(text, list))
    layout.addWidget(search_bar)

    select_layout = QHBoxLayout()
    select_all = QPushButton()
    select_all.setText('select all')
    select_all.clicked.connect(lambda : list.selectAll())

    select_layout.addWidget(select_all)


    deselect_all = QPushButton()
    deselect_all.setText('deselect all')
    deselect_all.clicked.connect(lambda : list.clearSelection())

    select_layout.addWidget(deselect_all)

    layout.addLayout(select_layout)


    list.setSelectionMode(QAbstractItemView.MultiSelection)
    for item in All_Items.list:
        list.addItem(item.get_text())
    layout.addWidget(list)

    return layout

def skip_page_UI():
    layout = QVBoxLayout()

    list = QListWidget()

    select_layout = QHBoxLayout()
    select_all = QPushButton()
    select_all.setText('select all')
    select_all.clicked.connect(lambda: list.selectAll())

    select_layout.addWidget(select_all)

    deselect_all = QPushButton()
    deselect_all.setText('deselect all')
    deselect_all.clicked.connect(lambda: list.clearSelection())

    select_layout.addWidget(deselect_all)

    layout.addLayout(select_layout)
    layout.addWidget(list)

    list.setSelectionMode(QAbstractItemView.MultiSelection)
    for i in range(0, page_list.len()):
        list.addItem(str(i))

    return layout




def search(text, list):
    select = bool(False)
    for i in range(1, list.count()):
        for j in range(0, list.count()):
            if SequenceMatcher(None, text, list.item(i).text()).ratio() > SequenceMatcher(None, text, list.item(j).text()).ratio():
                if (list.item(i).isSelected()):
                    select = bool(True)

                item = list.takeItem(i)
                list.insertItem(j, item)
                list.item(j).setSelected(select)
                i+=1
                select = bool(False)
                break


def popupwindow(layout, width, hight):
    scroll = QScrollArea()

    w = QWidget()
    w.resize(750, 725)
    w.move(1743, 22)


    main = QVBoxLayout()

    main.addLayout(layout)

    w.setLayout(main)
    scroll.setWidget(w)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    scroll.resize(width, hight)
    scroll.setWidgetResizable(True)
    scroll.show()
    pop_up.append(scroll)






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