from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import sip

import main_item_list
import baseQuery


pop_up = []


def show(page_list):
    layout = QVBoxLayout()

    submit_btn = QPushButton("Submit")
    submit_btn.clicked.connect(lambda :popupwindow(Final_location_UI(page_list), 750, 725))
    layout.addWidget(submit_btn)
    layout.addLayout(page_list.load_UI())

    popupwindow(layout, 750, 725)



    # this is more of a placeholder UI for how the location got from Final_location will display
    # aka its just shows the location index
def Final_location_UI(page_list):
    index = Final_location(page_list)
    layout = QVBoxLayout()
    label = QLabel(str(index))
    layout.addWidget(label)
    return layout

    # this gets the item list from the finished questionnaire and finds a location
    # this isn't finished
def Final_location(page_list):
    items = main_item_list.main_item_list()
    for item in items.get_list():
        print(item.get_text())

    list = page_list.get_rem_items()
    for item in list.get_list():
        print(item.get_text())
        items.del_obj(items.find_obj(item.get_text()))

    for i in range(0, 10):
        planes = baseQuery.planeQuery(i)
        for plane in planes:
            for item in items.get_list():
                if plane[0] == item.model_num and plane[1] == item.type:
                    return i
    return -1


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
