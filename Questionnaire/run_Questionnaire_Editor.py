from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import sip
import Questionnaire_Editor
import main_item_list

pop_up = []


def show(items, page_list):

    popupwindow(Questionnaire_Editor.run(items, page_list), 800, 725)

def popupwindow(layout, width, hight):
    scroll = QScrollArea()

    w = QWidget()
    w.resize(width, hight)
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

