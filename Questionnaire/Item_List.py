import Item
import list_func

class Item_List(list_func.list_func):


    def __init__(self):
        self.list = []

    def find_obj(self, text):
        for obj in self.list:
            if obj.get_text() == text:
                return obj

        return None
