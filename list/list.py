class NodeItem:
    def __init__(self, value):
        self.value = value
        self.next_item = None

    def get(self):
        return self.value

    def get_next(self):
        return self.next_item

    def set_next(self, next_item):
        self.next_item = next_item


class ListIterator:
    def __init__(self, source_list):
        self.current_head = source_list.get_head()

    def __next__(self):
        if self.current_head:
            value = self.current_head.get()
            self.current_head = self.current_head.get_next()
            return value
        else:
            raise StopIteration


class List:
    def __init__(self, *args):
        self.__head = None
        self.__tail = None
        for value in args:
            self.__add(value)

    def __iter__(self):
        return ListIterator(self)

    def __str__(self):
        return " ".join(map(str, self))

    def __iadd__(self, other):
        if type(other) == List:
            other = self.get_normal_order(other)
        for item in other:
            self.__add(item)
        return self

    def __add(self, value):
        temp = NodeItem(value)
        temp.set_next(self.__head)
        self.__head = temp

    @staticmethod
    def get_normal_order(list_instance):
        temp_list = List()
        for item in list_instance:
            temp_list.__add(item)
        return temp_list

    def get_head(self):
        return self.__head

    def append(self, *args):
        for value in args:
            self.__add(value)

    def print_reversed(self):
        print(self)

    def print(self):
        print(self.get_normal_order(self))
