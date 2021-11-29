class Item:
    model_num = ""
    type = ""

    def __init__(self, model_num, type):
        self.model_num = model_num
        self.type = type

    def get_text(self):
        return self.type + " " + self.model_num

