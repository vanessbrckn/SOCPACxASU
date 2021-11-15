class Option:
    Option_text = ""
    is_selected = bool(False)
    index = 0

    def __init__(self, new_Option_text = "", index = 0):
        self.Option_text = new_Option_text
        self.index = index

    def select(self, state):
        self.is_selected = bool(state)
        print(self.Option_text + "changed" + str(bool(state)))
        return bool(True)

    def Is_Selected(self):
        return self.is_selected

    def get_Option_text(self):
        return self.Option_text

    def set_Option_text(self, option_text):
        print(self.Option_text + " | text change: " + self.Option_text + " to " + option_text)
        self.Option_text = option_text

    def get_index(self):
        return self.index

    def set_index(self, index):
        print(self.Option_text + " | index change: " + str(self.index) + " to " + str(index))
        self.index = index


