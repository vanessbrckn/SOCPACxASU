import Item
import Item_List
import list_func

class Option:
    Option_text = ""
    is_selected = bool(False)
    preferred_items = None
    remove_items = None
    skip_pages = None

    def __init__(self, new_Option_text = "", index = 0):
        self.remove_items = Item_List.Item_List()
        self.preferred_items = Item_List.Item_List()
        self.skip_pages = list_func.list_func()

        self.Option_text = new_Option_text
        self.index = index

    def select(self, state):
        self.is_selected = bool(state)
        return bool(True)

    def Is_Selected(self):
        return self.is_selected

    def get_Option_text(self):
        return self.Option_text

    def set_Option_text(self, option_text):
        self.Option_text = option_text


    def get_pre_items(self):
        return self.preferred_items

    def get_rem_items(self):
        return self.remove_items

    def get_skipped_pages(self):
        return self.skip_pages

