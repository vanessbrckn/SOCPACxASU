import Question_List

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import sip
import sys



def main():

    question_list = dummy_questions()

    # dummy_questions() returns a question list that can be truned into a layout
    # using question_list.load_UI()

    # every thing else in main is more or less arbitrary
    # to show the layout on screen and can be changed

    app = QApplication(sys.argv)

    scroll = QScrollArea()

    w = QWidget()
    w.resize(750, 725)
    w.move(1743, 22)
    w.setWindowTitle('Simple')

    w.setLayout(question_list.load_UI())

    scroll.setWidget(w)
    scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    scroll.resize(750, 725)
    scroll.setWidgetResizable(True)
    scroll.show()


    sys.exit(app.exec_())

def dummy_questions():
    question_list = Question_List.Question_List()

    # quesion 1
    checkbox = Question_List.Question.Checkbox.Checkbox()
    checkbox.add_option(Question_List.Question.Answer.Option.Option("option 1"))
    checkbox.add_option(Question_List.Question.Answer.Option.Option("option 2"))
    checkbox.add_option(Question_List.Question.Answer.Option.Option("option 3"))
    question = Question_List.Question.Question("Example checkmark", checkbox)
    question_list.add_question(question)

    # quesion 2
    dropdown = Question_List.Question.Dropdown.Dropdown()
    dropdown.add_option(Question_List.Question.Answer.Option.Option("option 1"))
    dropdown.add_option(Question_List.Question.Answer.Option.Option("option 2"))
    dropdown.add_option(Question_List.Question.Answer.Option.Option("option 3"))
    question = Question_List.Question.Question("Example dropbox", dropdown)

    question_list.add_question(question)
    # quesion 3

    toggle = Question_List.Question.Toggle.Toggle()
    toggle.add_option(Question_List.Question.Answer.Option.Option("option 1"))
    toggle.add_option(Question_List.Question.Answer.Option.Option("option 2"))
    toggle.add_option(Question_List.Question.Answer.Option.Option("option 3"))
    question = Question_List.Question.Question("Example toggle", toggle)
    question_list.add_question(question)

    return question_list




if __name__ == "__main__":
    main()
