class list_func:

    list = None

    def __init__(self):
        self.list = []

    def clear(self):
        while self.list != []:
            self.del_obj(self.list[0])

    def get_list(self):
        return self.list

    def add_obj(self, object):
        self.list.append(object)

    def del_obj(self, object):
        self.list.remove(object)

    def insert_obj(self, index, object):
        if index < 0 or index > len(self.list):
            print("can't insert object: index out of bounds")
        else:
            self.list.insert(index, object)

    def move_obj(self, index, object):
        if index < 0 or index >= len(self.list):
            print("can't move object: index out of bounds")
        else:
            self.del_obj(object)
            self.insert_obj(index, object)

    def find_indexof(self, object):
        return self.list.index(object)

    def len(self):
        return len(self.list)

    def obj_at(self, index):
        return self.list[index]
