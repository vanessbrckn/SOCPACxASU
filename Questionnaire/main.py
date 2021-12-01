import main_item_list
import run_Questionnaire
import Toggle, Answer, Checkbox,Dropdown
import Page_List
import Page

from PyQt5.QtWidgets import *
import sys

import Question_List
import Questionnaire_Editor
import run_Questionnaire_Editor

items = main_item_list.main_item_list()

def main():

    app = QApplication(sys.argv)

    #this initializes the page list with dummy quetions
    page_list = dummy_questionaire()

    # this shows a pop up window for the Questionnaire editor
    #run_Questionnaire_Editor.show(items, page_list)

    # this shows a pop up window for the questionnaire the user can take
    # run_Questionnaire also has the functions that will get a location from the item lists
    run_Questionnaire.show(page_list,(34.946222,69.264639))

    sys.exit(app.exec_())


def print_questions(printed_layout, question_list):
    Questionnaire_Editor.delete_childern(printed_layout)
    printed_layout.addLayout(question_list.load_UI())

def dummy_questionaire():
    question_list = dummy_questions()

    page_list = Page_List.Page_List()
    page = Page.Page(question_list)
    page_list.add_obj(page)
    page_list.add_obj(Page.Page(dummy_questions2()))
    page_list.add_obj(Page.Page(dummy_questions3()))

    return page_list


def dummy_questions():
    question_list = Question_List.Question_List()

    # quesion 1
    checkbox = Checkbox.Checkbox()
    checkbox.add_obj(Question_List.Question.Answer.Option.Option("option 1"))
    checkbox.add_obj(Question_List.Question.Answer.Option.Option("option 2"))
    checkbox.add_obj(Question_List.Question.Answer.Option.Option("option 3"))
    question = Question_List.Question.Question("Example checkmark", checkbox)
    question_list.add_obj(question)

    checkbox.obj_at(0).preferred_items.add_obj(items.list[1])
    checkbox.obj_at(0).preferred_items.add_obj(items.list[0])
    checkbox.obj_at(2).preferred_items.add_obj(items.list[2])


    # quesion 2
    dropdown = Dropdown.Dropdown()
    dropdown.add_obj(Question_List.Question.Answer.Option.Option("option 1"))
    dropdown.add_obj(Question_List.Question.Answer.Option.Option("option 2"))
    dropdown.add_obj(Question_List.Question.Answer.Option.Option("option 3"))
    question = Question_List.Question.Question("Example dropbox", dropdown)

    question_list.add_obj(question)
    # quesion 3

    toggle = Toggle.Toggle()
    toggle.add_obj(Question_List.Question.Answer.Option.Option("option 1"))
    toggle.add_obj(Question_List.Question.Answer.Option.Option("option 2"))
    toggle.add_obj(Question_List.Question.Answer.Option.Option("option 3"))
    question = Question_List.Question.Question("Example toggle", toggle)
    question_list.add_obj(question)

    return question_list

def dummy_questions2():
    question_list = Question_List.Question_List()

    # quesion 1
    checkbox = Checkbox.Checkbox()
    checkbox.add_obj(Question_List.Question.Answer.Option.Option("option 4"))
    checkbox.add_obj(Question_List.Question.Answer.Option.Option("option 5"))
    checkbox.add_obj(Question_List.Question.Answer.Option.Option("option 6"))
    question = Question_List.Question.Question("Example checkmark", checkbox)
    question_list.add_obj(question)

    checkbox.obj_at(0).preferred_items.add_obj(items.list[1])
    checkbox.obj_at(0).preferred_items.add_obj(items.list[0])
    checkbox.obj_at(2).preferred_items.add_obj(items.list[2])


    # quesion 2
    dropdown = Dropdown.Dropdown()
    dropdown.add_obj(Question_List.Question.Answer.Option.Option("option 4"))
    dropdown.add_obj(Question_List.Question.Answer.Option.Option("option 5"))
    dropdown.add_obj(Question_List.Question.Answer.Option.Option("option 6"))
    question = Question_List.Question.Question("Example dropbox", dropdown)

    question_list.add_obj(question)
    # quesion 3

    toggle = Toggle.Toggle()
    toggle.add_obj(Question_List.Question.Answer.Option.Option("option 4"))
    toggle.add_obj(Question_List.Question.Answer.Option.Option("option 5"))
    toggle.add_obj(Question_List.Question.Answer.Option.Option("option 6"))
    question = Question_List.Question.Question("Example toggle", toggle)
    question_list.add_obj(question)

    return question_list

def dummy_questions3():
    question_list = Question_List.Question_List()

    # quesion 1
    checkbox = Checkbox.Checkbox()
    checkbox.add_obj(Question_List.Question.Answer.Option.Option("option 7"))
    checkbox.add_obj(Question_List.Question.Answer.Option.Option("option 8"))
    checkbox.add_obj(Question_List.Question.Answer.Option.Option("option 9"))
    question = Question_List.Question.Question("Example checkmark", checkbox)
    question_list.add_obj(question)

    checkbox.obj_at(0).preferred_items.add_obj(items.list[1])
    checkbox.obj_at(0).preferred_items.add_obj(items.list[0])
    checkbox.obj_at(2).preferred_items.add_obj(items.list[2])


    # quesion 2
    dropdown = Dropdown.Dropdown()
    dropdown.add_obj(Question_List.Question.Answer.Option.Option("option 7"))
    dropdown.add_obj(Question_List.Question.Answer.Option.Option("option 8"))
    dropdown.add_obj(Question_List.Question.Answer.Option.Option("option 9"))
    question = Question_List.Question.Question("Example dropbox", dropdown)

    question_list.add_obj(question)
    # quesion 3

    toggle = Toggle.Toggle()
    toggle.add_obj(Question_List.Question.Answer.Option.Option("option 7"))
    toggle.add_obj(Question_List.Question.Answer.Option.Option("option 8"))
    toggle.add_obj(Question_List.Question.Answer.Option.Option("option 9"))
    question = Question_List.Question.Question("Example toggle", toggle)
    question_list.add_obj(question)

    return question_list

if __name__ == "__main__":
    main()
