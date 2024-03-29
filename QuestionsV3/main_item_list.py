import Item_List
import Item
import baseQuery

class main_item_list(Item_List.Item_List):

    def __init__(self):
        self.list = []
        self.initialize_list()

    def initialize_list(self):
        loc = baseQuery.locationQuery(34.946222, 69.264639)

        for i in range(0, 10):
            planes = baseQuery.planeQuery(i)

            for plane in planes:
                self.add_obj(Item.Item(plane[0], plane[1]))