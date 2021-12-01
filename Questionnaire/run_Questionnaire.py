from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import sip

import main_item_list
import baseQuery
import geopy.distance

pop_up = []
location_list = []


def show(page_list, destination_Coords):
    layout = page_list.load_UI()
    initialize_location_list(destination_Coords)
    popupwindow(layout, 750, 725)


def initialize_location_list(destination_Coords):
    for coord in baseQuery.CoordinatesQuery():
        if coord[0] != destination_Coords[0] or coord[1] != destination_Coords[1]:
            location_list.append(coord)
    order_nearest_locations(destination_Coords)

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

    list = page_list.get_rem_items()
    for item in list.get_list():
        items.del_obj(items.find_obj(item.get_text()))

    for coords in location_list:
        planes = baseQuery.planeQuery(baseQuery.locationQuery(coords[0], coords[1])[0])
        for plane in planes:
            for item in items.get_list():
                if plane[0] == item.model_num and plane[1] == item.type:
                    return coords

    return -1


def order_nearest_locations(destination):
    location_list.sort(key=lambda num: geopy.distance.distance(num, destination).km)


def calc_distance(location1, location2):
    pass


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
