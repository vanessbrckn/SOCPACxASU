import Question_List

class Page:

    isSkipped = bool(False)
    question_list = None

    def __init__(self, question_list = None):
        if question_list is None:
            question_list = Question_List.Question_List()

        self.question_list = question_list

    def set_IsSkipped(self, bool):
        self.isSkipped = bool

    def IsSkipped(self):
        return self.isSkipped

    def load_UI(self):
        return self.question_list.load_UI()

    def get_skipped_pages(self):
        return self.question_list.get_skipped_pages()

    def get_pre_items(self):
        return self.question_list.get_pre_items()

    def get_rem_items(self):
        return self.question_list.get_rem_items()
