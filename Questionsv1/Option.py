class Option:
    Option_text = ""
    is_selected = bool(False)

    def __init__(self, new_Option_text):
        self.Option_text = new_Option_text

    def select(self, state):
        self.is_selected = bool(state)
        print(self.Option_text + "changed" + str(state))
        return bool(True)

    def Is_Selected(self):
        return self.is_selected

    def get_Option_text(self):
        return self.Option_text

    def set_Option_text(self, option_text):
        self.Option_text = option_text


